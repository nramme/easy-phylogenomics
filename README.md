# easy-phylogenomics
This repository contains scripts that facilitate the manipulation of large amounts of data for phylogenomic analysis.

# Requirements #

- [Python >= 3](https://www.python.org/downloads/)
- [DIAMOND](https://github.com/bbuchfink/diamond) 


USAGE:  blast_phylogenomics.py [ options ]\
Generate a file with concatenated protein sequences for mutiple sequence alignment.
  
OPTIONS:
  -q |--proteins_query	Reference protein sequences in FASTA format.\
  -p |--proteomes_dir	Directory containing protein sequences files in FASTA format.\
  -e |--evalue		E-value for BLAST search (default: 1e-10).

```bash
blast_phylogenomics.py  \
	-q conserved_proteins.fasta \
	-p /home/Proteomes/ \
	-e 1e-50
```
