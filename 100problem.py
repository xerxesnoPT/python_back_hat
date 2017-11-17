def one():
    l = [1, 2, 3, 4]
    for a in l:
        for b in l:
            for c in l:
                if a!=b and b!=c and c!=a:
                    print(a,b,c)

def two():
    i = [100, 60, 40, 20, 10, 0]
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    total = int(input('输入利润'))
    money = 0
    for index, x in enumerate(i):
        if total > x:
            money += (total-x)*rate[index]
            total = x
    print('总奖金 %s' %money)

def three():








if __name__ == '__main__':
    # one()
    # two()
    three()




