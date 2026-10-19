def main():
    str = 'Temperature Conversion'
    print(str)

    do_repeat = 'y'

    while do_repeat == 'y':

        temp_far = float(input('Enter a temperature in Fahrenheit: '))

        temp_cel = (temp_far - 32) * (5 / 9)

        print(
            'The conversion of temp fahrenheit',
            temp_far,
            'is',
            format(temp_cel, '.2f'),
            'celcius'
        )

        do_repeat = input('Do you want to repeat the conversion? (y/n) ')


main()