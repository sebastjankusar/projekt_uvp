import re
import os

def naredi_seznam_filmov():
    vzorec = re.compile(
        r'<div class="item-name">\s*(?P<naslov>.+?)\s*\(\s*(?P<leto>\d{4})\s*\)\s*</div>.*?'
        r'(?:.*?<a[^>]*>.*?<img src="/i/rt-(?:fresh|rotten|cert)\.png"[^>]*>\s*(?P<ocena_rotten_tomatoes>\d+)%.*?</a>)?'
        r'(?:.*?<a[^>]*>.*?<img src="/i/imdb\.png"[^>]*>\s*(?P<ocena_imdb>\d+(?:\.\d+)?)\s*</a>)?',
        re.DOTALL
    )

    filmi = []
    for stran in range(1, 31):
        with open(os.path.join("strani_seznama", f"stran{stran}.html")) as dat:
            besedilo = dat.read()

        for najdba in vzorec.finditer(besedilo):
            filmi.append({
                "naslov": najdba["naslov"], 
                "leto": int(najdba["leto"]), 
                "ocena_rotten_tomatoes": int(najdba["ocena_rotten_tomatoes"]) if najdba["ocena_rotten_tomatoes"] else None, 
                "ocena_imdb": float(najdba["ocena_imdb"]) if najdba["ocena_imdb"] else None,
                })
    
    return filmi