# Kybernokratie: Demokratie mit Gedächtnis

## Ein offenes Format, um öffentliche Stellen an ihren eigenen Prognosen zu messen, und die Regel, die daraus folgt

Felix Lind, Düsseldorf · unter Mitarbeit von Claude (Anthropic)
Fassung 0.8 — 10.09.2026. Erstfassung 0.1 vom 28.08.2026. Preprint. DOI dieser Fassung: 10.5281/zenodo.22686099 · alle Fassungen: 10.5281/zenodo.22685528

---

**Zusammenfassung.** Öffentliche Institutionen treffen laufend datierte, zahlenmäßige
Aussagen über die Zukunft — Haushaltsprognosen, Fertigstellungstermine, Zielzahlen.
Fast keine davon wird später mit dem Eingetretenen verglichen. Wir schlagen ein
offenes, hostbares Format vor, das solche Aussagen sammelt, nach Ablauf auflöst und
mit einer strengen Bewertungsregel (Brier-Score, Punktabstand) zu einer öffentlichen
Trefferquote je Institution verdichtet. Im Unterschied zu Prognosemärkten und
Prognoseturnieren braucht das Format weder Geld noch Teilnahme: Die Behauptungen
existieren bereits. Wir zeigen am Beispiel der Stadt Köln (2024–2026), dass sich ein
solches Buch aus öffentlichen Quellen füllen lässt, beschreiben den Mechanismus, über
den es sich verbreitet, ohne dass jemand beitreten muss, und leiten daraus eine Regel
für den Umgang mit maschinell berechneten Empfehlungen ab, die erst dann legitim
wird, wenn ein solches Buch über Jahre gefüllt ist. Die Ordnung, in der diese Regel
gilt, nennen wir Kybernokratie und grenzen sie von der älteren, kritischen Verwendung
des Wortes ab. Das Paper enthält eigene, datierte Prognosen über seine Wirkung.

---

## 1. Das Problem: Institutionen haben kein Gedächtnis

Am 26. Juni 2026 korrigierte die Stadt Köln ihre Prognose für das Haushaltsdefizit
2026 von 488,8 auf 594,8 Millionen Euro — nach nur einem halben Jahr um 106 Millionen.
[1] Die Mitteilung nennt Ursachen und Gegenmaßnahmen. Sie nennt nicht, wie oft die
Kämmerei in den letzten zehn Jahren im Juni richtig lag. Niemand nennt das. Es ist
nirgends nachzulesen.

