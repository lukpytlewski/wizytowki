class Wizytowka:
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.adres_email = adres_email

    def kontakt(self):
        print(f"{self.imie} {self.nazwisko}, {self.adres_email}")

    def contact(self):
        print(
            f"Kontaktuję się z", self.imie, self.nazwisko + ",", self.adres_email + "."
        )

    def imienazwisko_length(self):
        return self._imienazwisko_length

    def imienazwisko_length(self):
        self._imienazwisko_length = print(f"{len(self.imie)} {len(self.nazwisko)}")


class Basecontact(Wizytowka):
    def __init__(self, imie, nazwisko, nazwa_firmy, stanowisko, adres_email, telefon):
        super().__init__(imie, nazwisko, nazwa_firmy, stanowisko, adres_email)
        self.telefon = telefon

    def contact(self):
        print(
            f"Wybieram numer",
            self.telefon + "i dzwonię do" + self.imie,
            self.nazwisko + ".",
        )

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email}"

    def label_length(self):
        return self._label_length

    def label_length(self):
        self._label_length = print(f"{len(self.imie)} {len(self.nazwisko)}")


class Businesscontact(Basecontact):
    def __init__(self, telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(
            f"Wybieram numer",
            self.telefon_sluzbowy + "i dzwonię do" + self.imie,
            self.nazwisko + ".",
        )

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} {self.adres_email} {self.telefon_sluzbowy} {self.stanowisko} {self.nazwa_firmy} "

    def label_length(self):
        return self._label_length

    def label_length(self):
        self._label_length = print(f"{len(self.imie)} {len(self.nazwisko)}")


from faker import Faker

fake = Faker("pl_PL")


def create_contacts(rodzaj, liczba):
    Bazowe_kontakty = []
    Biznesowe_kontakty = []
    if rodzaj == 1:
        for i in range(liczba):
            Bazowe_kontakty.append(
                Basecontact(
                    imie=fake.first_name(),
                    nazwisko=fake.last_name(),
                    adres_email=fake.email(),
                    telefon=fake.phone_number(),
                    nazwa_firmy=fake.company(),
                    stanowisko=fake.job(),
                )
            )
        print(Bazowe_kontakty)
    elif rodzaj == 2:
        for i in range(liczba):
            Biznesowe_kontakty.append(
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
        print(Biznesowe_kontakty)


if __name__ == "__main__":

    Osoba01 = Wizytowka(
        imie="Lukasz",
        nazwisko="Wysocki",
        nazwa_firmy="Marianne",
        stanowisko="Control room assistant",
        adres_email="LukaszJablonski@armyspy.com",
    )

    Osoba02 = Wizytowka(
        imie="Miłosław",
        nazwisko="Kowalczyk",
        nazwa_firmy="Red Robin Stores",
        stanowisko="Financial consultant",
        adres_email="MiloslawWysocki@dayrep.com",
    )

    Osoba03 = Wizytowka(
        imie="Dawid",
        nazwisko="Kamiński",
        nazwa_firmy="Today's Man",
        stanowisko="Chiropractic doctor",
        adres_email="DawidKaminski@rhyta.com",
    )

    Osoba04 = Wizytowka(
        imie="Nadzieja",
        nazwisko="Wysocka",
        nazwa_firmy="Sammy's Record Shack",
        stanowisko="Computer forensic investigator",
        adres_email="NadziejaWysocka@armyspy.com",
    )

    Osoba05 = Wizytowka(
        imie="Felicjan",
        nazwisko="Sobczak",
        nazwa_firmy="The Original House of Pies",
        stanowisko="Mathematical technician",
        adres_email="FelicjanSobczak@jourrapide.com",
    )

    osoby = [Osoba01, Osoba02, Osoba03, Osoba04, Osoba05]

    for i in range(len(osoby)):
        print(osoby[i].imie, osoby[i].nazwisko + ",", osoby[i].adres_email)
    print()

    by_imie = sorted(osoby, key=lambda osoby: osoby.imie)
    by_imie = sorted(osoby, key=lambda osoby: osoby.nazwisko)
    by_imie = sorted(osoby, key=lambda osoby: osoby.adres_email)

    Wizytowka.kontakt(Osoba01)

    Wizytowka.contact(Osoba03)

    Wizytowka.imienazwisko_length(Osoba01)

    create_contacts(2, 11)
