# def assert_int():
#     try:
#         assert 1>2
#     #     assert  3==3
#     # except:
#     #     print('110')

def assert_str():
    b = '58'
    d = '99'
    try:
        assert b in d
        assert d not in b
    except:
        print('报警')

if __name__ == '__main__':
    # assert_int()
    assert_str()