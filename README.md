# FohlenhofMatzenweiler-webpy-app-project

Internetseite für den Pferdehof meiner Familie

## 📋 Dokumentation

### Wichtige Dokumente

| Dokument | Beschreibung |
|----------|-------------|
| [Pflichtenheft](docs/handbuch/PFLICHTENHEFT.md) | Systemanforderungen & Spezifikationen |
| [Handbuch](docs/handbuch/HANDBUCH.md) | Installation, Konfiguration & Nutzung |

### Legacy-Code Analyse

Die Anwendung basiert auf dem analysierten PHP-Legacy-Code aus `upload/Projekt_PHP_Clara_Knörle.zip`.

## 🚀 Quick Start

```bash
# Abhängigkeiten installieren
pip install web.py

# Anwendung starten
python app.py
```

Öffne http://localhost:8080 im Browser.

## 📁 Projektstruktur

```
├── app.py              # Hauptanwendung
├── models/             # Geschäftslogik
├── views/              # HTML-Templates
├── controllers/        # Request-Handler
├── static/             # CSS, JS, Bilder
├── tests/              # Unit-Tests
├── docs/               # Dokumentation
│   └── handbuch/
└── upload/             # Legacy-Code & Analyse
```
