class CarteValidator():

    def validare_date(self,id_carte, titlu, autor, descriere):
        err = ""
        if id_carte <= 0:
            err += "id invalid!\n"

        if len(titlu) == 0:
            err += "titlu invalid!\n"

        if len(autor) == 0:
            err += "autor invalid!\n"

        if len(descriere) == 0:
            err += "descriere invalida!\n"

        if len(err) != 0:
            raise Exception(err)