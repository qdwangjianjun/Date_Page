class Foo:
    # x = 'Foo attr'

    # def __init__(self):
    #     self.x = 'father instance attr'
    pass

class Foo_sub(Foo):
    # pass
    x = 'Foo_sub attr'

    def __init__(self):
        self.x = 'Foo_sub instance attr'

    def __getattr__(self, item):
        print('last __getattr__ method')

    # def __getattribute__(self,item):
    #     print('highest property method')


f = Foo_sub()
print(f.x)
# print(f.y)

