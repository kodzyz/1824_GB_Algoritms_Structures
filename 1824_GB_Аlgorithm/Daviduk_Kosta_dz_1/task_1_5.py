# Задача 5
# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

#'A','z' ->
# место в алфавите 'A':  1
# место в алфавите 'Z':  26
# букв между 'A'и'Z': 24
#'z','A' ->
# место в алфавите 'z':  26
# место в алфавите 'a':  1
# букв между 'z'и'a': 24

# n1 = input("Первый символ: ")
# n2 = input("Второй символ: ")
n1 = 'F'
n2 = 'n'
# бол ингл
if  n1.isupper() and 65 <= ord(n1) <= 90 and 65 <= ord(n2.upper()) <= 90:
    print(f"место в алфавите '{n1}':  {ord(n1) - 65 + 1}")  # рус.
    print(f"место в алфавите '{n2.upper()}':  {ord(n2.upper()) - 65 + 1}")
    print(f"букв между '{n1}'и'{n2.upper()}': {abs(ord(n1) - ord(n2.upper())) - 1}")
# мал ингл
elif n1.islower() and 97 <= ord(n1) <= 122 and 97 <= ord(n2.lower()) <= 122:
    print(f"место в алфавите '{n1}':  {ord(n1) - 97 + 1}")  # рус.
    print(f"место в алфавите '{n2.lower()}':  {ord(n2.lower()) - 97 + 1}")
    print(f"букв между '{n1}'и'{n2.lower()}': {abs(ord(n1) - ord(n2.lower())) - 1}")
else:
    print('Введите так, чтобы буквы принадлежали к английскому языку!')

# место в алфавите 'F':  6
# место в алфавите 'N':  14
# букв между 'F'и'N': 7