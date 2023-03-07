
def file_generator():
    for i in range(26):
        filename = chr(65 + i)
        open(f"{filename}.txt", "x")
        
file_generator()
