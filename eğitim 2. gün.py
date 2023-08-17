"""import random
liste= ["SİYAH","BEYAZ","MAVİ","YEŞİL","GRİ","TURUNCU"] choice fonks. listeden rastgele bir şey seçip yazdırmasına sebep olur
print(random.choice(liste))"""
"""import random"""

#random.shuffle() fonksiyonu, bir veri dizisi veya liste gibi bir koleksiyonun öğelerini karıştırmak için kullanılır. Bu fonksiyon koleksiyonun öğelerini yerinde değiştirir ve karıştırdıktan sonra herhangi bir değer döndürmez (None döndürür). Bu nedenle, random.shuffle() fonksiyonunu çağırdıktan sonra döndürdüğü değer None olacaktır.
"""import random
liste= ["SİYAH","BEYAZ","MAVİ","YEŞİL","GRİ","TURUNCU"]
print(random.shuffle(liste))"""
#random 3 tane renk seçtirdim
"""import random
liste= ["SİYAH","BEYAZ","MAVİ","YEŞİL","GRİ","TURUNCU"]
print(random.sample(liste,3))"""
"""import random
zarlar={1:0,2:0,3:0,4:0,5:0,6:0}
for i in range(100):
    zar=random.randint(1,6)
    zarlar[zar]+=1

for zar in zarlar:
    print(f"{zar}gelme olasılığı:{zarlar[zar]/100}")"""
#time modülü

"""import time
zaman=time.ctime(10000000)
print(zaman)"""

"""import time
zaman=time.localtime(100)
print(zaman)"""
"""import time
zaman2=time.localtime()
zaman=time.asctime(zaman2)
print(zaman)"""
"""import time
zaman=time.strftime("%d:%m:%Y")
print(zaman)"""
"""import time
zaman=time.strftime("%d:%m:%Y:%S")
print(zaman)"""
#kendi geliştirdiğim alıştırmam
"""from turtle import *
import time
import random


def create_star(x, y):
    pensize(2)
    pencolor(random.choice(["red", "green", "blue", "purple", "yellow", "orange"]))
    goto(x, y)

    for _ in range(10):
        forward(50)
        right(154)


def move_star(star):
    star.setx(star.xcor() + random.uniform(-5, 5))
    star.sety(star.ycor() + random.uniform(-5, 5))


def main():
    screensize(800, 600)
    hideturtle()
    speed(0)

    for i in range(10, 0, -1):
        clear()
        goto(0, 0)
        write(str(i), align="center", font=("Arial", 36, "normal"))
        time.sleep(1)

    clear()

    stars = []

    for _ in range(10):
        x_star = random.randint(-300, 300)
        y_star = random.randint(-200, 200)
        star = Turtle()
        star.speed(0)
        star.penup()
        star.shape("turtle")
        star.color(random.choice(["red", "green", "blue", "purple", "yellow", "orange"]))
        star.goto(x_star, y_star)
        stars.append(star)

    for _ in range(50):
        for star in stars:
            move_star(star)

        time.sleep(0.1)
        clear()

if __name__ == "__main__":
    main()
    done()"""
#dosya konumu bulmak için
"""import os
print(os.getcwd())"""
#dosya yolunu döndürmek
"""import os
print(os.getcwd())
os.chdir("C:\\Users\\pc\\PycharmProjects\\pythonProject8")
print(os.getcwd())"""
#dosyayı ve altdizinleri listeledi
"""import os
print(os.getcwd())
os.chdir("C:\\Users\\pc\\PycharmProjects\\pythonProject8")
print(os.listdir())"""
#---------------------------------------------------
"""import os
print(os.getcwd())
os.chdir("C:\\Users\\pc\\PycharmProjects\\pythonProject8")
for dosya in os.listdir():
    print(dosya)"""
#yeni klasör oluşturdu
"""import os
print(os.getcwd())
os.chdir("C:\\Users\\pc\\PycharmProjects\\pythonProject8")
os.mkdir("DENEMEKkLASÖRÜ")"""
#belirtilen dosya içindeki hataları ayıklamak
"""import os
print(os.getcwd())
os.chdir("C:\\Users\\pc\\PycharmProjects\\pythonProject8")
os.makedirs("deneme1/deneme2/deneme")"""

"""import turtle
import time
import random

# Ekran oluşturma
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Yıldız Haritası")

def geri_sayim():
    for count in range(5, -1, -1):
        turtle.clear()
        if count > 0:
            turtle.write(str(count), align="center", font=("Arial", 100, "normal"))
        else:
            turtle.write("Başla!", align="center", font=("Arial", 100, "normal"))
        turtle.update()
        time.sleep(1)

def yildiz_haritasi():
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.clear()
    turtle.update()

    stars = []

    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        stars.append((x, y))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(4, "white")
        turtle.hideturtle()
        turtle.update()

    return stars

def tikla(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(2, "red")
    turtle.update()

    tablo_turtle.clear()
    tablo_turtle.write(f"Tıklanan yıldız koordinatı: ({x}, {y})", align="left", font=("Arial", 12, "normal"))

def temizle():
    turtle.clear()

geri_sayim()

yildiz_koordinatlari = yildiz_haritasi()

turtle.onscreenclick(tikla)

screen.onkeypress(temizle, "c")
screen.listen()

tablo_turtle = turtle.Turtle()
tablo_turtle.speed(0)
tablo_turtle.color("white")
tablo_turtle.penup()
tablo_turtle.hideturtle()
tablo_turtle.goto(-350, 350)

turtle.mainloop()"""

"""numbers=[1,2,3,4,5,6,7,8,9]
list2=[]
for number in numbers:
    list2.append(number)
print(list2)

list3=[number for number in numbers]"""
"""list2 = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    list2.append(number * number)
print(list2)

list3 = [number * number for number in numbers]

list2 = []
for number in numbers:
    if number % 2 == 0:
        list2.append(number)
print(list2)"""
"""smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)"""
"""counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))"""
"""d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)"""
"""lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)"""

"""import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)"""

"""while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()"""

"""import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())"""
"""class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()"""

"""class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()"""

"""def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = "32"
    second_line = "698"
    dash_line = "3801"
    answer_line = "-2"

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        max_width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(max_width) + '    '
        second_line += operator + num2.rjust(max_width - 1) + '    '
        dash_line += '-' * max_width + '    '

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line += result.rjust(max_width) + '    '

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()
    if show_answers:
        arranged_problems += '\n' + answer_line.rstrip()

    return arranged_problems

result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)
print(result)"""
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        max_width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(max_width) + '    '
        second_line += operator + ' ' + num2.rjust(max_width - 2) + '    '
        dash_line += '-' * max_width + '    '

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line += ' ' + result.rjust(max_width) + '    '

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()
    if show_answers:
        arranged_problems += '\n' + answer_line.rstrip()

    return arranged_problems

result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)
print(result)
