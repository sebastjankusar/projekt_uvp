import requests
import os

def naredi_html_strani():
    url = "https://www.listchallenges.com/every-number-1-movie-in-the-usa-box-office"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # kopiran iz https://medium.com/@datajournal/http-headers-for-web-scraping-9073c67e22f2 (example header)

    for stran in range(1, 31):
        if stran == 1:
            odgovor = requests.get(url,
            headers=headers,
        )

        else:
            odgovor = requests.get(f"{url}/list/{stran}",
            headers=headers,
        )

        if odgovor.status_code != 200:
                print("napaka", stran)
                continue

        with open(os.path.join("strani_seznama", f"stran{stran}.html"), "w", encoding="utf-8") as dat:
            dat.write(odgovor.text)

