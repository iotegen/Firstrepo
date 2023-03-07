import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"file '{os.path.basename(path)}' was deleted")
        else:
            print("you do not have access")
    else:
        print("path does not exists")
        
p = input()
delete_file(p)