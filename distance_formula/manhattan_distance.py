import numpy as np

"""Die Manhattan-Distanz misst die Summe der absoluten Differenzen zwischen den Koordinaten der Punkte. Sie wird oft 
in Situationen eingesetzt, in denen der Weg, den man durch Straßen in einer Stadt zurücklegt, eine bessere Analogie 
darstellt als die direkte Entfernung.

Anwendungsbeispiele:

Stadtplanung: Wenn du die Entfernung oder den Aufwand, um von einem Ort zum anderen zu gelangen, in städtischen 
Umgebungen berechnen möchtest, ist die Manhattan-Distanz sinnvoll.

Genetik: In der Genetik werden oft Abstände zwischen genetischen Merkmalen gemessen, und die Manhattan-Distanz kann 
dabei hilfreich sein.

Textverarbeitung: Bei der Analyse von Textdokumenten können Wortfrequenzen oder andere Merkmale mit der 
Manhattan-Distanz verglichen werden."""


def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))


point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
distance = manhattan_distance(point1, point2)
print("Manhattan-Distanz:", distance)
