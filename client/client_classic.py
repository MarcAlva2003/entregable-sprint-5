from .client import Client

class ClientClassic(Client):
    def __init__(self, name, surname, number, dni, direction):
        super().__init__(name, surname, number, dni, direction)

    def ableToCreateCheckbook():
        return False

    def ableToCreateCreditCard():
        return False

    def ableToBuyDollar():
        return False