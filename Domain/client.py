class Client():
    def __init__(self, id, nume, cnp):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp

    def __eq__(self, other):
        return self.__id == other.get_id() and self.__cnp == other.get_cnp() and self.__nume == other.get_nume()

    def __str__(self):
        s = ""
        s += "[ID]: " + str(self.__id) + " | "
        s += "[NUME]: " + self.__nume + " | "
        s += "[CNP]: " + self.__cnp
        return s

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    def set_cnp(self, cnp_nou):
        self.__cnp = cnp_nou
