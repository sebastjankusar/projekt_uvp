import re
import os


def naredi_seznam_filmov():

    vzorec = re.compile(
        r'<div class="item-name">\s*(?P<naslov>.+?)\s*(?:\(\s*(?P<leto>\d{4})\s*\)\s*)?</div>\s*'
        r'<div class="item-rank">\d*</div>\s*'
        r'<div class="item-checkbox"></div>\s*'
        r'<div class="item-movie-info"><div class="flex-grow1"></div><div class="movie-ratings">'
        r'(?:<a href="/item-redirect\?id=\d*&type=0"[^>]*><img src="/i/rt-(?:fresh|rotten|cert)\.png" />'
        r'(?P<ocena_rotten_tomatoes>\d+)%</a>)?'
        r'(?:\s*<a href="/item-redirect\?id=\d*&type=1"[^>]*><img src="/i/imdb\.png" />'
        r'(?P<ocena_imdb>\d+(?:\.\d+)?)</a>)?'
        r'</div><div class="flex-grow1"></div></div>',
        re.DOTALL
    )
    
    filmi = []
    for stran in range(1, 31):
        with open(os.path.join("strani_seznama", f"stran{stran}.html")) as dat:
            besedilo = dat.read()
        for najdba in vzorec.finditer(besedilo):
            filmi.append({
                "naslov": najdba["naslov"], 
                "leto": int(najdba["leto"]) if najdba["leto"] else None, 
                "ocena_rotten_tomatoes": int(najdba["ocena_rotten_tomatoes"]) if najdba["ocena_rotten_tomatoes"] else None, 
                "ocena_imdb": float(najdba["ocena_imdb"]) if najdba["ocena_imdb"] else None,
                })
    
    return filmi