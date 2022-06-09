def f1():
    print("hi")

def f2():
    print("hello")

def func_caller(fn):
    fn()

def my_func(a,b=3,c=5):
    print(b)

def main():
    my_func(c=1,a=2)

if __name__=="__main__":
    main()
    func_caller(f1)
    func_caller(lambda : print('lambda hi'))