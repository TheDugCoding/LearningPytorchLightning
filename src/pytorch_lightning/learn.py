import os.path as osp

import lightning as L
import torch
import torch.nn.functional as F
import torch_geometric.transforms as T
from torch_geometric.datasets import Planetoid
from torch_geometric.nn import GATConv
from torch.utils.data import DataLoader
from lightning.pytorch.callbacks.early_stopping import EarlyStopping

dataset = 'Cora'
path = osp.join(osp.dirname(osp.realpath(__file__)), '..', '..', 'data',
                dataset)
dataset = Planetoid(path, dataset, transform=T.NormalizeFeatures())


class GAT(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GATConv(dataset.num_features, 8, heads=8, dropout=0.6)

        self.conv2 = GATConv(64, dataset.num_classes, heads=1, concat=True,
                             dropout=0.6)

    def forward(self, x, edge_index):
        x = F.dropout(x, p=0.6, training=self.training)
        x = F.elu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.6, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

class LitGnn(L.LightningModule):
    def __init__(self, gnn_model):
        super().__init__()
        self.gnn = gnn_model

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        out = self.gnn(data.x, data.edge_index)
        loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
        #no need to define the optimizer or backpropagation
        return loss

    def validation_step(self, batch, batch_idx):
        # training_step defines the train loop.
        out = self.gnn(data.x, data.edge_index)
        pred = out[data.val_mask].argmax(1)
        acc = pred.eq(data.y[data.val_mask]).sum().item() / data.val_mask.sum().item()
        #no need to define the optimizer or backpropagation
        self.log("val_acc", acc)

    def test_step(self, batch, batch_idx):
        out = self.gnn(data.x, data.edge_index)
        pred = out[data.test_mask].argmax(1)
        acc = pred.eq(data.y[data.test_mask]).sum().item() / data.test_mask.sum().item()
        self.log("test_acc", acc)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.gnn.parameters(), lr=0.005, weight_decay=5e-4)
        return optimizer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_gat, data = GAT().to(device), dataset[0].to(device)
model_gat = torch.jit.script(model_gat)
train_loader = DataLoader(data.x[data.train_mask], batch_size=32, shuffle=True)
val_loader = DataLoader(data.x[data.val_mask], batch_size=32, shuffle=True)
test_loader = DataLoader(data.x[data.test_mask], batch_size=32, shuffle=True)



# model
model_gnn = LitGnn(model_gat)

# train model define early stopping
early_stop_callback = EarlyStopping(monitor="val_acc", min_delta=0.01, patience=5, verbose=False, mode="max")
trainer = L.Trainer(max_epochs=90, callbacks=[early_stop_callback], profiler="simple")
trainer.fit(model=model_gnn, train_dataloaders=train_loader, val_dataloaders=val_loader)

trainer.test(model_gnn, dataloaders=test_loader)