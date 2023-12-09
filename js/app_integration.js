// Pobierz zawartość z aplikacji Flask i wstaw ją do diva "flask-app"
fetch('/get_flask_app_content')
    .then(response => response.text())
    .then(data => {
        document.getElementById('flask-app').innerHTML = data;
    })
    .catch(error => console.error('Błąd podczas pobierania zawartości aplikacji Flask:', error));
