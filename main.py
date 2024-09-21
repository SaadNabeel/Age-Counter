
def checkevenorodd(age):
    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")


try:
    age = int(input("Enter your age: "))
    
 
    if age <= 0 or age > 120:
        raise ValueError("Age must be a positive number between 1 and 120.")
    
    
    checkevenorodd(age)
    
except ValueError as e:
    print("Error:", e)
