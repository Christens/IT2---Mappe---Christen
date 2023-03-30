# Objektorientert programmering

### Objektorienter programmering (OOP) er en effektiv programmeringsmåte for å opprette flere objkter med samme egenskaper

Nøkkelord er:
- Objekt
- Metode
- Arv
    - Superklasse
    - Subklasse
- Instansvariabel
- Konstruktør

#### Objekt
Objektene i OOP er de forskjellige enhetene som produseres av klassen.
Felles for objektene er at de har felles egenskaper som dannes av konstruktøren.

#### Konstruktør
Konstruktøren er en funksjon som danner initialvaribler for objektene.
Den danner selve objektet med en rekke variabler som bestemmer objektenes .

#### Initialvariabler
Initialvariablene er objektenes egenskaper.
Hvis objektene hadde vørt personer kan konstruktøren og initialvaribalene se slik ut:
```python
    class Person:
    def __init__(self, navn, høyde, alder):
        self._navn = navn
        self._høyde = høyde
        self._alder = alder
```

#### Metode
Metoder er funksjoner som brukes til å blant annet: hente informasjon fra objektene eller endre på objektenes egenskaper.

```python
    def vokser(self):
        self._høyde += 1 #Øker personens høyde med 1
```

#### Arv
Arv brukes for å føre initialverdier fra en superklasse til en subklasse.
Superklasser en klassen som arves fra, subklasser er klassen som arver.

Hvis perosner med briller skal ha en egen initialverdi uten at personer uten briller skal få en egenskap som sier om de har det eller ikke, kan agenskapene fra "Person" arves til denne klassen.

```python
    class Briller(Person):
        __init__(self):
        super().__init__(navn, høyde, alder)
        self._briller = True
```

Subklasser vil også arve superklassens metoder

## Eksempel
Spiller i pygame med bruk av OOP og arv:
[Skyteblink](Skyteblink_pygame/verden.py)
