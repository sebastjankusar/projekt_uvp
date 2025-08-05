import pandas as pd

def doloci_visjo_oceno(vrstica):
    if pd.isna(vrstica["ocena_imdb"]) or pd.isna(vrstica["ocena_rotten_tomatoes"]):
        return "Ni podatkov"
    elif vrstica["ocena_imdb"] == (vrstica["ocena_rotten_tomatoes"] / 10):
        return "Enako"
    elif vrstica["ocena_imdb"] > (vrstica["ocena_rotten_tomatoes"] / 10):
        return "IMDb"
    else:
        return "Rotten Tomatoes"


def je_poseben(vrstica):
    return vrstica["naslov"] in {
        "Epic Movie",
        "Hannah Montana & Miley Cyrus: Best of Both Worlds Concert",
        "Police Academy 5: Assignment Miami Beach",
        "The Toy",
        "Toy Story",
        "The Dark Knight"
    }