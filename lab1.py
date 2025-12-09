
if __name__ == "__main__":
    print("Выполнил: Опекунов Николай R3142\nВариант 6\n")



# №1

    print("№1 Cтран: Таиланд")

    RED = '\u001b[41m'
    WHITE = '\u001b[47m'
    BLUE = '\u001b[44m'
    BLACK = '\u001b[40m'
    GREEN = '\u001b[42m'
    END = '\u001b[0m'
    flag_height = 8
    flag_width = 16
    for i in range(1, flag_height):
        if i == 1 or i == 7:
            print(f'{RED}{"  " * (flag_width)}{END}')
        if i == 2 or i == 6:
            print(f'{WHITE}{"  " * (flag_width)}{END}')
        if 3 <= i <= 5:
            print(f'{BLUE}{"  " * (flag_width)}{END}')
    print('\n')



# №2

    print("№2 Узор: f")

    # for i in range(1,7):
    #     if i == 1:
    #         print(f'{WHITE}{"  " * (6)}{BLACK}{"  " * (1) }{WHITE}{"  " * (6)}{END}')
    #     elif i%2==0 and i!=6:
    #         print(f'{WHITE}{"  " * (6-i+1) }{BLACK}{"  " * 1}{WHITE}{"  " * (2*i-3) }{BLACK}{"  " * 1 }{WHITE}{"  " * (6-i+1) }{END}')
    #     elif (i%2==1 and i!=1) or i==6:
    #         print(f'{WHITE}{"  " * (6-i) }{BLACK}{"  " * 2}{WHITE}{"  " * (2*i-3) }{BLACK}{"  " * 2 }{WHITE}{"  " * (6-i) }{END}')
    # print(f'{END}')

    pattern_height = 7
    pattern_width = 1
    for i in range(pattern_width, pattern_height):
        if i == 1:
            print(f'{WHITE}{"  " * (6)}{BLACK}{"  " * (1) }{WHITE}{"  " * (6)}{END}')
        elif 2 <= i <=3 :
            print(f'{WHITE}{"  " * (6-i+1) }{BLACK}{"  " * 1}{WHITE}{"  " * (2*i-3) }{BLACK}{"  " * 1 }{WHITE}{"  " * (6-i+1) }{END}')
        elif 4 <= i <=6 :
            print(f'{WHITE}{"  " * (6-i) }{BLACK}{"  " * 2}{WHITE}{"  " * (2*i-3) }{BLACK}{"  " * 2 }{WHITE}{"  " * (6-i) }{END}')
    print('\n')



# №3

    print("№3 График: y = 1 / x")

    graph_height = graph_width= 10
    pos=[]
    for x in range(1, graph_width + 1):
        y = 1 / x
        y_pos = int(y * (graph_height - 1) + 0.5)
        if y_pos < 0:
            y_pos = 0
        if y_pos > graph_height - 1:
            y_pos = graph_height - 1
        pos.append(y_pos)
    for row in range(graph_height -1, -1, -1):
        print(f'{row} | ', end='')
        for col in range(graph_width):
            if pos[col] == row:
                print(f'{BLACK}{"  "}{END}', end='')
            else:
                print(f'{WHITE}{"  "}{END}', end='')
        print()
    print('    ' + '-' * (graph_width * 2))
    x_labels = ' '.join(str(i) for i in range(1, graph_width + 1))
    print('    ' + x_labels)
    print('\n')



# №4

    print("№4 Условие: Числа больше 5 и меньше 5, отрицательные отбросить")

    file = open('sequence.txt', 'r')
    list_plus = []
    list_minus = []
    for num in file:
        if float(num) > 5:
            list_plus.append(num)
        if float(num) > 0 and float(num) < 5:
            list_minus.append(num)
    len_plus = len(list_plus)
    len_minus = len(list_minus)
    proc_pl = ((len_plus / (len_plus + len_minus)) * 100) 
    proc_min = ((len_minus / (len_plus + len_minus)) * 100)
    print(f'{GREEN}{"  "}{BLACK}{" Числа от 0 до 5 | кол-во: "}{len_minus}{" | процентное соотношение: "}{round(proc_min , 1)}{" %"}{END}')
    print(f'{RED}{"  "}{BLACK}{" Числа от 5 до ∞ | кол-во: "}{len_plus}{" | процентное соотношение: "}{round(proc_pl , 1)}{" %"}{END}')
    print(f'{round(proc_min , 1)}{" % "}{GREEN}{"  " * int(proc_min // 10)*2}{RED}{"  " * int(proc_pl// 10)*2}{BLACK}{" "}{round(proc_pl , 1)}{" %"}{END}')
    file.close()

    