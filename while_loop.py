i = 0
while(i < 10):
    i = i + 1
    print (i)

a = 6
while(a < 18):
    a = a + 1
    print (a)

b = 10
while(b < 20):
    b = b + 2
    print(b)

a = input("Enter your lowest number")
b = input("Enter your highest number")
c = int(a)
d = int(b) + 1
x = range(c, d)
def evens():
    for i in x:
        num = int(i) 
        if num % 2 == 0:
           print(x)
        else:
            pass
evens()

