x = "-1"
while not x.isdigit() or int(x) > 999 or int(x) < 0:
    x = input("Enter any natural number from 0 to 999")
n = int(x)
hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]


result = (hundreds[n // 100]+" ")
n = n % 100
if 10 < n < 20 :
    if n == 11:
        result += ("одиннадцать")
    if n == 12:
        result+=("двенадцать")
    if n == 13:
        result+=("тринадцать")
    if n == 14:
        result+=("четырнадцать")
    if n == 15:
        result+=("пятнадцать")
    if n == 16:
        result+=("шестнадцать")
    if n == 17:
        result+=("семнадцать")
    if n == 18:
        result+=("восемнадцать")
    if n == 19:
        result+=("девятнадцать")
else:
    result += (tens[(n // 10)]+ " " + ones[n % 10])
print(result)
