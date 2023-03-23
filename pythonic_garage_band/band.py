class Musician:
    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

class Band:
    instances = []

    def __init__(self, name_arg, members_arg):
        self.name = name_arg
        self.members = members_arg
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    def __str__(self):
        return self.name

    @classmethod
    def to_list(cls):
        return cls.instances

class Guitarist(Musician):
    def __init__(self, name_arg):
        self.name = name_arg
        self.instrument = 'guitar'
        self.solo = 'face melting guitar solo'
        print(Guitarist.__name__)

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


class Bassist(Musician):
    def __init__(self, name_arg):
        self.name = name_arg
        self.instrument = 'bass'
        self.solo = 'bom bom buh bom'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):
    def __init__(self, name_arg):
        self.name = name_arg
        self.instrument = 'drums'
        self.solo = 'rattle boom crash'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


if __name__ == '__main__':
    Guitarist("eric")



