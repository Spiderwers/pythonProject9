'''for x in '0123456789ABCD':
    t = int('1' + x + '563', 14) + int('871' + x + '3', 14)
    if t % 24 == 0:
        print(t // 24)
        exit()'''

x = 5 ** 36 + 5**24 - 25
s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count("4"))
