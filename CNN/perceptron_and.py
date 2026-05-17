# Perceptron tres simple pour reproduire la porte logique AND.


def activation(somme):
    if somme >= 0:
        return 1
    return 0


def perceptron(x1, x2):
    poids1 = 1
    poids2 = 1
    biais = -1.5

    somme = x1 * poids1 + x2 * poids2 + biais
    return activation(somme)


tests = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
]

for x1, x2 in tests:
    resultat = perceptron(x1, x2)
    print(x1, "AND", x2, "=", resultat)
