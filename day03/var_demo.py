avar= '梁善辉'
def name ():
    print(avar)
def you_name():
    global avar
    avar='圣贤者'
    print(avar)






if __name__ == '__main__':
    name()
    you_name()