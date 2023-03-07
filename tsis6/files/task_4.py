txtfile = input("write the text file(without ext. 'txt'):")

f = open(f"{txtfile}.txt", "r")

print(f"Number of lines in '{txtfile}.txt':",len(f.readlines()))

f.close()