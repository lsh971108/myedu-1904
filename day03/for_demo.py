def for_demo():
    for dome in range(6,10):
        print('3.1415926')
        print(dome)

def for_demo1():
    for dome in range(6,10,1):
        print(dome)

def for_demo1():
    for dome in range(100,10,-10):
        print(dome)

def for_list():
    x =[1,2,3,4,5,6,7,8,9]
    # for p in x:
    #     print(p)

    for p in range(len(x)):
        print(x[p])

def for_for():
    for i in range(3):
        print('梁善辉')
        for j in range(3):
            print('牛逼',end=',')
        print('')
        print('\n')
def break_continue():
    for i in range(6):
        print(i)
        if i ==3:
            break

    for  i in range(6):
        if i==3:
            continue
        print(i)
if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    # for_list()
    # for_for()
    break_continue()