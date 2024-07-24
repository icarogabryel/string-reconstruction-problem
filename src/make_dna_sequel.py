import random


def makeDNA(length):
    dna = ""

    for _ in range(length):
        dna += random.choice("ACGT")

    return dna

if __name__ == "__main__":
    with open('../test/100k_dna_sequel.txt', 'w') as file:
        file.write(makeDNA(100000))
