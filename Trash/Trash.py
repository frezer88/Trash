import os
import random

platforma = [['||','=','=','=',' ',' '],
             ['||',' ',' ','|',' ',' '],
             ['||',' ',' ','|',' ',' '],
             ['||',' ',' ','O',' ',' '],
             ['||',' ','/','|','\\',' '],
             ['||',' ','/',' ','\\',' '],
             ['||',' ',' ',' ',' ',' '],
             ['||',' ',' ',' ',' ',' '],
             ['||',' ',' ',' ',' ',' '],
             ['=','=','=','=','=','=']]

def Works():
    works = ['инкапсуляция','универ','планиметрия','ассемблер','моделирование','бухгалтерия','многопоточность','изокванта','максимизация']
    x = random.randint(0,len(works)-1)
    return works[x]


def Print(error,end,abs):#Обработка ошибок
    
    if error == 0:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 1:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0:
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end

    elif error == 2:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2:
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 3:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2 or i == 3:
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 4:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2 or i == 3:
                    print(platforma[i][j], end='')
                elif i == 4 and j == 3:
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 5:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2 or i == 3:
                    print(platforma[i][j], end='')
                elif i == 4 and (j == 3 or j == 2):
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 6:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2 or i == 3:
                    print(platforma[i][j], end='')
                elif i == 4 and (j == 3 or j == 2 or j == 4):
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end
    elif error == 7:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                if i == len(platforma)-1:
                    print(platforma[i][j], end='')
                elif i == 0 or i == 1 or i == 2 or i == 3:
                    print(platforma[i][j], end='')
                elif i == 4 and (j == 3 or j == 2 or j == 4):
                    print(platforma[i][j], end='')
                elif i == 5 and j == 2:
                    print(platforma[i][j], end='')
                elif j == 0:
                    print(platforma[i][j], end='')
                else:
                    print(' ', end='')
            print()
        print('Использованные буквы: ',end = '')
        for i in abs:
            print(i,end = ' ')
        print('\n')
        for i in work2:
            print(i,end = ' ')
        return end

    else:
        for i in range(len(platforma)):
            for j in range(len(platforma[0])):
                    print(platforma[i][j], end='')
            print()
        print('GAME OVER','\nСлово:',work)
        end = False
        return end

def Button(work,work2,error,win,abs):#обработка буквы которую нажали
    work.split()
    x = input('Введите букву: ')
    x = x.lower()
    if len(x) == 1:
        if x.isalpha() == True:
            if abs.find(x) == -1:
                abs = abs + str(x)
                if work.find(x) != -1:
                    for i in range(len(work)):
                        if work[i] == x:
                            work2[i] = x
                            win-=1#нужно пофиксить когда в слове несколько одинаковых букв, и добавить обработку нескольких букв и слова

                else:
                    error+=1
        else:
            error+=1
    os.system('cls||clear')
    return error,Print(error,end,abs),win,abs

error = 0
end = True
abs = ''
work = Works()
work2 = list(work)
win = len(work2)
for i in range(len(work2)):
    work2[i] = '_ '
Print(error,end,abs)
while end:
    error,end,win,abs = Button(work,work2,error,win,abs)
    if win == 0:
        print("\nYOU WIN")
        end = False

