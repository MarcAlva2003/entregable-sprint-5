class Client:
    def __init__(self, name, surname, number, dni, direction):
        self.name = name
        self.surname = surname
        self.number = number
        self.dni = dni
        self.direction = direction
    
    def ableToCreateCheckbook():
        return False

    def ableToCreateCreditCard():
        return False

    def ableToBuyDollar():
        return False