# “Don't let the noise of others' opinions
# drown out your own inner voice.”Steve Jobs
#
#
#
# Завдання 1:
# Напишіть функцію, яка виводить на екран відформатований текст, зазначений нижче:
# “Don't let the noise of others'
#     opinions drown out your
#             own inner voice.”
#                     Steve Jobs


def format_text(text):
    text = text.replace("\n","")
    text = text.replace("   ","")
    text = text.replace("  S","S")
    text = text.replace(" d","\nd")
    return text


format_text("""“Don't let the noise of others'
    opinions drown out your
            own inner voice.”
                    Steve Jobs""")
print(format_text("""“Don't let the noise of others'
    opinions drown out your
            own inner voice.”
                    Steve Jobs"""))

# Завдання 2: +
# Напишіть функцію, яка приймає два числа в якості параметрів та виводить всі непарні числа між ними.

def unpaired_number(num1, num2):
    list_unpaired_number = []
    for i in range(num1 +1, num2):
        if i % 2 != 0:
            list_unpaired_number.append(i)
    return list_unpaired_number

unpaired_number(1, 9)


# Завдання 3: +
# Напишіть функцію, яка виводить горизонтальну або вертикальну лінію з певного символу.
# Функція приймає в якості параметрів: довжину лінії, напрямок та символ.

def write_line(lenght, direction, symbol):
    if direction == "horizontal":
        return (lenght * symbol)
    elif direction == "vertikal":
        for i in range(lenght):
            print(symbol)

write_line(7, "vertikal", "*")
write_line(15, "horizontal", "$")
print(write_line(15, "horizontal", "$"))

# Завдання 4: +
# Напишіть функцію, яка повертає максимальне з чотирьох чисел. Числа передаються як параметри.

def max_number(num1, num2, num3, num4):
    num_list = [num1, num2, num3, num4]
    result = max(num_list)
    return result

max_number(4, -16, 13, 9)


# Завдання 5: +
# Напишіть функцію, яка повертає суму чисел у вказаному діапазоні.
# Межі діапазону передаються як параметри.

def sum_numbers(num1, num2):
    result = 0
    for i in range(num1, num2 + 1):
        result += i
    return result

sum_numbers(3, 8)


# Завдання 6: +
# Напишіть функцію, яка перевіряє, чи є число простим. Число передається як параметр.
# Якщо число просте, поверніть true, інакше false.

def prime_num(num):
    flag = True
    if num < 2:
        flag = False
    for i in range(2, int(num)):
            if num % i == 0:
                flag = False
    return flag

prime_num(293)


# Завдання 7:
# Напишіть функцію, яка перевіряє, чи є шестизначне число "щасливим". Число передається як параметр.
# Якщо число щасливе, поверніть true, інакше false. "Щасливе шестизначне число" - це число,
# у якого сума перших трьох цифр дорівнює сумі трьох наступних цифр.
# Наприклад, 123420 - щасливе (1+2+3 = 4+2+0), а 723422 - нещасливе (7+2+3 ≠ 4+2+2).

def lucky_number(num):
    if 100000 <= num <= 999999:
        num1 = num // 100000
        num2 = (num // 10000) % 10
        num3 = (num // 1000) % 10
        num4 = (num // 100) % 10
        num5 = (num // 10) % 10
        num6 = num % 10
        return (num1 + num2 + num3 == num4 + num5 + num6)
    else:
        return False

lucky_number(456780)
