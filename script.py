import os

env_var1 = os.environ.get('ENV_VAR_1', 'Default_Value')
env_var2 = os.environ.get('ENV_VAR_2', 'Default_Value')

print("Value of ENV_VAR_1:", env_var1)
print("Value of ENV_VAR_2:", env_var2)
