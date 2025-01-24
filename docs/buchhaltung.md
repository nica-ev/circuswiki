---
publish: true
tags:
  - moc
created: 2025-01-19 16:47:55
update: 2025-01-23 05:44:55
title: Buchhaltung Übersicht
authors:
  - Marc Bielert
---

# Buchhaltung Übersicht

Unsere Buchhaltung basiert auf dem sogenannten "Plaintext Accounting". 
Man schreibt alle Daten / Transaktionen in eine Textdatei in einem gut menschlich lesbarem Format

So sieht eine Transaktion in diesem Format aus:
```
2023-01-09 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_004.jpg" ^2023_004

2023-01-09 ! "Hornbach" "Buerolampe" #open #scanned ^2023_004

    Ausgaben:Buero:Sonstiges                                    64.95 EUR

    Verbindlichkeiten:Person:Marc-Bielert
```

# Todo

Spenden sollten immer klar getrackt werden, entweder durch ein extra Konto, oder tags.
Dies ist wichtig für die [[Tätigkeitsberichte]] welche wir jährlich erstellen müssen. #todo 