import os
# print(os.environ)
print(os.environ["PYTHONPATH"])
os.environ["User"]="root"
print(os.environ["User"])
varPath="Users/$User/bin"
actPath=os.path.expandvars(varPath)
print(actPath)
