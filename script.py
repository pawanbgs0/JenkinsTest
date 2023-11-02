import os

env_var1 = os.environ.get('ENV_VAR_1', 'Default_Value')
env_var2 = os.environ.get('ENV_VAR_2', 'Default_Value')

if env_var1 in os.environ:
    value1 = os.environ[env_var1]
else:
    value1 = "Environment variable 1 not set"

if env_var2 in os.environ:
    value2 = os.environ[env_var2]
else:
    value2 = "Environment variable 2 not set"

print("Value of ENV_VAR_1:", value1)
print("Value of ENV_VAR_2:", value2)