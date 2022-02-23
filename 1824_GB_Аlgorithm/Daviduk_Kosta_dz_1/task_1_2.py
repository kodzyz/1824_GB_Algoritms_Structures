# Задача 2
# Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

#5,6 ->
# 0b101 | 0b110 = 0b111 = 7
# 0b101 & 0b110 = 0b100 = 4
# 0b101 ^ 0b110 = 0b11 = 3
# 0b101 << 2 = 0b10100 = 20
# 0b101 >> 2 = 0b1 = 1

n1 = 5
n2 = 6
print(f'{bin(int(n1))} | {bin(int(n2))} = {bin(int(n1) | int(n2))} = {int(bin(int(n1) | int(n2)),2)}')
print(f'{bin(int(n1))} & {bin(int(n2))} = {bin(int(n1) & int(n2))} = {int(bin(int(n1) & int(n2)),2)}')
print(f'{bin(int(n1))} ^ {bin(int(n2))} = {bin(int(n1) ^ int(n2))} = {int(bin(int(n1) ^ int(n2)),2)}')
print(f'{bin(int(n1))} << 2 = {bin(int(n1) << 2)} = {int(bin(int(n1) << 2),2)}')
print(f'{bin(int(n1))} >> 2 = {bin(int(n1) >> 2)} = {int(bin(int(n1) >> 2),2)}')