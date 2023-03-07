#Write a Python program with builtin function that returns True if all elements of the tuple are true.

def TrueTuple(tpl):
    return all(tpl)

t = (1, 3, "hello", 0)

print(TrueTuple(t))
