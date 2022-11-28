class Hello_World:
    hello = 'Hello'
    _hello = '_Hello' #Захищений атрибут
    __hello = '__Hello' #Приватний атрибут
    def __init__(self):
        self.word = 'Word'
        self._word = '_Word'
        self.__word = '__Word'
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.word)
        print(self._word)
        print(self.__word)


class Hi(Hello_World):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.word)
        print(self._word)
        print(self.__word)


hello = Hello_World()
hello.printer()
hi = Hi()
hi.printer()