from datetime import datetime

def outer(func):
    def inner(*args,**kwargs):
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        print("时长",end - start)
    return inner

@outer
def f1():
    print("f1")

@outer
def f2():
    print("f2")

# 装饰器有参数
def check_p(permission):
    def outer(func):
        def inner(qx,*args,**kwargs):
            # 校验权限
            if permission & qx == permission:
                # 通过校验 才可以调用权限
                return func(qx,*args,**kwargs)
            else:
                print("没有权限")
        return inner
    return outer

@check_p(2)
def f3(n):
    print()
    print("kkkk")
    return "hehe"

if __name__ == '__main__':
    # start = datetime.now()
    # f1()
    # f2()
    res = f3(7)
    print("res",res)
    # end = datetime.now()
    # print(end - start)

# 需求  计算f1函数