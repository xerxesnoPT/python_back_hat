class LookingGlass:
    def __init__(self):
        self.origin_std_out = None
    def __enter__(self):
        import sys
        self.origin_std_out = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return self

    def reverse_write(self, text):
        self.origin_std_out(text[::-1])

    def __exit__(self, exc_type, exc_val, traceback):
        import sys
        sys.stdout.write = self.origin_std_out
        if exc_type is ZeroDivisionError:
            print('ggg')
            return True

if __name__ == '__main__':
    with LookingGlass() as look:
        print(look)
        raise TypeError
    print('oooott')
