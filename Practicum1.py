def number_to_string(number):
    mapping_number_string = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety'
    }

    # convert the number to text
    if 0 <= number <= 20 or number % 10 == 0:
        return mapping_number_string[str(number)]
    else:
        return mapping_number_string[str(number // 10 * 10)] + '-' + mapping_number_string[str(number % 10)]


def replace_number_with_string(user_string):
    words = user_string.split()
    result = []

    for word in words:
        if word.isdigit() and 0 <= int(word) <= 99:
            result.append(number_to_string(int(word)))
        else:
            result.append(word)
    return ' '.join(result)


def main():
    # get input from user
    user_string = input("Enter a string: ")

    end_string = replace_number_with_string(user_string)
    print("Result:", end_string)


if __name__ == '__main__':
    main()
