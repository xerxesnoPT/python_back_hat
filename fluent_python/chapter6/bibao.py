def make_average():
    l = []
    def average(num):
        l.append(num)
        total = sum(l)
        return total / len(l)
    return average

def func():
    a = 1
    n = dict({'a':a})
    def funb():
        print(a)
        n['a'] = 5
        return n['a']
    return funb


if __name__ == '__main__':
    c = func()
    print(c.__closure__)


 