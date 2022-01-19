while True:
    num = int(input("Sayı Gir"))
    num2 = str(num)
    lenght = len(num2)
    toplam = 0
    for i in num2:
        force = int(i) ** lenght
        toplam += force
    if toplam == num:
        print("{}' is Armstrong number.".format(num))
    else:
        print("{}' is not a Armstrong number.".format(num))