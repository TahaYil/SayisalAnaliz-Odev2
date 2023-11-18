e = 2.71828182845904


def fonksyon(x0):
    y = 0;
    for i in range(0, 4):
        y = 4 * (e ** ((-1 * x0) / 2))
        x0 = y
    return x0


x0 = float(input("e⁻⁰˙⁵ˣ-x fonksyonun yaklaşık kök değeri için x in başlangıç değerini giriniz : "))
print("4 literasyon sonucu x in yaklaşık değeri : ",fonksyon(x0))
