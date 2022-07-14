from .client import Client

class ClientBlack(Client):
    def __init__(self, name, surname, number, dni, direction):
        super().__init__(name, surname, number, dni, direction)

    def ableToCreateCheckbook():
        return True

    def ableToCreateCreditCard():
        return True

    def ableToBuyDollar():
        return True