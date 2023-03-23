class Bruker:
    """ Superklasse for brukere i skolesystemet. Skal ikke brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    """
    def __init__(self, epost, fornavn, etternavn):
        self._epost = epost
        self._fornavn = fornavn
        self._etternavn = etternavn

    def logg_inn(self):
        print(f"{self._epost} logget inn")

    def logg_ut(self):
        print(f"{self._epost} logget ut")

class Elev(Bruker):
    """ Subklasse for bruker. Oppretter elver i skolesystemet.

    Attributes:
        epost: En string med elevens epost
        fornavn: En string med elevens fornavn
        etternavn: En string med elevens etternavn
        trinn: En integer med elevens klassetrinn
        klasse: En integer med elevens kontaktklasse
        fag: En liste med elevens fag
    
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse, fag):
        super().__init__(epost, fornavn, etternavn)
        self._trinn = trinn
        self._klasse = klasse
        self._fag = fag

    def lever_egenmelding(self):
        pass

class Laerer(Bruker):
    """ Subklasse for bruker. Oppretter lærere i skolesystemet.

    Attributes:
        epost: En string med lærerns epost
        fornavn: En string med lærerns fornavn
        etternavn: En string med lærerns etternavn
        trinn: En integer med lærerns lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, loennskonto):
        super().__init__(epost, fornavn, etternavn)
        self._loennskonto = loennskonto

class Faglaerer(Laerer):
    """ Subklasse for laerer. Oppretter faglærerelærere i skolesystemet.

    Attributes:
        epost: En string med lærerns epost
        fornavn: En string med lærerns fornavn
        etternavn: En string med lærerns etternavn
        loennskonto: En integer med lærerns lønnskonto
        loennskonto: Liste med lærerns kompetanse
        klasser: En liste med lærerns klasser
    
    """
    def __init__(self, epost, fornavn, etternavn, loennskonto, kompetanse, klasser):
        super().__init__(epost, fornavn, etternavn, loennskonto)
        self._kompetanse = kompetanse
        self._klasser = klasser

    def sett_karakter(self):
        pass

class Kontaktlaerer(Laerer):
    """ Subklasse for laerer. Oppretter kontaktlærere i skolesystemet.

    Attributes:
        epost: En string med lærerns epost
        fornavn: En string med lærerns fornavn
        etternavn: En string med lærerns etternavn
        loennskonto: En integer med lærerns lønnskonto
        loennskonto: Liste med lærerns kontaktklasse
        trinn: En integer med lærerns kontaktklassetrinn
    
    """
    def __init__(self, epost, fornavn, etternavn, loennskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, loennskonto)
        self._klasse = klasse
        self._trinn = trinn

    def fiks_fravaer(self):
        pass        

# Denne brukes for testing. Betyr at koden inne i if-setningen kun kjøres hvis vi  trykker "play" på denne fila, eller kjører denne fila i terminalen
if __name__ == "__main__":
    ravi = Laerer("ravim@viken.no", "David Ravi", "Manikarnika", 97003406654)
    ravi.logg_inn()

    christen = Elev("christens@viken.no", "Christen Backe", "Staib", 3, "3STF", ["IT2", "R2", "Fysikk2"])
    christen.logg_inn()

    ravi.logg_ut()
    christen.logg_ut()