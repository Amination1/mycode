def is_star_number(x):
    n = 1
    while True:
        star_num = n * (n + 1)
        if star_num == x:
            return True
        elif star_num > x:
            return False
        n += 1

numbers = []
try:
    with open("input.txt", 'r') as inputfile:
        for number in inputfile:
            if number.strip().isnumeric():
                numbers.append(int(number.strip()))
except FileNotFoundError:
    print("فایل ورودی پیدا نشد.")
    exit(1)

with open("output.txt", 'w') as outputfile:
    for i in numbers:
        if is_star_number(i):
            outputfile.write("OK\n")
        else:
            outputfile.write("NOK\n")
exit(0)