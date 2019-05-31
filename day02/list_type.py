
q = ['是打发',2, '你好',6,7,1,3]
def qa():
    print(q[-3])
    print(q[4:])
    print(q[0:2])
    print(q[-2:])
    print(q[:4])
def dele_1():
    q.pop()
    print(q)
    q.pop(2)
    print(q)
    q.pop(3)
    print(q)
    m=q.pop(1)
    print(q)
    print(m)
def list_jia():
    jia =[12,794564,'15486']
    jia.append('5264654')

    hebing = [777,888,999]
    jia.extend(hebing)
    print(jia)
    jia.append(hebing)
    print(jia)

def gai():
        gaizao = [15846,5465464,5864646,6444785644558,58]
        gaizao[2]= '牛逼'
        print(gaizao)
        gaizao[2:5]='厉害了'
        print(gaizao)
def shunxv():
    pai = [0,1,2,8,4,5,7,9,3,6,9,8]
    pai.sort()
    print(pai)
    pai.sort(reverse=True)
    print(pai)

def qvchong():
    chongfu = [0,1,2,8,4,5,7,9,3,6,9,8]
    # chongfu = set(chongfu)
    # print(chongfu)
    # chongfu = list(set(chongfu))
    # print(chongfu)
    print(len(chongfu))

def zuoye():
    zy = [1,2,3,4,5]
    #访问索引2
    print(zy[1])
    #切片访问索引1到4
    print(zy[0:4])
    #删除索引3
    zy.pop(2)
    print(zy)
    #添加两个元素
    tianjia = [6,7]
    zy.extend(tianjia)
    print(zy)
    #第0位元素改成字符5
    zy[0]='5'
    print(zy)
    #获取索引长度
    print(len(zy))
if __name__ == '__main__':

    dele_1()
    list_jia()
    gai()
    shunxv()
    qvchong()
    zuoye()