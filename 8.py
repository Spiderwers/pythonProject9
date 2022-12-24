for x in '0123456789ABCD':
    t = int('1' + x + '563', 14) + int('871' + x + '3', 14)
    if t % 24 == 0:
        print(t // 24)
        exit()
