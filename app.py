from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

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
            rows = table.find_all('tr')

            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    material = columns[0].text.strip()
                    cena = columns[1].text.strip()
                    data.append({'material': material, 'cena': cena})
        else:
            data = []

        # Zapisz dane do pliku JSON
        with open('materials_data.json', 'w') as json_file:
            json.dump(data, json_file)

        # Zwróć dane do szablonu HTML
        return render_template('table.html', data=data)
    else:
        return "Błąd podczas pobierania strony. Kod statusu: " + str(response.status_code)

if __name__ == '__main__':
    app.run(port=5051)
