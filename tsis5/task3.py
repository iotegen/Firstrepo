import re

text = "aa_f_aslkdj_"

pat = r"[a-z]+_[a-z]+"

x = re.findall(pat, text)

print(x)