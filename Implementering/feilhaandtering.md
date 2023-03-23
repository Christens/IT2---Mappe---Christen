# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil

Håndtering av kjøretidsfeil gjøre med nøkkelordene try og except.
Ptyhon forsøker å kjøre koddeblokken som ligger under 'try:', hvis python får en kodemelding, vil den kjøre kodeblokken osm ligger under 'except:'

``` python
 try:
     alder = int(input("Alder: "))
     fødselsår = 2023 - alder
     print(F"Fødselsår: {fødselsår}")
 except:
     print("Feil: Alder må være et positivt heltall")
```

### Eksperttips: While-løkke med try-except

``` python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print(f"Alder må være et heltall, prøv igjen")

føselsår = 2023 - alder
print(f"Fødselsår: {føselsår}")
```

## Logiske feil i programmer

For å oppdage logiske feil i programmet kan vi bruke nøkkelordet assert for å forsikre oss om at koden gir korrekt resultat

Eks:
```python
def areal(l,b):
    assert l >=0, b >= 0
    return l*b
def omkrets(l,b):
    return 2*l+2*b

assert areal(3,2) == 6
assert areal(3,3) == 9

assert omkrets(3,3) == 12
assert omkrets(2,3) == 10
```

## Håndtering av kjøretidsfeil og logiske feil

```python
while True:
    try:
        alder = int(input("Alder: "))
        assert alder >=0
        break
    except:
        print(f"Alder må være et heltall, prøv igjen")

føselsår = 2023 - alder
print(f"Fødselsår: {føselsår}")
```
