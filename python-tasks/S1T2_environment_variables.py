import os

def print_specific_env_variable(variable_name):
    try:
        value = os.environ[variable_name]
        print(f"The value of {variable_name} is: {value}")
    except KeyError:
        print(f"The environment variable {variable_name} does not exist.")

#env_variable = input("Enter the name of the environment variable: ")
env_variable = "USER"
print_specific_env_variable(env_variable)

