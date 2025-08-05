from pathlib import Path

#I create this function mostly because the path relative position depends on the location from which we call the program
def retrieve_data_path():
    #current working directory
    cwd = Path.cwd()
    #print absolute path
    print(cwd)
    while cwd.name != 'src':
        cwd = cwd.parent
    return cwd.parent.joinpath('data')