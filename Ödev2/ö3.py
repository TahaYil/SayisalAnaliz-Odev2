def newton(x0):
    x1=x0
    for i in range(1,4):
        x1=x0-((x0**(1/3))/((1/3)*(x0**(-2/3))))
        x0=x1
    return x1




x0=int(input("x üzeri 1/3 fonksyonun newton raphson modeli için x başlangıç değeri girin : "))
print("model sonucu x değeri yaklaşık olarak : ",newton(x0))