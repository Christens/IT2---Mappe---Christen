# Presentere data

Med å presentere data mener vi all mulig informasjon
Feks:
- Tempratur
- Tekst
- Tall
- Bilder
- Filmer

I IT2 lærer vi to måter å presentere data på, nemlig:
- Tegning av grafer
- Nettsider

## Tegne grafer

For å tegne grafer i Python kan vi bruke biblioteket `matplotlib`.
Eks:


## Lage nettsider (HTML/Flask)
Nettsider er en god måte å presentere data på. Json-filer eller api-er kan blant annet brukes for å skaffe data til siden.  
I dette prosjektet: [Filmsiden](https://github.com/Christens/Filmsiden) er begge deler brukt for å hente filmer til siden.  
"Søk" bruker API, ratingssystemet på hjemmesiden og "Anbefalt" bruker json

### json
Slik kan en json-fil åpnes og omformuleres til en ordbok med informasjon
```python
    import json

    def json_filmer():
        fil = open("json/imdb.json")
        filmer = json.load(fil)
        fil.close()
        return filmer
```
Eks:
```python
    [
        {
        "navn": "Yôjinbô",
        "bilde": "https://m.media-amazon.com/images/M/MV5BZThiZjAzZjgtNDU3MC00YThhLThjYWUtZGRkYjc2ZWZlOTVjXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",
        "sjangere": ["Action", "Drama", "Thriller"],
        "url": "https://www.imdb.com//title/tt0055630/",
        "beskrivelse": "A crafty ronin comes to a town divided by two criminal gangs and decides to play them against each other to free the town.",
        "dato": "1961-09-13",
        "regissører": ["Akira Kurosawa"],
        "trailer": "https://www.imdb.com/video/imdb/vi1659814169/imdb/embed?autoplay=false&width=640",
        "karakter": 8.2
        },
        {
        "navn": "Witness for the Prosecution",
        "bilde": "https://m.media-amazon.com/images/M/MV5BNDQwODU5OWYtNDcyNi00MDQ1LThiOGMtZDkwNWJiM2Y3MDg0XkEyXkFqcGdeQXVyMDI2NDg0NQ@@._V1_.jpg",
        "sjangere": ["Crime", "Drama", "Mystery"],
        "url": "https://www.imdb.com//title/tt0051201/",
        "beskrivelse": "A veteran British barrister must defend his client in a murder trial that has surprise after surprise.",
        "dato": "1958-02-06",
        "regissører": ["Billy Wilder"],
        "trailer": "https://www.imdb.com/video/imdb/vi421183001/imdb/embed?autoplay=false&width=640",
        "karakter": 8.4
        }
    ]
```