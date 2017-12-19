import asyncio

class Ticker():
    def __init__(self,delay,end):
        self.delay = delay
        self.i = 0
        self.end = end

    # def __aiter__(self):
    #     return self
    #
    # async def __anext__(self):
    #     i = self.i
    #     if i >= self.end:
    #         raise StopAsyncIteration
    #     self.i += 1
    #     if i:
    #         await asyncio.sleep(self.delay)
    #     return i

    async def producer(self):
        i = self.i
        if i >= self.end:
            raise StopAsyncIteration
        self.i += 1
        if i:
            await asyncio.sleep(self.delay)
        return i

async def main():
    i = await Ticker(1,5).producer()
    print(i)

def qsort(l):
    if not l:
        return []
    else:
        pivit = l[0]
        less = [a for a in l if a < pivit]
        more = [b for b in l if b > pivit]
        return qsort(less) + [pivit] + qsort(more)

def qsort_one(l):
    less = []
    pivotlist = []
    more = []
    pivit = l[0]
    if len(l) <= 1:
        return l
    for i in l:
        if i < pivit:
            less.append(i)
        if i > pivit:
            more.append(i)
        else:
            pivotlist.append(i)

    less = qsort_one(less)
    more = qsort_one(more)
    return less + pivotlist + more


def hanoi(n, a, b, c):
    if n == 1:
        print('%s -> %s' %(a, c))
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)




if __name__ == '__main__':
    hanoi(3,'a','b','c')
    names = ['Marry', 'Isla', 'Sam']
