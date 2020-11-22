import random

p_list1 = []

for i in range(10):
    p_list1.append([])
    for j in range(10):
        p_list1[i].append(random.randint(0,2))
print("Исходный массив")
print(p_list1)
print("Углы")
print("vl", p_list1[0][0], "vp", p_list1[0][len(p_list1[0])-1], "nl", p_list1[len(p_list1[0])-1][0], "np", p_list1[len(p_list1[0])-1][len(p_list1[0])-1])


new_p_list1 = []

for t in range(len(p_list1)+2):
    new_p_list1.append([])
    for f in range(len(p_list1[0])+2):
        new_p_list1[t].append(None)

for t in range(len(p_list1)):
    for f in range(len(p_list1[0])):
        new_p_list1[t+1][f+1] = p_list1[t][f]

new_p_list1[0][0] = p_list1[0][0]
new_p_list1[0][len(new_p_list1[0])-1] = p_list1[0][len(p_list1[0])-1]
new_p_list1[len(new_p_list1[0])-1][0] = p_list1[len(p_list1[0])-1][0]
new_p_list1[len(new_p_list1[0])-1][len(new_p_list1[0])-1] = p_list1[len(p_list1[0])-1][len(p_list1[0])-1]

for t in range(len(p_list1)):
    for f in range(len(p_list1[0])):
        new_p_list1[t+1][0] = p_list1[t][0]
        new_p_list1[t+1][len(new_p_list1[0])-1] = p_list1[t][len(p_list1[0])-1]
        new_p_list1[0][f+1] = p_list1[0][f]
        new_p_list1[len(new_p_list1[0])-1][f+1] = p_list1[len(p_list1[0])-1][f]


print("Исходный массив с углами и доп. сторонами")
print(new_p_list1)


list2 = []

for e in range(3):
    list2.append([])
    for s in range(3):
        list2[e].append(random.randint(0,2))

print(list2)

listitog = []

for k in range(len(p_list1)):
    listitog.append([])
    for m in range(len(p_list1)):
        listitog[k].append(None)

for k in range(len(p_list1)):
    for m in range(len(p_list1)):
        listitog[k][m] = (new_p_list1[k][m]*list2[0][0])+(new_p_list1[k][m+1]*list2[0][1])+(new_p_list1[k][m+2]*list2[0][2])+(new_p_list1[k+1][m]*list2[1][0])+(new_p_list1[k+1][m+1]*list2[1][1])+(new_p_list1[k+1][m+2]*list2[1][2])+(new_p_list1[k+2][m]*list2[2][0])+(new_p_list1[k+2][m+1]*list2[2][1])+(new_p_list1[k+2][m+2]*list2[2][2])

print("Итог")
print(listitog)