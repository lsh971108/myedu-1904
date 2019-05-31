def jiujiu():
    for shulie in range(1,10):
        for hanglie in range(1,shulie+1):
            print('%s*%s=%s'%(shulie,hanglie,shulie*hanglie),end='    ')
        print('')




if __name__ == '__main__':
    jiujiu()
