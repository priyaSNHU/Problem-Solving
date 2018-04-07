# HACKERRANK PROBLEM LINK: https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

#!/bin/python3

import sys

def steadyGene(gene):
    # Complete this function
    gene_char = {'A': 0, 'C': 0, 'T': 0, 'G': 0 }
    n = len(gene)
    for i in range(n):
        gene_char[gene[i]] += 1
    # check count of each char 
    for k,v in gene_char.items():
        if v > n/4:
            gene_char[k] = int(gene_char[k] - n/4)
        else:
            gene_char[k] = 0
    #check if given string is stable
    char_count = 0
    for v in gene_char.values():
        char_count += v
    if char_count == 0:
        return 0

    # check for sub string in string
    min_len = len(gene)
    start = 0
    stop = 0
    sub_gene_char = {'A': 0, 'C': 0, 'T': 0, 'G': 0 }

    while stop < len(gene):
        if all([sub_gene_char[k] >= gene_char[k] for k,v in gene_char.items()]):
            current_length = stop- start
            if current_length < min_len:
                min_len = current_length
            sub_gene_char[gene[start]] -= 1
            start += 1
        else:
            sub_gene_char[gene[stop]] += 1
            stop += 1
    return min_len

if __name__ == "__main__":
    n = int(input().strip())
    gene = input().strip()
    result = steadyGene(gene)
    print(result)
