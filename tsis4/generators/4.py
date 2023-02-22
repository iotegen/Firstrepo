# n = int(input())
# squares = [i**2 for i in range(n)]

# for i in squares:
#     print(i)

def squares(a, b):
    for i in range(a, b + 1):
        yield i*i


a = int(input("введите 'a' :"))
b = int(input("введите 'b' :"))

for x in squares(a, b):
    print(x)