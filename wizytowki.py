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


def create_contacts(rodzaj, liczba):
    bazowe_kontakty = []
    biznesowe_kontakty = []
    if rodzaj == 1:
        for i in range(liczba):
            bazowe_kontakty.append(
                Basecontact(
                    imie=fake.first_name(),
                    nazwisko=fake.last_name(),
                    adres_email=fake.email(),
                    telefon=fake.phone_number(),
                )
            )
        print(bazowe_kontakty)
    elif rodzaj == 2:
        for i in range(liczba):
            biznesowe_kontakty.append(
                Businesscontact(
                    imie=fake.first_name(),
                    nazwisko=fake.last_name(),
                    adres_email=fake.email(),
                    telefon=fake.phone_number(),
                    nazwa_firmy=fake.company(),
                    stanowisko=fake.job(),
                    telefon_sluzbowy=fake.phone_number(),
                )
            )
        print(biznesowe_kontakty)


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
