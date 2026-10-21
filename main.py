import os
import time


WHITE = '\u001b[47m'
RED = '\u001b[41m'
RESET = '\u001b[0m'


#Флаг Японии
def flag(radius=4.8):
    pixel = '  '
    lenght = 24
    height = 16
    cx = lenght/2
    cy = height/2
    for y in range(height):
        line = ''
        for x in range(lenght):
            if (x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2 <= radius ** 2: #по уравнению окружности проверяем, входит ли точка в круг
                line += RED+pixel
            else:
                line += WHITE+pixel
        print(line+RESET)


#Узор g
def pattern():
    pixel = '  '
    size = 3 #расстояние от центра до вершины ромба
    period = 4*size #ширина узора, в одном узоре 2 ромба
    repeats = 5
    height = 2*size + 1 #+1 для центральной линии

    for i in range(height):
        dist = abs(i - size) #расстояние от строки до центральной
        line = ''
        for j in range(period*repeats):
            c = j % period #позиция в узоре
            k = min(abs(c - size), abs(c - 3 * size)) #расстояние до ближайшего центра
            if k + dist == size: #если точка находится на границе ромба по формуле |x| + |y| = r
                line += WHITE + pixel + RESET
            else:
                line += pixel
        print(line)


#График y = 3x
def graph():
    height = 12
    scale = 4 #4 символа на один x

    for y in range(height, -1, -1): 
        print(f'{y:2} |')
    print('   +--------------------')
    print('    0   1   2   3   4   5')

    for y in range(height + 1):
        x = y / 3
        i = round(x * scale)
        up = y + 3 #вверх на 3 строки, тк график начинается с 3

        print(f'\033[{up}A', end='') #перемещаемся вверх в нужный y
        print(f'\033[{i + 4}C', end='') #перемещаемся вверх в нужный x
        print(f'{RED} {RESET}', end='') #ставим точку
        print(f'\033[{up}B', end='') #возвращаемся в начальный y
        print(f'\033[{i + 5}D', end='') #возвращаемся в начальный x
    print()


#Диаграмма про числа больше -5 и меньше -5, положительные отбросить
def sequence():
    file = open('sequence.txt', 'r')
    bolshe = []
    menshe = []
    for line in file:
        number = float(line)
        if number > 0:
            continue
        if number > -5:
            bolshe.append(number)
        elif number < -5:
            menshe.append(number)
    file.close()

    total = len(bolshe) + len(menshe)
    print(f'Больше -5: {len(bolshe)}, меньше -5: {len(menshe)}')
    print(f'{RED}{' ' * int(len(bolshe) / 2)}{RESET} {len(bolshe) / total * 100}%  (больше -5)')
    print(f'{WHITE}{' ' * int(len(menshe) / 2)}{RESET} {len(menshe) / total * 100}%  (меньше -5)')


#Анимация. Солнце на флаге Японии растёт
def animation():
    clear = 'cls' if os.name == 'nt' else 'clear'
    for radius in [3, 4, 4.8, 4, 3]: 
        os.system(clear)
        flag(radius)
        time.sleep(1)


flag()
pattern()
graph()
sequence()

a = input('Напишите w для запуска анимации: ')
if a == 'w': animation()