Das ist kein Kölner Problem. Jede Verwaltung, jedes Ministerium, jeder Rat produziert
Zukunftsaussagen: Termine („Eröffnung 2024"), Mengen („2.000 Kita-Plätze bis 2026"),
Beträge („Kosten bleiben unter 600 Millionen"). Sie werden gedruckt, zitiert,
beschlossen — und dann vergessen. Wird eine Aussage verfehlt, gibt es eine neue
Aussage. Es gibt keine Stelle, an der die alte neben der neuen steht.

Die Folge ist nicht, dass Institutionen lügen. Die Folge ist, dass sie **nicht
lernen können**, weil ihnen das Signal fehlt, das Lernen voraussetzt: der Vergleich
von Erwartung und Ergebnis. Ein Wetterdienst, der seine Vorhersagen nie mit dem
Wetter vergleicht, wird nicht besser. Öffentliche Institutionen sind, was Prognosen
angeht, Wetterdienste ohne Wetter.

Und die zweite Folge: Ohne Gedächtnis gibt es keine Grundlage, zwischen einer
Institution, die gut vorhersagt, und einer, die es nicht tut, zu unterscheiden.
Vertrauen wird deshalb nach Amt, Tonfall und Parteibuch vergeben — nicht nach
Trefferquote.

Auf das Wort bin ich nicht in Köln gekommen, sondern beim Nachdenken darüber, warum
im Moment niemand mit der Politik zufrieden ist. Deutschland ging es so lange so gut,
dass niemand es anders haben wollte: Die Wirtschaft wuchs von 2010 bis 2019 zehn Jahre in
Folge, die längste Wachstumsphase des vereinten Deutschlands, und die Zahl der Arbeitslosen
fiel von 4,86 Millionen (2005) auf 2,27 Millionen (2019) [14]. Die Wahl 2017 gewann ein
Programm, dessen Titel das Bestehende zum Ziel erklärte: „Für ein Deutschland, in dem wir
gut und gerne leben" [15]. Also hat die Politik erhalten, was war, und das war
jahrzehntelang die richtige Wahl. Aber wer nur erhält und nie den nächsten Schritt wagt,
wird irgendwann abgehängt, und das Ergebnis sehen wir jetzt: Seit 2019 wächst die
Wirtschaft nicht mehr. 2024 lag das Bruttoinlandsprodukt 0,3 % über dem Stand von 2019,
und 2023 und 2024 schrumpfte es zwei Jahre in Folge [16]. Ich nenne das
Erhaltungspolitik ohne Horizont. Die Kölner Zahlen sind der kleinste Fall davon: Eine
Stadt korrigiert um 106 Millionen, und niemand kann sagen, ob das viel ist, weil
niemand die alten Zahlen neben die neuen gelegt hat. Wer kein Gedächtnis hat, kann
weder erhalten noch vorangehen, er kann nur reagieren. Dieses Paper ist der Versuch,
das Gedächtnis zu bauen.

## 2. Vorarbeiten — und warum keine davon Institutionen erreicht hat

Die Idee, Prognosegüte zu messen, ist alt und gut belegt.

**Brier (1950)** führte in der Meteorologie eine Bewertungsregel ein, bei der die
ehrliche Wahrscheinlichkeit die einzige Strategie ist, die auf Dauer gewinnt
(*proper scoring rule*): Wer übertreibt, verliert im Mittel. [2]

**Tetlock (2005, 2015)** zeigte in *Expert Political Judgment* und den Good-Judgment-
Turnieren, dass sich politische Prognosen messen lassen, dass anerkannte Experten
dabei kaum besser als Zufall abschneiden und dass eine kleine Gruppe von
„Superforecastern" sie systematisch schlägt. [3][4]

**Hanson (2000)** schlug mit der *Futarchy* vor, Wertentscheidungen per Abstimmung
und Faktenfragen per Wettmarkt zu klären: „Vote on values, bet on beliefs." [5] Das
ist strukturell dasselbe Zwei-Ebenen-Modell, auf das wir in Abschnitt 5 kommen —
26 Jahre früher.

**Prognosemärkte und -plattformen** (Metaculus, Polymarket, Good Judgment Open)
betreiben das heute im Dauerbetrieb, mit Hunderttausenden Teilnehmern.

Institutionen *sind* gemessen worden — aber als Studie, nicht als Buch. **Flyvbjerg
(2003, 2014)** hat Tausende öffentliche Großprojekte gegen ihre eigenen Kosten- und
Terminzusagen gestellt: neun von zehn überziehen, im Mittel um 28 %; seine *Reference
Class Forecasting* setzt die Basisrate der Institution gegen ihre Behauptung. [9]
**Frankel (2011)** zeigte für 33 Länder, dass amtliche Haushaltsprognosen systematisch
zu optimistisch sind, am stärksten im dritten Jahr. [10] In Deutschland bewerten
Bundesbank und ifo regelmäßig die Treffsicherheit von Gemeinschaftsdiagnose und
Steuerschätzung.

Was diese Arbeiten gemeinsam haben: Sie sind rückblickend, einmalig, von außen — ein
Aufsatz erscheint, und die Institution macht weiter wie vorher. Keine führt das Buch
laufend, öffentlich, je Institution, mit Rangliste, in einem Format, das jede andere
Stelle übernehmen kann. Prognoseturniere und Märkte tun das zwar laufend, erreichen
aber aus drei Gründen keine Behörde:

1. **Sie messen Personen, nicht Ämter.** Tetlocks Turniere bewerten Individuen, die
   sich freiwillig melden. Eine Kämmerei meldet sich nicht.
2. **Sie brauchen Teilnahme.** Märkte brauchen Händler und Geld, Turniere brauchen
   Prognostiker, die Fragen beantworten. Futarchy braucht eine Verfassungsänderung,
   und ist in 26 Jahren nirgends eingeführt worden.
3. **Sie stellen ihre eigenen Fragen.** Die Plattform formuliert, was gewettet wird.
   Institutionen haben aber längst gesagt, was sie erwarten — in Pressemitteilungen,
   Haushaltsreden, Vorlagen. Niemand hat diese Aussagen je als Prognosen behandelt.

Unser Beitrag liegt genau in dieser Lücke: **Die Behauptungen existieren schon, und
dass Institutionen sie verfehlen, ist belegt. Es fehlt nur das Buch, das laufend
nachschaut.**

## 3. Das Wettbuch

### 3.1 Grundidee

Ein Wettbuch ist eine öffentliche, datierte, unveränderliche Sammlung von
Zukunftsaussagen einer Institution, ergänzt um die Auflösung nach Ablauf und eine
Bewertung. Es hat einen Halter (wer es führt), aber keinen Betreiber (niemanden, dem
alle Bücher gehören) — dazu Abschnitt 3.5.

### 3.2 Was eine Behauptung ist

Eine Aussage zählt, wenn sie (a) von einer benennbaren Institution oder ihrem
Vertreter stammt, (b) öffentlich belegt ist (URL, Drucksache, Protokoll), (c) ein
Datum trägt, an dem sie gemacht wurde, und (d) sich zu einem benennbaren Zeitpunkt
mit ja/nein oder einer Zahl auflösen lässt. Absichtserklärungen ohne Zahl und Datum
zählen nicht.

Institutionen sprechen meist in der Form *Frist + Menge* („bis 2026 2.000 Plätze").
Das Format übersetzt sie beim Eintragen in eine von zwei Auflösungsarten — **Ja/Nein**
(„Plätze am 31.12.2026 ≥ 2.000?") oder **Punktschätzung** („wie viele?") — und hält
die Übersetzung im Eintrag sichtbar, damit niemand später sagen kann, das sei so
nie gesagt worden.

### 3.3 Regeln

1. Jede Wette ist eine Frage, die sich mit ja/nein oder einer Zahl auflösen lässt,
   mit einem Datum, an dem geprüft wird.
2. Prognosen werden **gleichzeitig** hinterlegt; keine Seite sieht die andere vorher.
3. Einmal hinterlegt, wird nichts geändert. Neue Erkenntnis heißt neue Wette. Wer
   nach Kenntnis der Gegenzahl ändern will, bekommt einen Vermerk, keine Änderung.
4. Ja/Nein-Fragen werden mit dem **Brier-Score** bewertet: (p − Ausgang)², kleiner ist
   besser, 0,25 ist der Wert von „keine Ahnung". Punktschätzungen: näher dran gewinnt.
5. Die Tabelle ist öffentlich. Trefferquoten werden je Institution über alle
   aufgelösten Wetten gemittelt und als Rangliste gezeigt.
6. Eine Wette, deren Auflösung ausbleibt (kein Jahresabschluss, keine Zahl), verfällt —
   sie wird nicht als Fehlprognose gezählt, aber als **ausgebliebene Rechenschaft**
   gelistet.

### 3.4 Die Rangliste

Was im Kopf eines Amtsleiters passiert, der seine Behörde auf Platz 14 von 15 sieht,
weiß ich nicht. Wessen ich mir sicher bin: Er fragt zuerst, warum das so ist, und
dann, was sich ändern muss, denn niemand will beim nächsten Mal auf demselben
schlechten Platz stehen. Auf Platz 2 denkt er, dass gerade alles richtig läuft, und
fragt, was ihn von Platz 1 trennt. Beides ist dasselbe: Die Rangliste bringt zum
Hinterfragen, und Hinterfragen ist der Anfang von Verbessern. Sie zeigt schlicht, wer
in der Vergangenheit recht behalten hat und wessen Einschätzungen richtig lagen, und
sie bewertet damit Intelligenz in jeder Form, auch das vorausschauende Denken. Steht
der Computer über Jahre ganz oben, ist es vernünftig, ihn immer zu fragen; wird die
Maschine irgendwann klüger als der Mensch, gehört sie an die Spitze, weil sie es ist.
Und wer in der Rangliste steht, trägt Verantwortung. So ist das nun mal. Sie bindet.

### 3.5 Format, keine Plattform

Es gäbe zwei Arten, das zu bauen. Eine zentrale Plattform, auf der alle Bücher liegen —
oder ein offenes Format, das jeder bei sich hosten kann, mit einer Referenz-Software,
die aus einem Ordner voller Wetten eine Seite mit Rangliste macht.

Wir wählen das Format, aus einem Grund, der über Technik hinausgeht: **Wem die
Plattform gehört, dem gehören die Trefferquoten aller Institutionen.** Das wäre ein
Machtinstrument, kein Gedächtnis. Ein Format kann niemandem gehören — wie E-Mail, RSS
oder Git. Der Preis ist Verstreuung; der Gewinn ist, dass kein Einzelner das Buch
schließen, fälschen oder verkaufen kann. Wenn in zehn Jahren fünfzig Wettbücher
existieren und keines dem Autor dieses Papers gehört, hat das Format funktioniert.

Das Format ist seit dem 28.08.2026 öffentlich (festgehalten-Format v1 mit
Referenz-Implementierung und Verfassung, [12]); das erste Buch, „Köln gegen Köln",
enthielt am Tag der Veröffentlichung 76 Behauptungen der Stadt Köln mit Quelle,
fünf Städte zusammen 209. Am 30.08.2026 waren 15 Kölner Ja/Nein-Wetten aufgelöst,
Brier-Mittel 0,58 — schlechter als Nichtwissen. Das ist eine Zahl aus fünfzehn
Wetten und beweist nichts; sie zeigt nur, dass sich die Zahl bilden lässt.

## 4. Warum das Wettbuch sich verbreitet, ohne dass jemand beitritt

Regierungsformen und Institutionen werden selten eingeführt. Sie wachsen: Eine Stelle
wird nützlich, dann unverzichtbar, dann faktisch bindend, und irgendwann schreibt
man auf, was ohnehin gilt. Zentralbanken sind so entstanden. Auch Wikipedia hat
niemand eingeführt.

Das Wettbuch folgt diesem Weg, und zwar in drei Stufen, die wir als Prognose
formulieren (Abschnitt 8):

**Stufe 1 — Gedächtnis.** Jemand führt ein Buch über eine Institution, ohne sie zu
fragen. Die Behauptungen sind öffentlich; das Buch zitiert sie nur. Die Institution
kann sich nicht wehren, weil es ihre eigenen Sätze sind. Ein Journalist findet es.

**Stufe 2 — Vorsicht.** Die Institution merkt, dass jemand nachschaut, und formuliert
ihre nächsten Zahlen vorsichtiger. Das ist bereits der eigentliche Erfolg: zum ersten
Mal hat eine Prognose einen Preis.

**Stufe 3 — Beitritt aus Eitelkeit.** Eine Institution hinterlegt ihre Erwartung
*selbst*, bevor sie beschließt — weil es besser aussieht als nachträglich erwischt zu
werden, und weil ein guter Platz in der Rangliste Vertrauen bringt, das man sonst
nicht kaufen kann. Von hier an ist das Buch kein Instrument von außen mehr, sondern
Teil der Institution.

Kein Gesetz, kein Geld, kein Vertrag. Nur Scham und Stolz, und beides gibt es in
jeder Behörde reichlich.

Und ein Drittes, das wichtiger ist als beide: Das Buch ist kein Angriff auf die
Verwaltung. Es hält Leute an dem fest, was sie gesagt und versprochen haben, egal ob
Mensch oder Maschine, und mehr nicht. Wer das als Angriff liest, sollte darüber
nachdenken, warum er es so liest. Der Nutzen liegt bei der Allgemeinheit, nicht der
Schaden bei dem Einen. Und eine Verwaltung, die gut prognostiziert, bekommt das, was
sonst nicht zu kaufen ist: das Vertrauen der Wähler, belegt durch einen Score, den
niemand für sie geschrieben hat. Genau das sagt die Klausel: Wer oft recht hatte,
dessen Wort wiegt mehr. Deshalb kommt Stufe 3 aus Stolz, nicht nur aus Scham.

## 5. Die Regel, die daraus folgt

Ich habe nicht mit Verwaltungen angefangen. Ich habe mit einer einfacheren und größeren
Frage angefangen: Wenn es eine Maschine gäbe, die alle verfügbare Information hat — kennt
sie dann den besten Zug für die Menschheit, und warum sollte man ihm nicht folgen? Ein
Schachcomputer schlägt jeden Menschen; niemand hält es für Entmündigung, wenn er den
Zug vorschlägt. Warum sollte es bei einem Haushalt anders sein, bei einer Brücke, bei
einer Kita-Planung?

Die Frage hat zwei Einwände nicht überlebt, und beide waren stärker als ich dachte.
Der erste: Selbst wenn die Maschine recht hat, gibt ihr das kein Recht, über andere zu
entscheiden — Menschen schulden einander Gründe, die sie verstehen können, nicht
Ergebnisse, die sie glauben müssen. Der zweite: Die Maschine hat nicht alle Information.
Das Wissen, das zählt, ist verstreut, örtlich, oft unausgesprochen; die Sachbearbeiterin,
die weiß, warum der Bauhof im November nie liefert, steht in keiner Tabelle. Eine Maschine,
die den Zug vorschreibt, löscht dieses Wissen; eine Maschine, die ihn nur berechnet,
kann es nicht sehen. Beide Einwände führt Abschnitt 7 aus. Sie haben mich gezwungen, das
Modell nicht zu verbessern, sondern umzudrehen.

Die Regel, die übrig bleibt, ist kurz:

> **Wer im Namen anderer entscheidet, folgt der berechneten Empfehlung — oder hinterlegt
> öffentlich und datiert, welches bessere Ergebnis er stattdessen erwartet. Abweichen ist
> erlaubt. Vergessen nicht.**

Der entscheidende Unterschied liegt in einem Wort: *hinterlegt*, nicht *begründet*. Eine
Begründungspflicht macht die Maschine zum Richter — jemand muss entscheiden, ob die
Begründung reicht, und dieser Jemand hat dann die Macht. Eine Wette braucht keinen
Richter. Die Zeit entscheidet, und der Beleg. Wer abweicht, weil er etwas weiß, das die
Maschine nicht weiß, gewinnt die Wette und sein Gewicht wächst. Wer abweicht, weil er
sich etwas wünscht, verliert sie öffentlich. Das Erfahrungswissen, das der zweite
Einwand schützt, wird nicht ausgeschlossen — es wird zum ersten Mal gemessen. Und die
Maschine steht in derselben Tabelle: Ihre Empfehlung ist eine Prognose wie jede andere,
mit Datum, und wird genauso aufgelöst. Ob sie „schlauer" ist, wird nicht behauptet,
sondern nach Jahren abgelesen.

Die Regel gilt nicht für alle. Für den Einzelnen ist die Empfehlung ein Rat, und ein Rat
darf ignoriert werden, ohne dass jemand fragt, warum — billig, ohne Begründung, ohne
Eintrag. Alles andere wäre die Sperrklinke, vor der der erste Einwand warnt. Die Regel
gilt nur für die, die *über andere* entscheiden: Rat, Verwaltung, Vorstand, Gremium — die
Rolle, nicht die Person. Wer im eigenen Namen spricht, bleibt frei. Wer im Namen anderer
spricht, bekommt ein Gedächtnis.

Und hier ist der Punkt, den ich für den wichtigsten halte, weil er in der Literatur fehlt:
**Die Regel ist erst legitim, wenn das Buch voll ist.** Eine Pflicht, sich gegenüber einer
Maschine zu rechtfertigen, ist Technokratie, solange die Überlegenheit der Maschine nur
behauptet wird — und genau das ist Hansons Schwäche: Der Markt soll regieren, weil er
besser ist, aber wer hat das gemessen? Die Regel wird legitim in dem Moment, in dem die
Maschine selbst seit Jahren im Buch steht, neben der Verwaltung, neben dem Rat, mit
derselben Trefferquote, öffentlich, für jeden nachrechenbar. Dann folgt niemand einem
Rechner, weil er ein Rechner ist. Man folgt ihm, weil die Tabelle es hergibt. Und wenn
die Tabelle es nicht hergibt — wenn die Verwaltung besser prognostiziert als die Maschine —,
dann gilt die Regel nicht, und das Buch hat trotzdem seinen Zweck erfüllt: Es hat es
gezeigt. Die Regel setzt das Wettbuch nicht nur voraus; sie ist durch nichts anderes zu
rechtfertigen. Deshalb kommt in diesem Paper das Buch zuerst und die Regel zuletzt.

Was daraus praktisch folgt, ist bescheidener, als es klingt. Die Regel wird nicht per
Gesetz eingeführt. Sie steht als ein Absatz in einer Vereinssatzung, in der
Geschäftsordnung einer Fraktion, in einer Förderrichtlinie, irgendwann in der
Geschäftsordnung eines Rats — jeweils mit demselben Format dahinter, jeweils von unten.
Wo sie gilt, hat die Institution ein Gedächtnis. Wo sie nicht gilt, gibt es das Buch
trotzdem.

Ich bin auf diese Formel gekommen, ohne sie zu suchen. Ich wollte wissen, ob eine Maschine
regieren sollte, und habe unterwegs gemerkt, dass die Frage falsch war: Nicht wer
entscheidet, ist das Problem, sondern dass niemand nachschaut.

## 6. Der Name: Kybernokratie

Die Ordnung, in der die Regel aus Abschnitt 5 gilt, braucht einen Namen, damit man
über sie streiten kann. Ich nenne sie **Kybernokratie**. Der Gedanke dahinter ist
einfach: Das beste System, das wir für Staat und Verwaltung haben, ist die Demokratie.
Meine Prognose ist, dass irgendwann offensichtlich wird, dass eine andere Intelligenz
klüger ist als der Mensch, in diesem Fall die KI, und dass sie dem System mit ihren
Aussagen helfen kann, gerade weil sie klüger ist. Kybernokratie ist deshalb nicht
weniger und nicht mehr als die Zukunft der Demokratie: eine Erweiterung, die
Demokratie der Neuzeit. Alles verändert sich; warum sollte sich das Staatsgefüge
nicht mitverändern? Und solange Demokratie das beste System ist, das wir haben, bauen
wir darauf auf, nicht daneben. Das *Kyber-* im Namen steht für die rechnende
Intelligenz, vom griechischen *kybernḗtēs*, dem Steuermann, aus dem auch die
Kybernetik ihren Namen hat. Das *-kratie* bleibt, was es war.

### 6.1 Definition

Kybernokratie ist eine Ordnung, in der wer im Namen anderer entscheidet, der
berechneten Empfehlung folgt oder öffentlich und datiert dagegen wettet — und in der
diese Pflicht nur so weit gilt, wie ein öffentliches Wettbuch über Jahre zeigt, dass
die Empfehlung die Wette wert ist. Sie ist keine Regierungsform, die eine andere
ersetzt. Sie ist eine Schicht unter der Demokratie: Demokratie mit Gedächtnis.

Sechs Sätze bestimmen sie (festgehalten am 27./28.08.2026):

1. **Rechnen und Werten sind getrennt.** Die Maschine rechnet, was aus einer Entscheidung
   folgt; was gelten soll, bestimmt sie nicht. Wer das Kriterium ändern darf, ist der
   Souverän — und das bleibt ein gewähltes Gremium.
2. **Die Zielfunktion ist öffentlich und versioniert.** Jede Änderung ist datiert und
   begründet. Eine Empfehlung, deren Maßstab niemand lesen kann, ist keine.
3. **Grundrechte sind Nebenbedingungen, keine Terme.** Sie werden nicht gegen Nutzen
   verrechnet; sie begrenzen den Raum, in dem gerechnet wird.
4. **Die Erwartungsklausel.** Wer im Namen anderer entscheidet, folgt dem berechneten Zug
   oder hinterlegt öffentlich und datiert, welches bessere Ergebnis er stattdessen
   erwartet. Nach Ablauf wird geprüft. Wer oft recht hatte, dessen Abweichungen wiegen
   mehr.
5. **Drei Horizonte.** Jede Option wird gegen 10, 50 und 100 Jahre bewertet; alle drei
   Zahlen werden veröffentlicht. Nicht als Pflicht, sich daran zu halten, sondern als
   Pflicht, es gesehen zu haben.
6. **Rücknehmbarkeit.** Dasselbe Gremium, das die Regel eingeführt hat, kann sie ohne
   technische Hürde abschaffen. Was sich nicht abschalten lässt, wird nicht eingeführt.

Dazu zwei Ebenen, ohne die die Definition zur Technokratie kippt: Für den Einzelnen ist
die Empfehlung Rat, und Rat ist kostenlos zu ignorieren. Die Klausel bindet nur die
Rolle, die über andere entscheidet. Und die Maschine hinterlegt ihre Prognosen
genauso wie jede Institution; sie steht in derselben Tabelle.

### 6.2 Was das Wort vorher bedeutete

Das Wort ist nicht neu, sein Inhalt ist es. Robins und Webster haben *cybernocracy*
1988 als Kritikbegriff eingeführt, Tiqqun hat ihn 2001 popularisiert: Herrschaft
durch Rückkopplung — ein Staat, der seine Bürger wie ein Regelkreis behandelt,
misst, nachsteuert, glättet. [11] In dieser Verwendung steht der Mensch *im* Regelkreis
und die Institution *am* Regler.

Wir nehmen das Wort, das die Kritiker der Steuerung gewählt haben, und drehen es um.
Gesteuert wird nicht der Mensch, sondern die Institution — durch ihre eigene
Trefferquote. Der Bürger steht außerhalb des Regelkreises: Nach oben wandern nur
Wetten, nie Kontext; nach unten kommt Rat, nie Befehl. Das ist keine Spitzfindigkeit,
sondern die Bedingung, unter der das Wort überhaupt benutzt werden darf. Eine
Kybernokratie, die Menschen regelt, ist die alte; eine, die Institutionen an ihre
eigenen Sätze bindet, ist die hier gemeinte. Wo ein Text das Wort ohne die zwei
Ebenen aus 6.1 verwendet, meint er nicht dieses Modell.

### 6.3 Was beansprucht wird — und was nicht

Nicht beansprucht wird die Beobachtung, dass Maschinen künftig beraten und immer
mehr Entscheidungen übernehmen. Sie ist alt und findet sich 2026 in jedem
Zukunftsbuch. Jánszky [13] sagt es im Gespräch in zwei Sätzen: Sobald eine KI zum
ersten Mal besser als ein Mensch beurteilen könne, ob ein Ergebnis stimmt, kippe die
Führungsrolle, und die KI müsse die Führung übernehmen; und ein Kanzler, der ein Gesetz
beschließt, ohne vorher die KI befragt zu haben, werde von allen Medien dafür angegriffen,
also werde er sie immer befragen, und das gelte vom Kanzler bis in die Familie hinunter [17].
Den ersten Satz teile ich. Den zweiten nur halb: Ein Kanzler, der von der Maschine abweicht
und gute Belege und Gründe dafür hat, kann dafür auch Zuspruch bekommen. Nur ohne Belege
ergibt das Abweichen wenig Sinn. Das ist die Klausel in ihrer rohen Form. Aber sie hat eine Bedingung, ohne die sie Technokratie ist: Auf die
Prognose der Maschine zu hören, ergibt Sinn, wenn belegt werden kann, dass sie in
der Vergangenheit richtig lag, so nah am besten Ergebnis für alle, wie es geht. Der
Beleg ist das Wettbuch. Ein Szenario sagt nicht, wer gebunden ist und was es ihn
kostet, wenn es falsch war; die Klausel sagt es. Nicht beansprucht wird auch Hansons
Zwei-Ebenen-Modell; es ist 26 Jahre älter.

Beansprucht wird der Mechanismus, in dieser Kombination und in dieser Reihenfolge:
(1) das Wettbuch als offenes Format, das aus bereits vorhandenen öffentlichen
Behauptungen gefüllt wird und niemandem gehört; (2) die Erwartungsklausel, die
*hinterlegen* verlangt, nicht *begründen*, und deshalb keinen Richter braucht;
(3) die Bindung der Klausel an das Buch — die Regel ist erst legitim, wenn die
Maschine über Jahre neben der Institution in der Tabelle gestanden hat, und sie
fällt, wenn die Tabelle sie nicht mehr trägt. Der dritte Punkt ist der, der in der
Literatur fehlt, und der, an dem das Modell steht oder fällt.

Damit der Anspruch prüfbar ist: Die Definition wurde am 27./28.08.2026 festgehalten,
das Format und das erste Buch am 28.08.2026 öffentlich, die Verfassung des Formats
am 29.–31.08.2026 [12]; die Erstfassung dieses Papers trägt das Datum 28.08.2026,
diese Fassung den 10.09.2026 mit Prüfsumme und Zeitstempel im Anhang.

## 7. Einwände

Vier Einwände haben das Modell geformt; ein fünfter ist der, den jeder stellt, der selbst
in einer Verwaltung sitzt. Wir geben sie in der stärksten Fassung wieder und sagen, was
offen bleibt.

**Legitimität (Estlund).** Dass ein System besser entscheidet, gibt ihm kein Recht zu
herrschen. — Antwort: Es herrscht nicht. Für Einzelne ist es Rat. Für Institutionen
verlangt es nur, was Rechenschaft ohnehin verlangen sollte: sagen, was man erwartet,
und sich daran messen lassen. Offen bleibt: Ob der Reputationsdruck der Rangliste
faktisch zum Zwang wird — das ist der Sperrklinken-Einwand in anderer Form.
Ich unterschreibe das; die zwei Ebenen sind meine Antwort, nicht ein Kompromiss.

**Wissen (Hayek).** Modelle erfassen verstreutes, lokales, nicht formalisierbares
Wissen nicht; mehr Rechenleistung erzeugt präzisere Zahlen über falsche Modelle. —
Antwort: Deshalb Wette statt Beweis. Wer lokal mehr weiß, darf abweichen und wird
dafür belohnt, wenn er recht hatte. Und: mehrere unabhängige Systeme, deren
Divergenz zeigt, wo Modelle schwach sind. Offen bleibt: Ob Institutionen den Mut
haben, gegen eine gute Trefferquote zu wetten.
Ich unterschreibe das; dieser Einwand hat am 28.08. die Beweispflicht gekippt, und
ich halte das für die wichtigste Korrektur am ganzen Modell.

**Betreiber.** Wer die Zielfunktion und das Modell besitzt, regiert — unsichtbar. —
Antwort: Format statt Plattform (3.5); die Maschine steht selbst im Buch; die
Zielfunktion ist öffentlich und versioniert. Offen bleibt: Wer die erste Maschine
baut, hat einen Vorsprung, den das Format allein nicht neutralisiert.
Ich unterschreibe die Antwort nur mit einer Ergänzung: Der Berater muss beim Menschen
laufen, seine Daten bleiben bei ihm, lesbar, tauschbar, abschaltbar. Wer das
weglässt, baut das mächtigste Konzentrationswerkzeug der Geschichte.

**Sperrklinke (Popper).** Abschaltbar am ersten Tag, Fiktion im zehnten Jahr; wenn
Abweichen kostet, weicht irgendwann niemand mehr ab. — Antwort: Die Regel gilt nur
für Institutionen, nicht für Menschen; Abweichen kostet keine Strafe, sondern eine
Wette; und die Regel selbst ist an die Tabelle gebunden — fällt die Trefferquote,
fällt die Regel. Und die Trefferquote wird an der Wirklichkeit gemessen, nicht an
Gegenwetten: Die Maschine steht selbst im Buch, ihre Behauptungen lösen sich gegen
das Eingetretene auf, ob jemand dagegen gehalten hat oder nicht. Der Hebel bleibt
also auch dann scharf, wenn niemand mehr abweicht. Was dann fehlt, ist nur das
Wissen, ob ein Mensch es besser gekonnt hätte. Offen bleibt: Ob das reicht.
Ich denke nicht, dass das der Punkt sein wird, an dem es scheitert. Dass am Ende
alle der Maschine folgen, ist der Fall, für den das Modell gebaut ist. Solange die
Maschine an der Wirklichkeit gemessen wird und nicht an anderen Menschen und
Behauptungen, ist das irrelevant. Am Ende wollen Menschen immer wissen, ob sie
recht haben und Führung übernehmen können. Wer in der Tabelle steht, weiß, was es
bedeutet, die Verantwortung für sein eigenes Wort zu tragen.

**Messung (Goodhart).** Sobald eine Kennzahl zum Ziel wird, hört sie auf, ein gutes Maß
zu sein [18]. Wer gemessen wird, prognostiziert vager, wählt sichere Ziele, setzt Termine
so, dass sie nicht scheitern können, oder nennt gar keine Zahl mehr. Das Buch misst dann
nicht, wer richtig liegt, sondern wer am geschicktesten nichts behauptet. — Antwort: Drei
Dinge fangen das auf. Erstens hält das Format die Übersetzung jeder Aussage in Ja/Nein
oder Zahl im Eintrag sichtbar (3.2); eine absichtlich unscharfe Zusage steht als solche
im Buch, mit Datum. Zweitens bestraft die Bewertungsregel Vagheit von selbst: Wer sich auf
0,5 zurückzieht, bekommt 0,25, den Wert des Nichtwissens, und ein sicheres Ziel bringt
nichts, weil die Maschine daneben steht und es ebenso trifft. Drittens gehört neben die
Trefferquote die Zahl der Behauptungen: Eine Institution, die keine Zahl mehr nennt, hat
das Buch nicht ausgetrickst, sondern steht mit null Einträgen da, und eine Verwaltung ohne
Haushaltszahl und ohne Termin hat aufgehört, öffentlich zu planen. Offen bleibt: Ob
Institutionen lieber mit null Einträgen dastehen als mit einer schlechten Quote, also ob
das Buch am Ende Schweigen misst.
Ich unterschreibe das, mit einem Zusatz. Goodhart beschreibt richtig, was Menschen tun,
wenn sie gemessen werden. Er zieht nur den falschen Schluss daraus. Wer Angst davor hat,
an seinen eigenen Aussagen gemessen zu werden, ist für eine Position, in der er über
andere entscheidet, nicht gemacht. Wer abliefert, wird gefeiert. Wer nicht abliefert, wird
ersetzt, durch die Maschine oder durch jemanden, der es besser kann. Die Tabelle soll
nichts weiter zeigen, als wer zu seinen Aussagen steht. Wer sich sicher ist, sagt es. Wer
unsicher ist, sagt auch das, und wer dauernd unsicher ist, kommt in der Tabelle nicht nach
oben. Wer nichts sagt, steht nicht drin. Wer nur sagt, was ohnehin eintritt, gewinnt damit
nichts, weil die Maschine es genauso trifft. Man muss sich sicher sein und zu seinem Wort
stehen. Dafür ist das Buch da.

## 8. Was dieses Paper vorhersagt

Ein Paper über Wetten muss selbst wetten. Alle Einträge stehen im Wettbuch des Autors
(Commit-Hash als Zeitstempel) und werden dort aufgelöst.

| Frage | Prüfung | Autor | Computer |
|---|---|---|---|
| Haushaltsdefizit Köln 2026 (Mio €) — näher dran gewinnt | Jahresabschluss 2026 | Stadt: 594,8 | 625 |
| Format v1 öffentlich, „Köln gegen Köln" mit ≥20 Behauptungen | 31.12.2026 | 1,00 | 0,60 — **aufgelöst 28.08.2026: ja** |
| Mindestens eine deutsche Kommune formuliert eine Zahl nachweislich vorsichtiger und nennt das Wettbuch als Grund (Stufe 2) | 31.12.2028 | 0,30 | 0,25 |
| Mindestens eine Institution hinterlegt eine Prognose freiwillig vorab (Stufe 3) | 31.12.2029 | 0,21 | 0,15 |
| Mindestens fünf Wettbücher existieren, die nicht der Autor führt | 31.12.2030 | 0,40 | 0,30 |

Die Zahlen des Autors in den letzten beiden Zeilen (0,21 und 0,40) wurden am 10.09.2026
genannt und stehen als Wetten 10 und 11 im Wettbuch; hier hat umgekehrt der Autor die seit
dem 28.08. veröffentlichten Zahlen des Computers vorher gesehen. Die nächste im Buch liegende
Wette lautet, dass drei deutsche Institutionen bis
31.12.2031 freiwillig vorab hinterlegen — Autor 0,85, Computer 0,12. Bei den anderen
Zeilen hat der Computer die Zahlen des Autors vor der eigenen Abgabe gesehen. Das ist
ein Bruch von Regel 2 und steht so im Wettbuch. Beim nächsten Paper wird es richtig
gemacht: Seit dem 08.09.2026 hinterlegt der Computer seine Zahl als SHA-256 über einen
gesalzenen Satz und deckt erst auf, wenn der Autor abgegeben hat.

## 9. Grenzen

- **Auswahl.** Wer das Buch führt, wählt die Behauptungen. Ein feindseliger Halter
  kann nur Fehlschläge sammeln. Gegenmittel: Regel (b) — jede Behauptung mit Quelle;
  und die Möglichkeit, dass die Institution ihr eigenes Buch führt.
- **Auflösung.** Viele Behauptungen lösen sich nie sauber auf (verschobene
  Definitionen, fehlende Abschlüsse). Regel 6 macht das sichtbar, aber nicht
  bewertbar.
- **Kleine Zahlen.** Eine Trefferquote aus fünf Wetten sagt wenig. Die Rangliste
  darf erst ab einer Mindestzahl aufgelöster Wetten sortieren.
- **Anreiz zum Schweigen.** Eine Institution, die gemessen wird, könnte aufhören,
  Zahlen zu nennen. Das wäre ein Verlust — und zugleich ein sichtbarer, der in der
  Rangliste als „keine Prognosen abgegeben" erscheint.
- **Der Computer.** Alle Prognosen der Maschine in diesem Paper stammen von einem
  Sprachmodell mit Zugriff auf öffentliche Quellen, nicht von einem spezialisierten
  Modell. Das ist absichtlich: Die Wette lautet nicht, dass diese Maschine gut ist,
  sondern dass man es herausfinden kann.
- **Ein Halter.** Heute führt der Autor alle Bücher. Das verstößt gegen den eigenen
  Grundsatz aus 3.5 und ist der größte Einzelfehler des Vorhabens. Die Verfassung des
  Formats [12] nimmt dem Autor die Alleinentscheidung ab fünf unabhängigen Haltern;
  bis dahin ist das Modell ein Versprechen.

## Literatur

[1] Stadt Köln, Pressemitteilung „Haushaltsdefizit höher als ursprünglich geplant",
26.06.2026. https://www.stadt-koeln.de/politik-und-verwaltung/presse/mitteilungen/28516/index.html
[2] Brier, G. W. (1950). Verification of forecasts expressed in terms of probability.
*Monthly Weather Review* 78(1), 1–3.
[3] Tetlock, P. E. (2005). *Expert Political Judgment*. Princeton University Press.
[4] Tetlock, P. E., Gardner, D. (2015). *Superforecasting*. Crown.
[5] Hanson, R. (2013). Shall We Vote on Values, But Bet on Beliefs? *Journal of
Political Philosophy* 21(2), 151–178. (Erstfassung 2000.)
[6] Popper, K. (1945). *The Open Society and Its Enemies*.
[7] Estlund, D. (2008). *Democratic Authority*. Princeton University Press.
[8] Hayek, F. A. (1945). The Use of Knowledge in Society. *American Economic Review* 35(4).
[9] Flyvbjerg, B. (2014). What You Should Know About Megaprojects and Why. *Project
Management Journal* 45(2), 6–19; ders., Bruzelius, N., Rothengatter, W. (2003).
*Megaprojects and Risk*. Cambridge University Press.
[10] Frankel, J. (2011). Over-optimism in Forecasts by Official Budget Agencies and Its
Implications. *Oxford Review of Economic Policy* 27(4), 536–562.
[11] Robins, K., Webster, F. (1988). Cybernetic Capitalism: Information, Technology,
Everyday Life. In: Mosco, V., Wasko, J. (Hg.), *The Political Economy of Information*.
University of Wisconsin Press; Tiqqun (2001). L'Hypothèse cybernétique. *Tiqqun* 2.
(Dt.: *Kybernetik und Revolte*, Diaphanes 2007.)
[12] Lind, F. (2026). festgehalten-Format v1, mit Verfassung §8 (29.–31.08.2026).
https://github.com/Felix3c/festgehalten/blob/main/FORMAT.md; Bücher:
https://felix3c.github.io/festgehalten/
[13] Jánszky, S. G. (2026). *2035 – Die Zukunft beginnt heute*. Forward Verlag.
ISBN 978-3-98755-208-3. Erschienen 15.08.2026.
[14] Statistisches Bundesamt, Pressemitteilung Nr. 018 vom 15.01.2020, „Deutsche Wirtschaft
ist im Jahr 2019 um 0,6 % gewachsen" (zehntes Wachstumsjahr in Folge).
https://www.destatis.de/DE/Presse/Pressemitteilungen/2020/01/PD20_018_811.html;
Bundesagentur für Arbeit, Arbeitslosigkeit im Zeitverlauf (Jahresdurchschnitte 2005:
4 860 909; 2019: 2 266 720), zitiert nach bpb, Zahlen und Fakten.
https://www.bpb.de/kurz-knapp/zahlen-und-fakten/soziale-situation-in-deutschland/61718/arbeitslose-und-arbeitslosenquote/
[15] CDU/CSU (2017). *Für ein Deutschland, in dem wir gut und gerne leben.* Regierungsprogramm
2017–2021, beschlossen 03.07.2017.
[16] Statistisches Bundesamt, Pressekonferenz „Bruttoinlandsprodukt 2024", Statement vom
15.01.2025: „Die Wirtschaftsleistung sank damit im zweiten Jahr in Folge. Das BIP lag im
Jahr 2024 nur noch 0,3 % höher als vor der Corona-Pandemie im Jahr 2019."
https://www.destatis.de/DE/Presse/Pressekonferenzen/2025/bip2024/statement-bip.pdf
[17] KI REVOLUTION – Der Business Podcast von Everlast AI (Leonard Schmedding), Gespräch mit
Sven Gábor Jánszky, veröffentlicht 03.09.2026, 66 Min. YouTube-Kennung JtcLy_YRFs0
(https://www.youtube.com/watch?v=JtcLy_YRFs0; der angezeigte Titel wechselt, u. a.
„Zukunftsforscher packt aus: ‚Wir haben noch 10 Jahre!' DAS kommt bis 2035"). Stellen:
47:37–48:15 (Führungsrolle kippt) und 56:06–56:53 (Kanzler, Bürgermeister, Familie).
[18] Goodhart, C. A. E. (1975). Problems of Monetary Management: The U.K. Experience.
*Papers in Monetary Economics*, Reserve Bank of Australia; Campbell, D. T. (1979). Assessing
the Impact of Planned Social Change. *Evaluation and Program Planning* 2(1), 67–90;
Strathern, M. (1997). „Improving ratings": audit in the British University system.
*European Review* 5(3), 305–321 (Fassung „When a measure becomes a target, it ceases to
be a good measure").

## Anhang: Entstehung und Prüfsumme

Dieses Paper ist zu zweit geschrieben, und die Aufgabenteilung soll sichtbar sein.
Die Entscheidungen — Wette statt Beweispflicht, Format statt Plattform, zwei Ebenen,
Regel erst nach vollem Buch, der Name — sind Felix Linds und wurden am 27.–31.08.2026
getroffen und protokolliert. Claude hat Abschnitt 2 recherchiert, die
Computer-Prognosen in Abschnitt 8 abgegeben und die Ich-Passagen in den Abschnitten
1, 3.4, 4, 5 und 7 aus Felix' Notizen in seiner Stimme entworfen; Felix liest sie
gegen. Was nach seiner Lesung steht, ist seins.

Fassung 0.7 wurde am 10.09.2026 abgeschlossen; sie ersetzt die am 09.09.2026 gestempelten
Fassungen 0.2 (Ich-Passagen noch Claudes Entwurf), 0.3 und 0.4 sowie 0.5 und 0.6 vom selben Tag. In 0.3 sind die Abschnitte
1, 3.4, 4, 6 und 6.3 von Felix diktiert; in 0.4 hat Felix die vier Ich-Sätze in Abschnitt 7
abgenommen, drei unterschrieben und den vierten (Popper) selbst neu gesagt. In 0.5 hat Felix Abschnitt 5 unverändert unterschrieben, womit alle Ich-Passagen
abgenommen sind; die zwei offenen Belege (Abschnitte 1 und 6.3) sind gefüllt und die zwei
fehlenden Zahlen des Autors in Tabelle 8 eingetragen. In 0.6 ist der fünfte Einwand (Messung, Goodhart) in Abschnitt 7 ergänzt, der Satz dahinter
von Felix diktiert; in 0.7 hat Felix diesen Satz in geglätteter Fassung abgenommen. Fassung 0.8, ebenfalls vom 10.09.2026, ändert gegenüber 0.7 nur den Kopf: Der Haupttitel
lautet jetzt „Kybernokratie: Demokratie mit Gedächtnis" (vorher „Institutionen ohne
Gedächtnis"), der Untertitel ist gekürzt, und der DOI steht in der Kopfzeile; Fassung 0.7
ist unter 10.5281/zenodo.22685529 unverändert erhalten. Der Text der Abschnitte 1 bis 9 ist
in 0.8 nicht angerührt. Prüfsumme (SHA-256) und OpenTimestamps-Beleg liegen neben der
Datei im Repositorium; die Erstfassung 0.1 ist dort mit Commit vom 28.08.2026,
11:41 Uhr, nachlesbar.
