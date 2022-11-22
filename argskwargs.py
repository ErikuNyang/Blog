def hello(*args, **kwargs):
    print('hello', end=' ')
    for arg in args:
        print(arg, end= ' ')
    print()
    for kwarg in kwargs.items():
        print(kwarg)

if __name__=='__main__':
    hello('Tech', 'kildong', 'no?')
    hello(name="cho", age="36", born="seoul")
