class Basecontact:
    def __init__(self, imie, nazwisko, telefon, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.adres_email = adres_email
        self._label_length = 0

    def contact(self):
        print(
            f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}."
        )

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email}"

    def label_length(self):
        self._label_length = f"{len(self.imie)} {len(self.nazwisko)}"
        return self._label_length


class Businesscontact(Basecontact):
    def __init__(self, stanowisko, nazwa_firmy, telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(
            f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}."
        )

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email} {self.telefon_sluzbowy} {self.stanowisko} {self.nazwa_firmy} "


from faker import Faker

fake = Faker("pl_PL")


def generate_elements(number, elements_type):
    lst = []
    for _ in range(number):
        arguments = {
            'imie': fake.first_name(),
            'nazwisko': fake.last_name(),
            'adres_email': fake.email(),
            'telefon': fake.phone_number(),
        }
        if elements_type == Businesscontact:
            arguments.update({
                'nazwa_firmy': fake.company(),
                'stanowisko': fake.job(),
                'telefon_sluzbowy': fake.phone_number(),
            })
        lst.append(elements_type(**arguments))
    return lst


def create_contacts(rodzaj, liczba):
    kontakty = []
    if rodzaj == 1:
        kontakty = generate_elements(liczba, Basecontact)
    elif rodzaj == 2:
        kontakty = generate_elements(liczba, Businesscontact)
    print(kontakty)


if __name__ == "__main__":
    create_contacts(2, 11)

    osoba01 = Basecontact(
        imie="Lukasz",
        nazwisko="Pytlewski",
        telefon=12345678,
        adres_email="Lukasz.Pytlewski@costam.com",
    )

    osoba02 = Businesscontact(
        imie="Lukasz",
        nazwisko="Pytlewski",
        telefon=12345678,
        adres_email="Lukasz.Pytlewski@costam.com",
        stanowisko="bylejakie",
        nazwa_firmy="firma",
        telefon_sluzbowy=32134566,
    )

    osoba01.contact()

    osoba02.contact()

    print(osoba01.label_length())
    print(osoba02.label_length())
