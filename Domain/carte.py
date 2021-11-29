class Carte():
    def __init__(self, id, titlu, autor, descriere, inchiriata):
        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__descriere = descriere
        self.__inchiriata = inchiriata

    def __eq__(self, other):
        return self.__id == other.get_id() and self.__autor == other.get_autor() and self.__titlu == other.get_titlu() and self.__descriere == other.get_descriere()

    def __str__(self):
        s = ""
        s += "[ID]: " + str(self.__id) + " | "
        s += "[TITLU]: " + self.__titlu + " | "
        s += "[AUTOR]: " + self.__autor + " | "
        s += "[DESC.]: " + self.__descriere + " | "
        s += "[STATUS]: " + str(self.__inchiriata)
        return s

    def get_status_carte(self):
        return self.__inchiriata

    def set_status(self, status):
        self.__inchiriata = status

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_autor(self):
        return self.__autor

    def get_descriere(self):
        return self.__descriere