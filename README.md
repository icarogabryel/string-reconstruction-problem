# String Reconstruction Problem

## Introduction

This repository have the implementation of a string reconstructor using Bruijn graphs and eulerian path. This problem is very important in bioinformatics, because it is used to reconstruct the DNA sequence from a set of k-mers.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Usage

To run the program, you need to have python installed in your machine. After that, you can run the `main.py` file using the following command:

```bash
python main.py
```

When you run the program, you will be asked to enter the input file name with the k-mers. The k-mers must be in a `.txt` file, where have only one line with the k-mers separated by a comma. Then, the program will ask you to enter the output file name where the reconstructed string will be saved. After that, the program will save the reconstructed string.

You can use the file `kmers.txt` in test folder to test the program.

## Algorithm

This implementation creates a Bruijn graph from the k-mers and then finds the eulerian path in the graph. The eulerian path show how to reconstructed string.

When the program reads the k-mers, it creates the Brujin graph as a incidence list. It creates a dictionary where the key is the prefix of the k-mer and the value is a list with the suffixes of the k-mer. After that, the program finds the eulerian path using Hierholzer's algorithm. With the eulerian path, the program reconstructs the string.
