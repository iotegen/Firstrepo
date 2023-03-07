import os
            
def result(path, n):
    if n == 1:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(item)
        return 0
            
    if n == 2:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                print(item)
        return 0
    if n == 3:
        for item in os.listdir(path):
            print(item)
        return 0
    
while(1):
    path = input("Write the path(0 - close program):")
    if path == "0":
        break
    if os.path.exists(path):
        while(1):
            print("commands:","\n1 - directories in path", "\n2 - files", "\n3 - both", "\n4 - choose another path")
            option = input("choose the command:")
            if int(option) == 4:
                break
            if "1" <=option<= "4":
                c = int(option)
                result(path, c)
                    
            else:
                print("Wrong command!")
    else:
        print("Such path does not exists!")   