def yunsuan (a):
    a+=9
    print(a)
    a -=9
    print(a)
    a  /=9
    print(a)
    a *=9
    print(a)
    a %=7
    print(a)

def bijiao(a,b,c):
    print(b>c)
    print(a==c)
    print(c<=a)
    print(a !=b)
    print(a /c)

if __name__ == '__main__':
    yunsuan(81)
    bijiao(7,8,9)