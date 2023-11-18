def fonksyon(literasyon):
    xn=2
    xp=4
    for i in range(1,literasyon):
        y1=  (xn ** 3) - (2 * (xn ** 2)) - 5
        y2 = (xp ** 3) - (2 * (xp ** 2)) - 5
        if(y1<0 and y2>0):
            xgecici=(xn+xp)/2
            ygecici=(xgecici ** 3) - (2 * (xgecici ** 2)) - 5
            if(ygecici<0):
                xn=xgecici
            else:
                xp=xgecici
        else:
            print("Literasyon ilerlemesi devam edemez kök aralığından çıkıldı ")
            return ("Kökler ",xn," ve ",xp," arasındadır!!")

    return ("Kökler " , xn , " ve " , xp , " arasındadır!!")





literasyon=int(input("x³-2x²-5 fonksyonunda [2,4] aralığında kaç literasyon yapmak istediğinizi yazınız"))
print(fonksyon(literasyon))
