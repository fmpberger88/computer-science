import numpy as np

"""
Euklidische Distanz: Die euklidische Distanz misst den direkten Abstand zwischen zwei Punkten im Raum. Sie wird 
oft verwendet, wenn die absoluten Abstände zwischen den Merkmalen wichtig sind und die Daten in einem 
kontinuierlichen Raum repräsentiert werden.

Anwendungsbeispiele:

Bildverarbeitung: Wenn du Bildmerkmale miteinander vergleichen möchtest, z. B. die Farbwerte von Pixeln in Bildern, 
ist die euklidische Distanz nützlich.

Empfehlungssysteme: Bei der Berechnung von Ähnlichkeiten zwischen Benutzern oder Produkten können die euklidische 
Distanzmetrik und ihre Varianten verwendet werden.

Koordinatenbasierte Daten: In GIS (Geographic Information Systems) werden oft räumliche Daten analysiert, 
bei denen die euklidische Distanz eine passende Metrik ist.
"""


def euclidean_distance(x, y):
    return np.sqrt(np.sum(x - y) ** 2)


point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
distance = euclidean_distance(point1, point2)
print("Euklidische Distanz:", distance)
