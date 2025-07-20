import csv

def shrani_filme(filmi):
     with open("filmi.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(
            [
                "naslov",
                "leto",
                "ocena_rotten_tomatoes",
                "ocena_imdb",
            ]
        )

        for film in filmi:
            pisatelj.writerow(
                [
                    film["naslov"],
                    film["leto"],
                    film["ocena_rotten_tomatoes"],
                    film["ocena_imdb"],
                ]
            )