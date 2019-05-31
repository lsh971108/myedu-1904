zidian = {'password': "123456",'username': "admin"}
def cha():
    print(zidian['password'])

def gaiv():
    zidian['password']='ahs51j'
    print(zidian)

def shanchu():
    zidian.pop('username')
    print(zidian)

def zhengjia():
    zidian['bbq']= 5555555
    print(zidian)
    cidian = {'list':58645846464684864,'tuple':'4857458,446464' }
    zidian.update(cidian)
    print(zidian)
    shengdian = {'password': '566466', 'class': '646464'}
    shenshengdian = dict(cidian, **shengdian)
    print(shenshengdian)


if __name__ == '__main__':
    cha()
    gaiv()
    shanchu()
    zhengjia()
