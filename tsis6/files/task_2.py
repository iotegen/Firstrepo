import os

path = input("Write the path:")

#Check existing
if os.path.exists(path):
    print(f"path '{path}' exists")
else:
    print(f"path '{path}' does not exists")
    
#Check readability
if os.access(path, os.R_OK):
    print(f"path '{path}' is readable")
else:
    print(f"path '{path}' is not readable")

#Check writability
if os.access(path, os.W_OK):
    print(f"path '{path}' is writable")
else:
    print(f"path '{path}' is not writable")
    
#Check executability
if os.access(path, os.X_OK):
    print(f"path '{path}' is executable")
else:
    print(f"path '{path}' is not executable")