content = """# Python Lernpfad – Lesebuch (ohne Code)
Dieses Dokument ist dein **reines Text-„Lesebuch“** zu unseren Lessons. Keine Code-Beispiele – nur klare Erklärungen, typische Fehler und kurze Checks. 

---
# Lesson 001 – Basics (Kurzleitfaden)

## Was lernst du hier?
- REPL vs. Script verstehen und sinnvoll einsetzen.
- Variablen anlegen, benennen und Datentypen unterscheiden.
- Strings sicher bearbeiten (Slicing, Methoden, Trimmen).
- f‑Strings für sauberes Formatieren von Ausgaben nutzen.

---

# Lesson 001 – Basics (Lesebuch)

## 1) REPL vs. Script
- **REPL** (interaktive Konsole): Sofort testen, was passiert. Ideal zum Ausprobieren einzelner Ausdrücke.
- **Script** (Datei): Mehrere Schritte als Programm speichern und reproduzierbar ausführen; perfekt für Git.
- **Workflow**: Erst im REPL experimentieren → dann als Script sauber dokumentiert.

---

## 2) Variablen & Benennung
- **Variable** = Name, der auf einen Wert zeigt (Bindung). Python ist **dynamisch typisiert**: der Typ folgt dem Wert.
- **Namen**: `snake_case`, sprechend, keine Umlaute/Leerzeichen, nicht mit Zahl starten.
- **Zuweisung** überschreibt die Bindung (der alte Wert kann weiterleben, wenn noch Referenzen existieren).

---

## 3) Datentypen (Kernwissen)

### int — Ganzzahlen
- Ganze Zahlen, beliebige Größe (sofern Speicher reicht).
- Typische Nutzung: Zählen, Indizes, Offsets.

### float — Kommazahlen
- Gleitkomma (binäre Repräsentation) → **Rundungsdarstellung kann „krumm“ wirken**.
- Für Geldbeträge besser formatieren oder spezielle Typen nutzen (später).

### str — Text
- Folge von Zeichen (Unicode). **Unveränderlich**: „Änderungen“ erzeugen neue Strings.
- Zugriff über Position (Index), Teilstücke (Slicing).

### bool — Wahr/Falsch
- Genau zwei Werte: `True`, `False`.
- **Truthiness**: Leere Strings/Listen/0 gelten „falsey“, alles andere „truthy“.

### None — kein Wert
- Bedeutet „nicht vorhanden / unbekannt“. Eigener Typ `NoneType`.
- Häufig als Platzhalter oder Rückgabewert, wenn es „nichts“ gibt.

---

## 4) Type Casting & Truthiness
- **Umwandeln**: „Zahl ↔ Text ↔ Bool“ ist möglich, wenn sinnvoll.
- Merkpunkte:
  - `int(3.9)` **schneidet ab** (ergibt 3), rundet nicht.
  - Ein Text wie „3.9“ ist **kein** int.
  - `bool("")` ist **False**, `bool(" ")` ist **True** (Leerzeichen ist Zeichen).
  - **Eingaben** kommen als Text; bei Bedarf umwandeln.

---

## 5) Strings – was du sicher können musst
- **Index & Slice**: Start inklusiv, **Ende exklusiv**. Negative Indizes zählen von hinten.
- **Länge**: Zählt **alle** Zeichen (inkl. Leerzeichen).
- **Typische Aufgaben**:
  - Groß-/Kleinschreibung vereinheitlichen (z. B. Anzeige/Vergleich).
  - **Trimmen**: Rand-Leerraum entfernen, bevor du Längen/Prüfungen machst.
  - **Suchen/Ersetzen**: Positionen finden, Teiltexte tauschen.
  - **Aufteilen/Verbinden**: Text in Wörter trennen und mit einem Trennzeichen wieder zusammenführen.
- **Praxisfalle**: Strings sind immutable → nie „in place“, immer Ergebnis weiterverwenden.

---

## 6) f-Strings – sauberes Formatieren
- **Idee**: Text + Werte in einem Schritt; lesbarer und sicherer als Verkettung.
- **Was können sie?**
  - Rechnen oder Methoden **direkt** im Platzhalter.
  - Formatierungen: feste Nachkommastellen (`:.2f`), Tausendertrennzeichen (`:,`), Prozent (`:.1%`), Ausrichtung/Abstände.
- **Nutzen**: Klare Ausgaben (z. B. Berichte/Logs), weniger Fehler.

---

## 7) Typische AP2-Stolpersteine (und Gegenmittel)
- **Slicing-Ende fehlt mit Absicht** → in Gedanken immer „bis, aber **ohne** Ende“.
- **„-0“ ist „0“** → kann leere Slices erzeugen (negatives Ende hilft hier nicht).
- **Zahl ≠ String** → keine Textmethoden auf Zahlen; Zahlen **formatieren**, nicht „ersetzen“.
- **Leerzeichen** zählen mit → bei Bedarf vorher **trimmen**.
- **Eingaben** sind Text → bei Rechnen erst **konvertieren**.

---






## Platzhalter für weitere Lessons (kommen später)
- **Lesson 003 – Funktionen**: Parameterarten, Rückgaben, Scope, Typannotationen, gute Signaturen.
- **Lesson 004 – Collections**: Listen/Tuples/Sets/Dictionaries, typische Muster (Suchen, Zählen, Gruppieren).
- **Lesson 005 – Dateien & Formate**: Text/CSV/JSON/YAML/XML, Lesen/Schreiben, Pfad-Grundlagen.
- **Lesson 006 – Fehlerbehandlung**: try/except/else/finally, eigene Fehlerklassen, sauberes Aufräumen.
- **Lesson 007 – OOP**: Klassen, __init__, dataclasses, einfache Modellierung.
- **Lesson 008 – Module/Venv/Imports**: Projektstruktur, Pakete, Abhängigkeiten sauber managen.
- **Lesson 009 – Tests**: pytest-Grundlagen, Arrange–Act–Assert, Fixtures.
- **Lesson 010 – Mini-Projekt**: Alles zusammenführen, kleine App mit klarer Struktur.

---