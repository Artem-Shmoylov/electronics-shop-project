from src.item import Item


class Mixing:
    language = 'EN'

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def change_lang(self):

        if Mixing.language == 'EN':
            self.language = 'RU'
            Mixing.language = 'RU'
        elif Mixing.language == 'RU':
            self.language = 'EN'
            Mixing.language = 'EN'
        return self


class KeyBoard(Mixing, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value != "RU" and value != "EN":
            raise AttributeError(f"property 'language' of 'KeyBoard' object has no setter")
        self.__language = value
