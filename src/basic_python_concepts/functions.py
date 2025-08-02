

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

