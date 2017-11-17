class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.colunm_type = column_type

    def __str__(self):
        return '<%s:%s>' %(self.__class__.__name__, self.name)


class FieldChar(Field):
    def __init__(self, name):
        super(FieldChar, self).__init__(name, 'varchar(100)')


class FieldInt(Field):
    def __init__(self, name):
        super(FieldInt, self).__init__(name, 'int')


class ModelMetaclass(type):
    def __new__(cls, name, base, attrs):
        if name == 'Model':
            return type.__new__(cls, name, base, attrs)
        print('find model %s' %name)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print(v.name,v.colunm_type)
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, base, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError
    # #
    # def __setattr__(self, key, value):
    #     self[key] = value

    def save(self):
        field = []
        params = []
        args = []
        for k, v in self.__mapping__.items():
            print(type(k))
            field.append(k)
            params.append("?")
            args.append(getattr(self, k, None))
        sql_temp = 'insert into %s (%s) VALUES (%s)' % (self.__table__, ','.join(field), ','.join(params))
        print(sql_temp)
        print((args))



class User(Model):
    name = FieldChar('aa')
    age = FieldInt('bb')
    phone = FieldInt('cc')
    email = FieldChar('ss')
    pp = 'aaa'






if __name__ == '__main__':
    user = User(name='tom', age=21, phone=1322, email="class")
    user.save()
    print(user.__mapping__)
