def fun1():
    try:
        print('try code')
    except:
        print('exception handling code')
    else:
        print('no exception code raised')
        x = int('a')
        
def fun2():
    try:
        print('try code')
        print('exception handling code')
        x = int('a')
    except:
        print('no exception code raised')
        
print('calling fun2')
fun2()
print('--------------')
print('calling fun1')
fun1()