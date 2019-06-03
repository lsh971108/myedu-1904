class fl(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def play(self):
        print(self.name+ '在玩')
    def work(self):
        print(self.name+'在工作')
    def info(self):
        print('这个人名叫%s,今年%s岁,性别：%s'%(self.name,self.age,self.sex))
        self.play()
        # self.work()
        # self.info()

class career(fl):
    def __init__(self,name,age,sex,job):
        self.name=name
        self.age=age
        self.sex=sex
        self.job=job

    def eat(self):
        print(self.name+'在吃东海三太子')
    def wk(self):
        print(self.name+'在发星道炮')

if __name__ == '__main__':
    # girl = fl('小白',5,'女')
    # # girl.play()
    # # girl.work()
    girl.wk()
