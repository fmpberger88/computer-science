"""Wann einzusetzen: Die Hamming-Distanz wird oft in Bereichen eingesetzt, in denen binäre Daten oder Zeichenketten
mit fester Länge verglichen werden müssen. Beispiele hierfür sind Fehlererkennung in Kommunikationssystemen,
DNA-Sequenzvergleiche oder Überprüfung von Codewörtern in Speichersystemen.

Bitte beachte, dass die Hamming-Distanz nur für Zeichenketten gleicher Länge definiert ist. Sie ist weniger geeignet
für den Vergleich von Vektoren unterschiedlicher Dimensionen oder für die Messung von Unterschieden in
kontinuierlichen Daten.

"""


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Die Zeichenkennte müssen die gleiche Länge haben")

    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance


string1 = "karolin"
string2 = "kathrin"
distance = hamming_distance(string1, string2)
print("Hamming-Distanz:", distance)
