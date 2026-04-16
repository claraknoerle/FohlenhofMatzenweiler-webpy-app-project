# Handbuch: Fohlenhof Matzenweiler Webpy-App

## 1. Überblick

Dieses Handbuch beschreibt die Installation, Konfiguration und Nutzung der webbasierten Anwendung für den Fohlenhof Matzenweiler.

## 2. Systemvoraussetzungen

- Python 3.8+
- Docker (optional für Deployment)
- Webbrowser (Chrome, Firefox, Safari, Edge)

## 3. Installation

### 3.1 Lokale Installation

```bash
# Repository klonen
git clone https://github.com/claraknoerle/FohlenhofMatzenweiler-webpy-app-project.git
cd FohlenhofMatzenweiler-webpy-app-project

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder venv\Scripts\activate  # Windows

# Abhängigkeiten installieren
pip install web.py

# Anwendung starten
python app.py
```

### 3.2 Docker-Installation

```bash
# Image bauen
docker build -t fohlenhof-app .

# Container starten
docker run -p 8080:8080 fohlenhof-app
```

## 4. Konfiguration

### 4.1 Umgebungsvariablen

Erstelle eine `.env`-Datei im Projektroot:

```
PORT=8080
DEBUG=True
```

### 4.2 Datenbank (falls erforderlich)

Die aktuelle Version verwendet keine Datenbank. Für zukünftige Erweiterungen:

```python
# In models/database.py
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('fohlenhof.db')
```

## 5. Nutzung

### 5.1 Starten der Anwendung

```bash
python app.py
```

Öffne http://localhost:8080 im Browser.

### 5.2 Navigation

- **Home**: Startseite mit Willkommenstext
- **Über uns**: Informationen zur Familie
- **Anlage**: Beschreibung der Stallungen
- **Team**: Vorstellung der Mitglieder
- **Angebote**: Preisübersicht
- **Galerie**: Bildergalerie
- **Rechner**: Kostenberechnung
- **Impressum**: Rechtliche Informationen

### 5.3 Kostenrechner

1. Gebe das aktuelle Alter des Fohlens ein (z.B. 0.5 für 6 Monate)
2. Gebe die Dauer der Aufzucht in Jahren ein (z.B. 3)
3. Klicke "Berechnen"
4. Ergebnis: Zukunftsalter und Gesamtkosten werden angezeigt

## 6. Wartung

### 6.1 Logs

Logs werden in `logs/app.log` gespeichert.

### 6.2 Backups

- Code: Git-Repository
- Statische Dateien: Regelmäßige Sicherung des `static/`-Ordners

### 6.3 Updates

```bash
git pull
pip install -r requirements.txt --upgrade
```

## 7. Fehlerbehebung

### 7.1 Häufige Probleme

**Port belegt:**
```bash
# Anderen Port verwenden
PORT=8081 python app.py
```

**Module nicht gefunden:**
```bash
pip install web.py
```

**Bilder laden nicht:**
- Überprüfe Pfade in `static/images/`
- Stelle sicher, dass Dateien existieren

### 7.2 Support

Bei Problemen:
1. Logs überprüfen
2. GitHub-Issues erstellen
3. Dokumentation konsultieren

## 8. Entwicklung

### 8.1 Projektstruktur

```
fohlenhof-app/
├── app.py              # Hauptanwendung
├── models/             # Geschäftslogik
│   ├── __init__.py
│   └── rechner.py
├── views/              # Templates
│   ├── base.html
│   ├── home.html
│   └── ...
├── controllers/        # Request-Handler
│   ├── __init__.py
│   └── main.py
├── static/             # CSS, JS, Bilder
│   ├── css/
│   ├── js/
│   └── images/
├── tests/              # Unit-Tests
└── docs/               # Dokumentation
```

### 8.2 Testing

```bash
# Tests ausführen
python -m pytest tests/

# Coverage
python -m pytest --cov=.
```

### 8.3 Deployment

```bash
# Produktions-Deployment mit Gunicorn
pip install gunicorn
gunicorn app:app -b 0.0.0.0:8080
```

## 9. Sicherheit

- Keine Benutzereingaben werden in Datenbank gespeichert
- XSS-Schutz durch Template-Escaping
- HTTPS empfohlen für Produktion

## 10. Glossar

- **MVC**: Model-View-Controller Architektur
- **web.py**: Leichtes Python-Webframework
- **Fohlen**: Junges Pferd
- **Stutfohlen**: Weibliches Fohlen

## 11. Anhänge

### 11.1 API-Referenz

Die Anwendung verwendet keine externe API.

### 11.2 Changelog

- v1.0.0: Erste Version basierend auf PHP-Legacy-Code