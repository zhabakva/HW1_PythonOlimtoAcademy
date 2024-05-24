def summ(n):
    summa = 0
    x = n
    while x != 0:
        summa += x % 10
        x //= 10
    return summa


x = "!"
while not x.isdigit():
    x = input("Enter any INTEGER number")
x = int(x)
while x > 9:
    x = summ(x)
print(x)
