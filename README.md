# Institutionen ohne Gedächtnis

**Kybernokratie: ein offenes Format, um öffentliche Stellen an ihren eigenen Prognosen zu messen — und die Regel, die daraus folgt**

Felix Lind, Düsseldorf, 2026 · unter Mitarbeit von Claude (Anthropic)

Fassung 0.7 vom 10.09.2026. Erstfassung 0.1 vom 28.08.2026. Preprint, DOI: **[10.5281/zenodo.22685529](https://doi.org/10.5281/zenodo.22685529)**

→ **[Das Paper lesen: paper/PAPER.md](paper/PAPER.md)**

## Worum es geht

Öffentliche Institutionen treffen laufend datierte, zahlenmäßige Aussagen über die Zukunft: Haushaltsprognosen, Fertigstellungstermine, Zielzahlen. Fast keine davon wird später mit dem Eingetretenen verglichen. Das Paper schlägt ein offenes, hostbares Format vor, das solche Aussagen sammelt, nach Ablauf auflöst und mit dem Brier-Score zu einer öffentlichen Trefferquote je Institution verdichtet: das **Wettbuch**.

Daraus folgt eine Regel für den Umgang mit maschinell berechneten Empfehlungen, die **Erwartungsklausel**:

> Wer im Namen anderer entscheidet, folgt der berechneten Empfehlung — oder hinterlegt öffentlich und datiert, welches bessere Ergebnis er stattdessen erwartet. Abweichen ist erlaubt. Vergessen nicht.

Die Regel ist erst legitim, wenn das Buch voll ist: wenn die Maschine über Jahre neben der Institution in derselben Tabelle gestanden hat. Die Ordnung, in der diese Regel gilt, nennt das Paper **Kybernokratie** und grenzt sie von der älteren, kritischen Verwendung des Wortes (Robins/Webster 1988, Tiqqun 2001) ab.

## Was dazugehört

- **Format und Referenz-Implementierung:** [festgehalten](https://github.com/Felix3c/festgehalten) (Format v1 mit Verfassung, seit 28.08.2026)
- **Die Wettbücher,** darunter „Köln gegen Köln": https://felix3c.github.io/festgehalten/

## Prüfsumme und Zeitstempel

Neben dem Paper liegen zwei Dateien, mit denen sich belegen lässt, dass genau dieser Text am 10.09.2026 existierte:

| Datei | Zweck |
|---|---|
| `paper/PAPER.md.sha256` | SHA-256-Prüfsumme der Datei |
| `paper/PAPER.md.ots` | OpenTimestamps-Beleg (Bitcoin-verankert) |

Prüfen:

```
sha256sum -c paper/PAPER.md.sha256
ots verify paper/PAPER.md.ots
```

Unter Windows findet der ots-Client libssl oft nicht; dafür liegt `paper/ots-windows.py` bei:

```
python paper/ots-windows.py verify paper/PAPER.md.ots
```

Der Stempel beweist, dass die Datei an dem Tag existierte. Die Erstfassung 0.1 trägt das Datum 28.08.2026.

## Zitieren

Felix Lind (2026). *Institutionen ohne Gedächtnis. Kybernokratie: ein offenes Format, um öffentliche Stellen an ihren eigenen Prognosen zu messen — und die Regel, die daraus folgt.* Fassung 0.7, 10.09.2026. Zenodo. https://doi.org/10.5281/zenodo.22685529

Maschinenlesbar in [`CITATION.cff`](CITATION.cff). Auf Zenodo liegen PDF, Markdown, Prüfsumme und OpenTimestamps-Beleg dieser Fassung.
Concept-DOI für alle Fassungen: https://doi.org/10.5281/zenodo.22685528

## Lizenz

[CC BY-ND 4.0](LICENSE): Weitergabe und Zitieren mit Namensnennung erlaubt, Bearbeitungen nicht. Die Erwartungsklausel und die sechs Sätze der Definition (§6.1) dürfen selbstverständlich wörtlich in Satzungen, Geschäftsordnungen und Richtlinien übernommen werden; das ist ein Zitat, keine Bearbeitung.
