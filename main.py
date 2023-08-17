"""print("hello world")""" #ekrana yazdırma fonksiyonu strign ifadeler tırnak içerisine yazılır
"""print('merhaba')""" #metinsel ifadenin bittiğini düşündüğü anlar olacaktır.
"""print("merhaba\n")"""
"""mesaj="merhaba"
print(mesaj)"""
#biri bitişik diğeri boşluklu yazım
"""mesaj="merhaba"
mesaj2="dünya"
print(mesaj+mesaj2)"""

"""mesaj="merhaba"
mesaj2="dünya"
print(mesaj+" "+mesaj2)"""
#mesaj değişkeninden 2. harfi yazdırdı
"""mesaj="merhaba"
mesaj2="dünya"
print(mesaj[1])"""
#m hariç geri kalan harfleri yazdı 1ve7 aralığı
"""mesaj="merhaba"
mesaj2="dünya"
print(mesaj[1])"""
#ikişer ikişer yazdırdı
"""mesaj="merhaba"
print(mesaj[::2])"""
#upper büyük harfe soktu
"""mesaj="selam"
print(mesaj.upper())"""
#mesajı küçük harflerle yazdırdı
"""mesaj="selam"
print(mesaj.upper())
print(mesaj)"""
#biri tamamen büyük yazarken diğeri tam tersine küçük yazıyor
"""mesaj="selam"
print(mesaj.upper())
mesaj=mesaj.lower()
print(mesaj)"""
#capitalizew baş harfini büyütttü
"""mesaj="selam"
print(mesaj.upper())
mesaj=mesaj.lower()
print(mesaj)
print(mesaj.capitalize())
print(mesaj)"""
#bir metnin herangi bir ifadeyle başlayıo-p başlamadığını kontrol ediyor
"""mesaj="selam"
print(mesaj.upper())
mesaj=mesaj.lower()
print(mesaj)
print(mesaj.capitalize())
print(mesaj)
print(mesaj.startswith("me"))"""
#son harfinin hangi harfle bitip bitmediğin i tespit ettiriyorsun
"""mesaj="selam"
print(mesaj.endswith("a"))"""
#len methodu mesajın kaç karakterden oluştuğunu gösterir
"""mesaj="selam"
print(len(mesaj))"""
#cümlenin içinde verilen her şeyi yazdırdı
"""isim="Ali"
Yas="20"
print("{}, {} yaşındadır".format(isim,Yas))"""
"""isim="ahmet"
mesaj="merhaba"
print("{}:{} dedi.".format(isim,mesaj))"""
#integer float type tam sayılar ve ondalık sayılar
"""sayi1=5
sayi2=3,8
print(type(sayi1))""" #bir değişkenin hangi tipte bir veri olduğunun type () fonksiyonu ile öğrenmemiz mümkündür.

"""sayi1=5**100
sayi2=22/7
print(sayi2)"""
#round çıkan sonucu tam sayıya yuvarladı
"""sayii=22/7
print(round(sayii))"""
"""sayi=3.32422
print(round(sayi))"""
#girdiğim ikinci parametre sayesinde kaç basamak yuvarlayacağına karar verdi
"""sayi=3.6768675
print(round(sayi,3))"""
#işlem önceliği normaldeki işlem önceliğiyle aynıdır
"""print(3*5+4)"""
"""print(3<=4)""" #küçüklğk eşitlik denklik kontrolü
"""print(5>3)""" #büyüklük eşitlik denklik kontrolü
"""print(3==3)"""#eşitlik,denklik kontrolü
"""print(3<1)""" #küçüklük kontrolü
"""print(4>10)"""#büyüklük kontrolü

"""a=1
b=a
a=5
print(b)""" #a=1 dendiği zaman bellekte a kutusu içine koyuyoruz ben bunu ne kadar değiştirsem de pek değişen bir durum olmaz

