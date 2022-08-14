for row in range(1, 10):
    for col in range(1, 10):
        num = col * row
        if num < 10: print('0', end = '')
        print(num, end = ' ')
    print()