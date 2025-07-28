import pandas as pd

def doloci_visjo_oceno(vrstica):
    if pd.isna(vrstica["ocena_imdb"]) or pd.isna(vrstica["ocena_rotten_tomatoes"]):
        return "ni_podatkov"
    elif vrstica["ocena_imdb"] == (vrstica["ocena_rotten_tomatoes"] / 10):
        return "enako"
    elif vrstica["ocena_imdb"] > (vrstica["ocena_rotten_tomatoes"] / 10):
        return "imdb"
    else:
        return "rotten_tomatoes"