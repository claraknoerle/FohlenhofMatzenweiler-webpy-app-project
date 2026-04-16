# Pflichtenheft: Fohlenhof Matzenweiler Webpy-App

## 1. Einführung

### 1.1 Zweck
Dieses Pflichtenheft beschreibt die Anforderungen für die Entwicklung einer webbasierten Anwendung für den Fohlenhof Matzenweiler. Die Anwendung basiert auf dem Legacy-PHP-Code und implementiert die Funktionalität in einem modernen Python-Webframework (web.py).

### 1.2 Scope
Die Anwendung soll eine responsive Website mit folgenden Hauptfunktionen bieten:
- Statische Inhaltsseiten (Home, Über uns, Anlage, Team, Angebote)
- Kostenrechner für Stutfohlenaufzucht
- Galerie mit Bildern
- Impressum und Datenschutz

## 2. Funktionale Anforderungen

### 2.1 Statische Inhalte
- **Home**: Willkommensseite mit Einführung
- **Über uns**: Beschreibung der Familie und Philosophie
- **Anlage**: Informationen über Stallungen und Koppeln
- **Team**: Vorstellung der Familienmitglieder
- **Angebote**: Tabelle mit Preisen für Stutfohlenaufzucht und Boxenhaltung

### 2.2 Kostenrechner
- Eingabe: Aktuelles Alter (in Jahren), Dauer der Aufzucht (in Jahren)
- Berechnung: Zukunftsalter = Alter + Dauer
- Berechnung: Gesamtkosten = Dauer * 12 * 300€
- Ausgabe: Zukunftsalter und formatierte Gesamtkosten

### 2.3 Navigation
- Responsive Navigation mit Links zu allen Hauptseiten
- Footer mit Kontaktinformationen

### 2.4 Galerie
- Anzeige von Bildern des Hofes
- Responsive Grid-Layout

## 3. Nicht-funktionale Anforderungen

### 3.1 Technisch
- **Framework**: web.py (Python)
- **Architektur**: MVC (Model-View-Controller)
- **Frontend**: HTML5, CSS3, JavaScript (minimal)
- **Datenbank**: Nicht erforderlich (statische Daten)
- **Deployment**: Docker-Container

### 3.2 Qualität
- **Sicherheit**: Keine Sicherheitslücken (XSS, etc.)
- **Performance**: Schnelle Ladezeiten (<2s)
- **Usability**: Intuitive Navigation, Mobile-optimiert
- **Wartbarkeit**: Modularer Code, Dokumentation

### 3.3 Compliance
- **Datenschutz**: DSGVO-konform
- **Barrierefreiheit**: WCAG 2.1 AA

## 4. Systemarchitektur

### 4.1 MVC-Struktur
- **Models**: Geschäftslogik (z.B. RechnerModel)
- **Views**: Templates für HTML-Ausgabe
- **Controllers**: Verarbeitung von Requests

### 4.2 Technologie-Stack
- Python 3.x
- web.py
- HTML/CSS/JavaScript
- Docker für Deployment

## 5. Akzeptanzkriterien

### 5.1 Funktional
- Alle Seiten laden korrekt
- Rechner berechnet korrekt
- Navigation funktioniert auf Desktop und Mobile

### 5.2 Qualität
- Code ist dokumentiert
- Unit-Tests vorhanden
- Performance-Tests bestanden

## 6. Risiken und Annahmen

### 6.1 Annahmen
- Alle Bilder und Texte aus dem Legacy-Code sind verfügbar
- web.py ist für die Anforderungen ausreichend

### 6.2 Risiken
- Komplexität der Migration von PHP zu Python
- Fehlende Erfahrung mit web.py

## 7. Meilensteine

1. Analyse des Legacy-Codes ✅
2. Erstellung Pflichtenheft ✅
3. Implementierung MVC-Struktur
4. Entwicklung Frontend
5. Integration Rechner
6. Testing und Deployment
7. Dokumentation abschließen