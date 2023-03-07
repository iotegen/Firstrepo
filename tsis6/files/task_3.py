import os

p = input()

if os.path.exists(p):
    filename = os.path.basename(p)
    dirname = os.path.dirname(p)
    print(f"Filename of the path :",filename )
    print(f"directory portion of the given path ':", dirname)
    
else:
    print("path does not exists")