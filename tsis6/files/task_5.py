def list_into_file(list, filename):
    file = open(f"{filename}", "w")
    file.writelines(lst)
    file.close()

lst = input().split()

filename = input()

list_into_file(lst, filename)