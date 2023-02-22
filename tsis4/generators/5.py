N = int(input())

numbers = (i for i in range(N, -1, -1))

print(type(numbers))

for number in numbers:
    print(number)