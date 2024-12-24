import random

# sta = "/storage/emulated/0/python/"+input("file name : ")+".txt"
# f = open(sta , "r")
# dc_word = f.read()

list = ["apple", "banana", "apricot", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]
random.shuffle(list)
cond = 12
unique_list = []
used_f_l = set()
l_st = []
for i in range(min(cond, len(list))):
    word = list[i]
    f_l = word[0].lower()
    if f_l not in used_f_l:
        unique_list.append(word)
        used_f_l.add(f_l)

print(unique_list)