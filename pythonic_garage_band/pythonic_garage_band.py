class Band:
    def __init__(self, name):
        self.name=name

    # def __str__(self):
    #     pass
    #
    # def __repr__(self):
    #     pass

    name = 'test'
    # members, inherits from Musician super class

    def play_solo(self):
        pass



if __name__ == '__main__':
    test = Band("Eric")
    print(test.name)


