class CarteFrecventaDto:
    def __init__(self, nume_carte, frecventa):
        self.__nume_carte = nume_carte
        self.__frecventa = frecventa

    def __str__(self):
        return f"Cartea [{self.__nume_carte}] inchiriata de: {self.__frecventa} ori"

    def get_nume_carte(self):
        return self.__nume_carte

    def get_frecventa(self):
        return self.__frecventa



