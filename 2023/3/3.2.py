global_variable = 10  # Global variable

def my_function():
    global_variable = 20  # Local variable with the same name as global

    # Accessing the global variable within the function
    print("Local variable:", global_variable)  # Accessing the local variable
    print("Global variable:", globals()['global_variable'])  # Accessing the global variable

my_function()