"""say1="100"
print(type(say1))"""
#string integer çevirme
"""say1="100"
say2=100
print(type(say2))"""
#ikisi eşit değil çünkü 1. metin olarak geçiyor false aldık
"""say1="100"
say2=100
print(say1==say2)"""
#sayı 2 ile sayı 3 e eşit,sayı3 1in integera çevirilmiş hali
"""say1="100"
say2=100
say3=int(say1)
print(say1==say2)"""
#listeler
"""renk=["mor","beyaz","pembe"] #liste halinde yazılan renkler ekrana yazıldı
print(renk)"""
"""renk=["mor","beyaz","pembe"]
print(renk[2])""" #filtreleme ile 2. rengi yazdırdı
#ikinci rengii yazdırdı
"""renk=["mor","beyaz","pembe"]
print(renk[1:2])"""
#beyazı atlayıp başta ve sondakini yazdırdı
"""renk=["mor","beyaz","pembe"]
print(renk[::2])"""
#append,insert,remove,pop,reverse,sort and sorted
#append metodu listeye yeni rengi ekledi
"""renk=["siyah","beyaz","sarı","mavi","yeşil"]
renk.append("gri")
print(renk)"""
#gri en başa yazıldı
"""renk=["siyah","beyaz","sarı","mavi","yeşil"]
renk.insert(0,"gri")
print(renk)"""
#sarı renk çıkarıldı
"""renk=["siyah","beyaz","sarı","mavi","yeşil"]
renk.remove("sarı")
print(renk)"""
#tüm renkleri birleştirdik
"""renk1=["mor","beyaz","siyah"]
renk2=["mavi","yeşil","sarı"]
renk1.append(renk2)
print(renk1)"""
"""renk1=["mor","beyaz","siyah"]
renk2=["mavi","yeşil","sarı"]
renk1.extend(renk2)
print(renk1)"""
"""renk1=["mor","beyaz","siyah"]
renk1.pop()
print(renk1)"""
"""renk1=["mor","beyaz","siyah"]
silinen=renk1.pop()
print(renk1)
print(silinen)"""
#tersten ve düzden liste yazım
"""renk1=["mor","beyaz","siyah"]
print(renk1)
renk1.reverse()
print(renk1)"""

"""renk1=["mor","beyaz","siyah"]
print(renk1)
renk1.sort(reverse= True)
print(renk1)"""
#tüm liste boşluklu şekilde yazıldı
"""renk1=["mor","beyaz","siyah"]
list1=sorted(renk1)
print(renk1)"""
#2 kez yazıldı
"""renk1=["mor","beyaz","siyah"]
list1=sorted(renk1)
print(renk1)
print(list1)"""
#alfabetik olaarak renkler listesinde bulunan en küçük elemanı döndürdü
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
sayilar=[1,2,39,4,3,7,8]
print(min(renk))"""#bu listeyi min değeri içine yazarsak en küçük sayıyı çıkaracak,max yazarsak renklerde alfabetik büyüklük ve sayılarda alfabetik büyüklük listesi yapar

#int. ile str toplanmaz,sadece sayıları sum ile toplayabiliriz
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
sayilar=[1,2,39,4,3,7,8]
print(sum(sayilar))"""
#for döngüsü ile tek tek renkleri saydırıyor
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
for renk in renk:
    print(renk)"""
#renk kısmını i ile değiştirdik sonuç aynı
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
for i in renk:
    print(renk)"""
#liste numaralandırma sıfırdan başladı
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
print(list(enumerate(renk)))"""
#3ten itibaren listeye aldı
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
print(list(enumerate(renk,start=3)))"""

#siyah renghin listede olup olmadığını sorguladı
"""renk=["MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI"]
print("siyah" in renk)"""
#birleştirerek yazdı
"""renk
stringrenkler="".join(renk)
print(stringrenkler)"""

#demetler
"""demet=("MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI")
print(demet)"""
#demete herhangi bir eleman ekleyip silemeyiz,bunu işlemsel olarak desteklemez
"""demet=("MAVİ","BEYAZ","YEŞİL","MOR","KIRMIZI")"""

#kümeler
"""kume={"sarı","mavi","yeşil","mor"}
for renk in kume:
    print(renk)""" #küme içindeki her rengi teker teker yazdırdı
#elemean ekle ve sil
"""kume={"sarı","mavi","yeşil","mor"}
print(kume)
kume.add("pembe")
print(kume)""" #önce ilk kümeyi yazdırdı sonradan pembeyi ekledi

"""kume={"sarı","mavi","yeşil","mor"}
print(kume)
kume.remove("sarı")#sarı elemanı silindi
print(kume)"""
"""kume={"sarı","mavi","yeşil","mor"}
print(kume)
kume.discard("gri")#kümeyi silmedi hata da vermedi sadece var olan kümeyi yazdırdı
print(kume)"""
#küme kesişim ve birleşim
"""kume={"sarı","mavi","yeşil","mor"}
kume1={"beyaz","mavi","lila","sarı"}
print(kume.intersection(kume1))""" #iki kümenin ortak elemanları
#iki kümeyi bağladı
"""kume={"sarı","mavi","yeşil","mor"}
kume1={"beyaz","mavi","lila","sarı"}
print(kume.union(kume1))"""
"""kume={"sarı","mavi","yeşil","mor"}
kume1={"beyaz","mavi","lila","sarı"}
print(kume.difference(kume1))"""#iki küme fark
#if else elif
"""if True:
    print("kosul doğru")
    print("halen if bloğunun içindeyiz")"""
