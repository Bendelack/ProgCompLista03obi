def primo(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    cont = 3
    while 2*cont <= x:
        if x % cont == 0:
            return False
        cont += 2
    return True
    
n = int(input())
for i in range (n):
    x = int(input())
    if primo(x):
        print('S')
    else:
        print('N')