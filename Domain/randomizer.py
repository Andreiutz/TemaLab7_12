import random

class Random():
    def get_random_id(self):
        return random.randint(0, 100)

    def get_random_cnp(self):
        digits = "0123456789"
        cnp = ""
        for i in range(1, 6):
            position = random.randint(0, 9)
            cnp += digits[position]
        return cnp

    def get_random_nume(self):
        litere = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        length_prenume = random.randint(4, 7)
        length_nume = random.randint(4, 7)
        prenume = ""
        nume = ""
        for i in range(0, length_nume):
            position = random.randint(0, 51)
            nume += litere[position]

        for i in range(0, length_prenume):
            position = random.randint(0, 51)
            prenume += litere[position]

        return nume + " " + prenume