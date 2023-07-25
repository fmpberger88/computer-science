# Diese Lösung stellt eine naive rekursive Lösung vor

"""
Imagine that you’re a thief breaking into a house. There are so many valuables to steal
- diamonds, gold, jewelry, and more! But remember, you’re just one person who can only carry so much.
Each item has a weight and value, and your goal is to maximize the total value of items
while remaining within the weight limit of your knapsack.
This is called the knapsack problem and is commonly used in programming interviews.
"""


def recursive_knapsack(weight_cap, weights, values, i):
    # base case
    if weights == 0 or i == 0:
        return 0
    # recursive call
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)
    return max(include_item, exclude_item)


# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(recursive_knapsack(weight_cap, weights, values, len(weights)))

"""Die vorgestellte Lösung verwendet eine naive rekursive Herangehensweise, um das Knapsack-Problem zu lösen. Der 
Code sieht im Allgemeinen korrekt aus, aber ich werde es nochmal Schritt für Schritt durchgehen und die 
Funktionsweise erläutern.

Der Code verwendet Rekursion, um die maximale Wertsumme für den Rucksack zu berechnen, wenn die Gewichtskapazität
 weight_cap gegeben ist und wir i Gegenstände zur Verfügung haben.

Hier ist die Funktionsweise des Codes:
Das Rucksackproblem wird schrittweise reduziert, indem entschieden wird, ob der i-te 
Gegenstand in den Rucksack aufgenommen wird oder nicht.

Wenn weights == 0 oder i == 0, gibt es keine Gegenstände oder die Gewichtskapazität des Rucksacks ist 0.
In diesem Fall wird 0 zurückgegeben, da keine Gegenstände ausgewählt werden können.

Wenn das Gewicht des i-ten Gegenstands größer ist als die verbleibende Gewichtskapazität weight_cap,
können wir diesen Gegenstand nicht in den Rucksack aufnehmen, da er die Gewichtsbeschränkung überschreiten würde.
In diesem Fall wird der Rekursionsaufruf durchgeführt, um die maximale Wertsumme ohne diesen Gegenstand zu berechnen.

Wenn der i-te Gegenstand in den Rucksack passt, 
wird der Rekursionsaufruf durchgeführt, um zwei Möglichkeiten zu betrachten:

include_item: Der i-te Gegenstand wird in den Rucksack aufgenommen, und die Gewichtskapazität weight_cap wird
um das Gewicht dieses Gegenstands reduziert. Der maximale Wert wird mit diesem Gegenstand aktualisiert.
 
exclude_item: Der i-te Gegenstand wird nicht in den Rucksack aufgenommen. 
Der Rekursionsaufruf wird durchgeführt, um die maximale Wertsumme ohne diesen Gegenstand zu berechnen.
Schließlich wird der max(include_item, exclude_item) zurückgegeben, da dies der Wert ist, 
der den maximalen Wert repräsentiert, den wir für den Rucksack erreichen können, 
wenn wir i Gegenstände und eine Gewichtskapazität von weight_cap haben.
"""
