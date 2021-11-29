class Enrollment():

    def __init__(self, id_enroll, id_client, id_carte, status):
        self.__id_enroll = id_enroll
        self.__id_client = id_client
        self.__id_carte = id_carte
        self.__status = status

    def __str__(self):
        s = ""
        s += "[ID_ENROLL]: " + str(self.__id_enroll) + " | "
        s += "[ID_CLIENT]: " + str(self.__id_client) + " | "
        s += "[ID_CARTE]: " + str(self.__id_carte)
        return s

    def get_id(self):
        return self.__id_enroll

    def get_id_client(self):
        return self.__id_client

    def get_id_carte(self):
        return self.__id_carte

    def get_status(self):
        return self.__status

    def cancel_enrollment(self):
        self.__status = 0