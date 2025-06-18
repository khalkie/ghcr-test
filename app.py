# This is a comment - comments start with a '#'
# This program prints a greeting to the console.

def greet(name):
    """
    This function takes a name as input and returns a greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This block of code runs only when the script is executed directly
    user_name = "World"
    message = greet(user_name)
    print(message)

    # You can also use a different name
    another_name = "Pythonista"
    print(greet(another_name))
