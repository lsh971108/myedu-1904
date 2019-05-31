zidian ={'k':'v','a':'45546'}
#通过key访问一个值
def fangwen():
    print(zidian['k'])
#删除一个键值对
    zidian.pop('a')
    print(zidian)
#添加一个键值对
    zidian['guan']='kan'
    print(zidian)
#更改任意一个值
    zidian['k']='vvv'
    print(zidian)
#再新建一个字典
def xinjian():
    xinhuazidain={'xin':'hua','zi':'dian'}
    print(xinhuazidain)
#将两个合并
    zidian.update(xinhuazidain)
    print(zidian)
if __name__ == '__main__':
    fangwen()
    xinjian()



