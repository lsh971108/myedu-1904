def open_writen():
    text_io = open('niubi.text','w+')
    for i in  range(5):
        text_io.write('梁善辉,梁善辉\n')

def open_writen1():
    text_io =open('niubi.text','a+')
    for i in range(5):
        text_io.write('牛逼\n')

def open_read():
    text_io=open('niubi.text','r')
    print(text_io.readline())

def 奇数():
    kaishi=0
    for fanwei in range(1,51):
        # if fanwei % 2 == 1:
        fanwei %2 ==1
        
            kaishi=kaishi+fanwei
        print(kaishi)
if __name__ == '__main__':
    # open_writen()
    # open_writen1()
    # open_read()
    奇数()



