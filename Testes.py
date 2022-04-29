import random
t = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
n = 0
l = [0,1,2,3,4,5,6,7,8]
while n < 1:
    lista =[t[0][0],t[0][1],t[0][2],t[1][0],t[1][1],t[1][2],t[2][0],t[2][1],t[2][2]]
    x = random.choice(l)
    n1 = lista[x]
    print(n1)
    if n1 ==" ":
        n1 ="O";
        continuar = "n"
        break
