def main():
    str = ' Looping structure is Python using while / for'
    print(str)

    count1 = int(input('Enter a count1 number: '))
    count2 = int(input('Enter a count2 number: '))

    while count1 < 10:
        print('The value of count 1 is ', count1)
        count1 += 3

    print('\nUsing for loop')

    for i in range(count2):
        print('The value of Count 2 is ', i)

    print('\nUsing for loop with set of value')

    for i in [2, 4, 18, 21]:
        print('The value of i is', i)

    print('\nUsing for loop with start, threshold')

    for i in range(10, 15):
        print('The value of i is ', i)

    print('\nUsing for loop with start, threshold, increment')

    for i in range(10, 20, 4):
        print('The value of i is ', i)

    print('\nUsing for loop with start, threshold, backward increment')

    for i in range(15, 10, -22):
        print('The value of i is ', i)


main()