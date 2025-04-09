def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called:")
        func()
        print("Something is happenung after the function is called:")
    return wrapper
def say_hello():
    print("Hello!, please enter your greetings")
    greet=str(input("enter your greetings:"))
    print(greet)
say_hello()