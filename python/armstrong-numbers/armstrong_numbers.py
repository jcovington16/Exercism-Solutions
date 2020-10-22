def is_armstrong_number(number):
    number_val = str(number)
    count, size = 0, len(number_val)

    for i in number_val:
        count += int(i) ** size

    return count == number
