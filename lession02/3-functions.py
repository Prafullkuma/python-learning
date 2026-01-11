# Function

def hello():
    print("Hello world")

hello()

def get_string():
    print("Helloe")

get_string()


def sum(num1, num2):
    print(num1+ num2)
sum(1,2)

def calculation(*args):
    print(args) # return tuples 

calculation(1,2,2,3,3)


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dict

mult_named_items(first="Prafull", second="Revan", last="bindu")

# returing value 

# Verifying passing number
def returing_values(num1, num2):
    if isinstance(num1, int) or isinstance(num2, int):
       return num1 + num2
    else:
        print("In valid input")  # return None  
        return 0 # Best practice

print(returing_values("dkalsd","dlaskda"))





