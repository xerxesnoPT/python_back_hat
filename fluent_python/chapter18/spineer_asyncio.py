import asyncio,sys
import itertools
import time


# @asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' '+ msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        write(' ' * len(status) + '\x08' * len(status))

# @asyncio.coroutine
async def slow_function():
    await asyncio.sleep(3)
    return 42

# @asyncio.coroutine
async def supervisor():
    spinner = asyncio.Task(spin('thinking!'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    print(loop.get_task_factory())
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)

@asyncio.coroutine
def waitprint(time,value):
    yield from asyncio.sleep(time)


if __name__ == '__main__':
    main()
