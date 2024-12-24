import random

# sta = "/storage/emulated/0/python/"+input("file name : ")+".txt"
with open("C:\\Users\\Admin\\Desktop\\test.txt", "r") as f:
    dc_word = f.readlines()
list = [word.strip() for word in dc_word]
random.shuffle(list)
cond = 12
unq_l = []
used_f_l = set()
l_st = []
for i in range(min(cond, len(list))):
    word = list[i]
    f_l = word[0].lower()
    if f_l not in used_f_l:
        unq_l.append(word)
        used_f_l.add(f_l)

print(' '.join(unq_l),end="")