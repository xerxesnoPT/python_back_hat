from inspect import signature
import collections
def verfy_type(func):
    msg = """Expected type {} for argument {}, but

            got type {} with value {}"
            """
    sig = signature(func)
    parameters = sig.parameters
    arg_keys = tuple(parameters.keys())

    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple("CheckItem",('anno','arg_name','value'))
        check_list = []
        for i, value in enumerate(args):
            arg_name = arg_keys[i]
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno,arg_name,value))
        
        for k, value in kwargs.items():
            arg_name = k
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno,arg_name,value))

        for check in check_list:
            if not isinstance(check.value, check.anno):
                newmsg = msg.format(check.anno, check.arg_name,
                        type(check.value), check.value)
                raise TypeError(newmsg)

        return func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    @verfy_type
    def func(name:str, age:int, c:float =3.2) ->tuple:
        return a, b ,c

    print(func(2,1,2))



