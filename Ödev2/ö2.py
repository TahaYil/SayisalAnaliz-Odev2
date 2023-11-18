def fonksyon():
    xn = 1
    xp = 2
    ygecici=2;
    xgecici=1;
    while (ygecici > 0.000001):
        y1 = (xn ** 3) + (4 * (xn ** 2)) - 10
        y2 = (xp ** 3) + (4 * (xp ** 2)) - 10
        if (y1 < 0 and y2 > 0):
            xgecici = (xn + xp) / 2
            ygecici = (xgecici ** 3) + (4 * (xgecici ** 2)) - 10
            if (ygecici < 0):
                xn = xgecici
            else:
                xp = xgecici
            if (ygecici < 0):
                ygecici = -1 * ygecici
        else:
            print("Literasyon ilerlemesi devam edemez kök aralığından çıkıldı ")
            return xgecici

    return xgecici


print("x³+4x²-10 fonksyonunda [1,2] aralığında kökü ")
print("Fonkson kökü 0.000001 hata payı ile : ", fonksyon())
