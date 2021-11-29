class ClientFrecventaDto:

    def __init__(self, nume, frecventa):
        self.__nume = nume
        self.__frecventa = frecventa

    def __str__(self):
        return f"Clientul [{self.__nume}] a inchiriat {self.__frecventa} carti"

    def get_nume(self):
        return self.__nume

    def get_frecventa(self):
        return self.__frecventa