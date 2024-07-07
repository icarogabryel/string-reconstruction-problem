class Kmer:
    def __init__(self, kmer):
        self.kmer = kmer
        self.prefix = kmer[:-1]
        self.suffix = kmer[1:]

    def __repr__(self):
        return self.kmer
    
    def __lt__(self, other):
        return self.kmer < other.kmer


def stringComposition(k, text):
    kmersList = []

    for i in range(len(text) - k + 1):
        kmer = Kmer(text[i:i+k])
        kmersList.append(kmer)
    
    return sorted(kmersList)
