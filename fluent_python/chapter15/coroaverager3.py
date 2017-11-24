from collections import namedtuple

Result = namedtuple('Result','count average')

def averager():
    count = 0
    total = 0
    averager = None
    while True:
        term = yield
        if term == None:
            break
        count += 1
        total += term
        averager = total/count
    return Result(count, averager)

def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    result = {}
    for key, values in data.items():
        group = grouper(result, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    # print(result)
    report(result)

data = {
    'girls;kg':[50,20,40],
    'girls;m' :[1,2,3]
}

def report(result):
    for key, resu in sorted(result.items()):
        group, unit = key.split(";")
        print(resu.count, group, resu.average, unit)

if __name__ == '__main__':
    main(data)