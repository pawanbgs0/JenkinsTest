import os
import sys

env_var1 = os.environ.get('ENV_VAR_1', 'Default_Value')
env_var2 = os.environ.get('ENV_VAR_2', 'Default_Value')

if len(sys.argv) > 1:
    script_argument = sys.argv[1]
else:
    script_argument = ""

jenkins_argument = script_argument

print("Value of ENV_VAR_1:", env_var1)
print("Value of ENV_VAR_2:", env_var2)
print("Value of ARGUMENTS:", jenkins_argument)
