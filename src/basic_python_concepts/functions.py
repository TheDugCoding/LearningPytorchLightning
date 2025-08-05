

def pizza():
    #This is the body of the function
    print('toppings')

def multiply(number):
    #number is a parameter
    return number * 2

#we can set a default value for a function
def multiple_parameters(k, numbers=(1,2,3)):
    return [x * k for x in numbers], k

def test_list(new_list):
    new_list[0] += 1

if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5]
    k = 2

    pizza()
    print(multiply(4)) #4 is the argument of the function
    print(multiple_parameters(k, numbers))

    #keywords arguments
    print(multiple_parameters(k=k, numbers =numbers))

    print(numbers)
    test_list(numbers)
    print(numbers)

#https://realpython.com/python-kwargs-and-args/
#args and kwargs
'''suppose you don't know how many parameters you want to pass to a function you can then use 
args and kwargs for this purpose
args are positional arguments   func(1, 2, 3)
kwargs are keyword arguments   func(a=1, b=2, c=3)

iterable unpacking
a, *b, c = [1, 2, 3, 4, 5]
print(b)
# [2, 3, 4]
'''

#args is considered a tuple here
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
