import random
import numpy as np
from PIL import Image

im = Image.open('kemerovo.jpg')
p_list1 = np.array(im)

print (p_list1[0][0])
print (p_list1[0][1598])
print (p_list1[1075][0])
print (p_list1[1075][1598])
print(p_list1[1][1])
new_p_list1 = []

for t in range(len(p_list1)+2):
    new_p_list1.append([])
    for f in range(len(p_list1[0])+2):
        new_p_list1[t].append(None)

for t in range(len(p_list1)):
    for f in range(len(p_list1[0])):
        new_p_list1[t+1][f+1] = p_list1[t][f]

new_p_list1[0][0] = p_list1[0][0]
new_p_list1[0][f+1] = p_list1[0][f]
new_p_list1[t+1][0] = p_list1[t][0]
new_p_list1[t+1][f+1] = p_list1[t][f]


for t in range(len(p_list1)):
    for f in range(len(p_list1[0])):
        new_p_list1[t+1][0] = p_list1[t][0]
        new_p_list1[t+1][len(new_p_list1[0])-1] = p_list1[t][len(p_list1[0])-1]
        new_p_list1[0][f+1] = p_list1[0][f]
        new_p_list1[len(new_p_list1)-1][f+1] = p_list1[len(p_list1)-1][f]

print(new_p_list1[2][2])

list2 = []

for e in range(3):
    list2.append([])
    for s in range(3):
        list2[e].append(random.randint(0,1))
print('3 на 3')
print(list2)

listitog = []

for k in range(t):
    listitog.append([])
    for m in range(f):
        listitog[k].append(None)

for k in range(t):
    for m in range(f):
        listitog[k][m] = (new_p_list1[k][m]*list2[0][0])+(new_p_list1[k][m+1]*list2[0][1])+(new_p_list1[k][m+2]*list2[0][2])+(new_p_list1[k+1][m]*list2[1][0])+(new_p_list1[k+1][m+1]*list2[1][1])+(new_p_list1[k+1][m+2]*list2[1][2])+(new_p_list1[k+2][m]*list2[2][0])+(new_p_list1[k+2][m+1]*list2[2][1])+(new_p_list1[k+2][m+2]*list2[2][2])

print(listitog[1][1])

print("Итог")
for z in range(len(listitog)):
    for x in range(len(listitog[0])):
        p_list1[z][x] = listitog[z][x]
print(p_list1[1][1])
img = Image.fromarray(p_list1, 'RGB')
img.show()