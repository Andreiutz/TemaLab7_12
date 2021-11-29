class EnrollmentValidator():

    def validare_date(self, id_enroll, id_client, id_carte, repo_client, repo_carte):
        err = ""
        try:
            client = repo_client.get_client(id_client)
        except Exception as ex:
            err += "id client invalid!\n"
        try:
            carte = repo_carte.get_carte(id_carte)
            if carte.get_status_carte() == True:
                err += "cartea este inchiriata deja!\n"
        except Exception as ex:
            err += "id carte invalid!\n"

        if id_enroll <= 0:
            err += "id inchiriere invalid!\n"
        if len(err) != 0:
            raise Exception(err)