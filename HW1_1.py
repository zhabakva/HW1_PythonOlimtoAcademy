x = "0"
while not x.isdigit() or x == "0":
    x = input("Enter any NATURAL number ")
res = ""
x = int(x)
for i in range(x - 1, -1, -1):
    res += ' ' * i + '*' * (2 * x - 2 * i - 1) + ' ' * i + '\n'
print(res)
