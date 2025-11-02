from collections import defaultdict


def letter_frequency_normal(sentence):
    frequencies = {}  # Diccionario normal
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)  # Verifica si la clave existe
        frequencies[letter] = frequency + 1
    return frequencies


def letter_frequency_default(sentence):
    frequencies = defaultdict(int)  # defaultdict con valor por defecto int(0)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies  # defaultdict se puede indexar igual que un diccionario normal


if __name__ == "__main__":
    print(letter_frequency_normal("hola mundo"))
    print(letter_frequency_default("hola mundo"))
