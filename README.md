# PythonProjekte

Das Programm erkennt bis jetzt aus einem zusammenhängenden text ohne umbrüche und tabs namen und entfernt diese.
(Das Umbrüche und tabs problem könnte man eventuell durch raw input lösen da \n immernoch als "enter" im input() angenommen wird.)

Außerdem zählt es von dem Text ohne die Namen die Häufigkeit der jeweiligen Buchstaben und Zeichen und speichert diese bis jetzt in einem dictionary.



Nächste Schritte sind:

   Scraping und Import der Texte
    
   Speichern des Dictionarys als .csv mit 3. Spalte der relativen Häufigkeit (Wichtig, das bestehende File muss ergänzt nicht     
   überschrieben werden)
   
   2. Programm, welches den frontend teil übernimmt (Sprich die tatsächliche Sprachenerkennung durch bezug auf die .csv Prozente)

Update 27.09:
   
   Das Programm speichert nun alle neuen daten aus dem gegebenen text in einem .csv file (was leider noch nicht so gut von menschen gelesen werden kann weil excel behindert ist) ohne die vorherigen zu überschreiben sondern addiert die geänderten variablen auf
