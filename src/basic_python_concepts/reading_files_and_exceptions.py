from pathlib import Path

#there is also the os library, but it is considered old school

#I create this function mostly because the path relative position depends on the location from which we call the program
def retrieve_data_path():
    #current working directory
    cwd = Path.cwd()
    #print absolute path
    print(cwd)
    while cwd.name != 'src':
        cwd = cwd.parent
    return cwd.parent.joinpath('data')


# reading a file data should always be in the data folder
path = Path('../../data/basic_python_data/pi_digits.txt')
#read_text add a blank at the end of the string
contents = path.read_text().rstrip()
print(contents)

lines = contents.split()
for line in lines:
    print(line)

cwd = Path.cwd()
path_txt_file = retrieve_data_path().joinpath('basic_python_data/pi_digits.txt')
#check file exists
print(path_txt_file.exists())
#print file extension
print(path_txt_file.suffix)
#iterate over all files and directories
for entry in cwd.iterdir():
    print(entry)
print('\n')
for entry in cwd.iterdir():
   if entry.is_dir():
      print(entry.name, 'is a directory')
   elif entry.is_file():
       print(entry.name, 'is a file')

#use glob to find files with specific extensions
files = list(retrieve_data_path().joinpath('basic_python_data').glob("*.txt"))
print(files)


#writing to a file
path_txt_file_writing = retrieve_data_path().joinpath('basic_python_data/programming.txt')
#if the file doesn't exist it creates one, write_text will erase everything contained in the file
path_txt_file_writing.write_text('why are you so serious?')




'''---exceptions---'''

'''
here is how exceptions are handled (keywords are in order)
-   try: try to run this code, if something goes wrong throw an exception
-   except: catch the exception, we can have multiple except. If we don't write the type of the exception, except will 
    catch any exception that is thrown
-   else: execute the code in else if no exception is thrown
-   finally: execute the code in finally with or without exceptions

'''

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Please change 'y' argument to non-zero value")
    except:
        print("Something went wrong")
    else:
        print(f"Your answer is {result}")
    finally:
        print("\033[92m Code by DataCamp\033[00m")



#try to execute the code if it doesn't work the except will catch the error
#you need to catch the correct exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#we can also handle  multiple exceptions
try:
   print(1/0)
except ZeroDivisionError:
   print("You cannot divide a value with zero")
except:
   print("Something else went wrong")

#we can also raise our own exception raise ValueError
#custom Exception raise Exception("Please add a value lower than 1,000")

'''common python exceptions

https://docs.python.org/3/library/exceptions.html

AssertionError: raised when the assert statement fails.
EOFError: raised when the input() function meets the end-of-file condition.
AttributeError: raised when the attribute assignment or reference fails.
TabError: raised when the indentations consist of inconsistent tabs or spaces. 
ImportError: raised when importing the module fails. 
IndexError: occurs when the index of a sequence is out of range
KeyboardInterrupt: raised when the user inputs interrupt keys (Ctrl + C or Delete).
RuntimeError: occurs when an error does not fall into any category. 
NameError: raised when a variable is not found in the local or global scope. 
MemoryError: raised when programs run out of memory. 
ValueError: occurs when the operation or function receives an argument with the right type but the wrong value. 
ZeroDivisionError: raised when you divide a value or variable with zero. 
SyntaxError: raised by the parser when the Python syntax is wrong. 
IndentationError: occurs when there is a wrong indentation.
SystemError: raised when the interpreter detects an internal error.
'''

#we can add else when no exception is raised
try:
   result = 1/3
except ZeroDivisionError as err:
   print(err)
else:
   print(f"Your answer is {result}")

#from python 3.10 it is possible to handle multiple exceptions more elegantly
try:
    result = 1 / 0
except Exception as e:
    match e:
        case ZeroDivisionError():
            print("You cannot divide by zero.")
        case NameError():
            print("Variable not defined.")
        case _:
            print("An unexpected error occurred.")


