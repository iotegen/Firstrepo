def copyFromFile1ToFile2(file1, file2):
    f1 = open(f"{file1}", "r")
    f2 = open(f"{file2}", "w")
    f2.write(f1.read())
    f1.close()
    f2.close()
    
file1 = input()
file2 = input()

copyFromFile1ToFile2(file1, file2)


    