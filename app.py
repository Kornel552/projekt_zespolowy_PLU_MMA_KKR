from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS  # Importuje CORS

app = Flask(__name__)
# CORS(app)

@app.route('/')
def scrape_and_display():
    # Pobierz dane z witryny i przetwórz je
    url = "https://www.ekosylwia.pl/cennik"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        if table:
            data = []
            rows = table.find_all('tr')  # Usuwamy pomijanie pierwszego wiersza z nagłówkami

            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:  # Sprawdzamy, czy mamy co najmniej 2 kolumny
                    material = columns[0].text
                    cena = columns[1].text
                    data.append({'material': material, 'cena': cena})
                # else:
                #     data.append({'material': 'Brak danych', 'cena': 'Brak danych'})
        else:
            data = []

        return render_template('table.html', data=data)
    else:
        return "Błąd podczas pobierania strony. Kod statusu: " + str(response.status_code)

if __name__ == '__main__':
    app.run()
