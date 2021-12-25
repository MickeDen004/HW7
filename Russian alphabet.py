# alpha = dict(zip([i for i in range(21)], ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']))
# print(alpha)
num = [i for i in range(1, 32)]
alpha = [chr(b) for b in range(1040, 1071)]
ALPHA = dict(zip(num, alpha))
print(ALPHA)