class ClientValidator():

    def validare_date(self, id_client, nume, cnp):
        err = ""
        if id_client <=0:
            err += "id invalid!\n"
        if len(nume) == 0:
            err += "nume invalid!\n"

        cnp_valid = True
        if len(cnp) == 0:
            err += "cnp invalid!\n"
        else:
            for ch in cnp:
                if ch < '0' or ch > '9':
                    cnp_valid = False
            if not cnp_valid: err += "cnp invalid!\n"

        if len(err) > 0:
            raise Exception(err)


