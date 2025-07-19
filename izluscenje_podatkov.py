import re

vzorec = re.compile(
    r'<div class="item-name">\s*(?P<ime>.+?)\s*\(\s*(?P<leto>\d{4})\s*\)\s*</div>.*?'
    r'(?:.*?<a[^>]*>.*?<img src="/i/rt-(?:fresh|rotten|cert)\.png"[^>]*>\s*(?P<tomato_score>\d+)%.*?</a>)?'
    r'(?:.*?<a[^>]*>.*?<img src="/i/imdb\.png"[^>]*>\s*(?P<imdb_score>\d+(?:\.\d+)?)\s*</a>)?',
    re.DOTALL
)

for stran in range(1, 31):
    