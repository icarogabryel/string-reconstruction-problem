from string_composition import stringComposition

def main():
    k = 3
    text = 'TATGGGGTGC'
    result = stringComposition(k, text)
    
    for kmer in result:
        print(kmer)

if __name__ == '__main__':
    main()