#a bye eşit olmadığı için güle güle yazıldı
"""a=5
b=7
if a==b:
    print("merhaba")
else:
    print("güle güle")"""
#demetin içindeki elemanları yazdırır
"""demet=(1,2,3,4)
for i in demet:
    print(demet)"""
"""demet=(1,2,3,4)
for i in demet:
    print(i)"""#alt alta yazım sağlandı

"""for i in range (0,10):
    print(i)"""#1 den 9 a kadar yazdırdı
#ilk sınır ve son sınır dahil değil,3 değerli yaparsan son değer kaçar kaçar yazdıracağını ifade eder
#1den 9 a kadar olan tüm sayıların 2 ile çarpımı
"""sonuc=1
for i in range (0,10) 
    sonuc *=2
print(sonuc)"""
#harf ve rakamları birbirine uyarladı
"""list1=["a","b","c"]
list2=["1","2","3"]
for harf in list1:
    for rakam in list2:
        print(harf,rakam)"""
#100e kadar 3 er saydırmak
"""list1=range(100)
for i in list1:
    if i % 3!=0:
        continue
    print(i)"""
#2den itibaren teker teker arttırdı ve 10a geldiğinde x=10 yazdırdı
"""x=2
while x<10:
    print(x)
    x+=1
    print("x=",x)"""
"""x=2
y=3
while x * y < 1000:
    print(x,y)
    x+=2
    y+=2"""
#ilk 10000 asal sayının kaç tanesi 3 ile başlar ve biter
"""prime_list=list()
prime_list.append(2)
sayi=3
while True:
    prime= True
    for i in range(2,sayi):
        if sayi %i==0:
            prime=False
            break
    if prime:
        prime_list.append(sayi)
        if len(prime_list)==10:
            break
    sayi +=1
print(prime_list)"""

#3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir
"""def rakam_kupleri_toplami(sayi):
    rakamlar = [int(rakam) for rakam in str(sayi)]
    return sum(rakam ** 3 for rakam in rakamlar)
esit_sayilar = []
for sayi in range(100, 1000):
    if rakam_kupleri_toplami(sayi) == sayi:
        esit_sayilar.append(sayi)
print("Rakamlarının küplerinin toplamına eşit olan 3 basamaklı sayılar:", esit_sayilar)"""

#fibonacci sayı dizisi ilk iki terimi  bir olan ve sonrak, her terimi kendisinden önceki 2 terimin toplamı olan bir sayı dizisidir. ilk 100 fibonacci sayısını ekrana yazdırınız
"""def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_fib)
    return fib_series
n = 100
fibonacci_series = fibonacci(n)
for i, fib in enumerate(fibonacci_series):
    print(f"Fibonacci({i+1}): {fib}")"""
#fonksiyonlar
"""def bilgi_ver():
    print("işlem  başarılı.")
    print("bloğun içerisi")
bilgi_ver()"""

"""def selamla(isim):
    print("merhaba" +isim)
selamla("ali")"""
"""def topla(x,y):
    print(f"x+y={x+y}")
topla(3,6)"""
"""def carp(x,y):
    print(f"x*y={x*y}")
carp(3,6)"""
"""def ortalama(x,y):
    print(f"x+y ortalama={(x*y)/2}")
ortalama(3,6)"""
"""def ortalama(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama_deger = toplam / adet
    return ortalama_deger

liste = [4, 3, 4, 5, 6, 7, 8, 8, 7]
ortalama_deger = ortalama(liste)
print("Ortalama:", ortalama_deger)"""
"""def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    return metin"""
"""metin = "aSDRFKsaAQDadk"
buyuk_harfli_metin = buyuk_harfe_cevir(metin)
print(buyuk_harfli_metin)"""
"""def selamla(mesaj,isim):
    print(f"{mesaj} {isim}.")
selamla("merhaba", "ahmet")"""
"""def indirim_yap(fiyat,yuzde):
    indirim_miktari=fiyat*(yuzde/100)
    indirimli_fiyat=fiyat-indirim_miktari
    print(f"indirimli tutar:{indirimli_fiyat}")
indirim_yap(60,90)"""
#"os" modülünü her projede her an kullanmanız gerekmez.
# Ancak, işletim sistemi işlemleri gerçekleştirmeniz gereken durumlarda bu modül oldukça faydalıdır.
# Özellikle dosya yönetimi, veri işleme, sistem konfigürasyonu gibi görevlerde sıkça kullanılır.
# Eğer projenizde bu tür işlemler yapmanız gerekiyorsa, "os" modülünü öğrenmek ve kullanmak size büyük kolaylık sağlayabilir.
