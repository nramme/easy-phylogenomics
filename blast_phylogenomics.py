#!/usr/bin/env python3

import re, os, subprocess, sys, argparse

### This script prepares your sequences for mutiple alignment.

### Functions ###

def blast_search_with_diamond():
	for proteome in os.listdir(proteomes_dir):
		if proteome.endswith(".faa") or proteome.endswith(".fasta") or proteome.endswith(".fa"):
			makeblast_db = ['makeblastdb','-in', proteomes_dir + proteome,'-dbtype', 'prot','-out', "DB_dir/" + proteome]
			subprocess.call(makeblast_db, cwd=current_directory)
			if args.evalue:
				blast_diamond = ['blastp', '-query',infile, '-db', "DB_dir/" + proteome, '-evalue', evalue, '-culling_limit', '1', '-outfmt', '6', '-out', proteome + '.6.blastp']
			else:
				blast_diamond = ['blastp', '-query',infile, '-db', "DB_dir/" + proteome, '-evalue', '1e-10', '-culling_limit', '1', '-outfmt', '6', '-out', proteome + '.6.blastp']
			subprocess.call(blast_diamond, cwd=current_directory)

def extract_blast_hits():
	for blast in os.listdir(current_directory):
		if blast.endswith(".blastp"):
			blast_files = blast 
			new_blast_files = blast + '.fasta'
			for proteome in os.listdir(proteomes_dir):
				if proteome.endswith(".fasta") or proteome.endswith(".faa") or proteome.endswith(".fa"):
					proteome_files = proteomes_dir + proteome
					if proteome.replace(".fasta", "") == blast.replace(".fasta.6.blastp", "") or proteome.replace(".faa", "") == blast.replace(".faa.6.blastp", "") or proteome.replace(".fa", "") == blast.replace(".fa.6.blastp", ""):
						with open(blast_files, 'r') as blast_output, open(proteome_files, 'r') as proteome_search, open(new_blast_files, 'w+') as extracted_seqs:
							while True:
								blast_lines = blast_output.readline()
								if blast_lines:
									blast_seqs = re.findall(protein_name_in_blast, blast_lines,flags=re.M)[0]
									while True:
										proteome_line = proteome_search.readline()
										if proteome_line:
											proteome_seqs = re.search(protein_name_in_proteome, proteome_line)
											if proteome_seqs:
												aux = 0										
												if blast_seqs == proteome_seqs.group(0).replace(">", ""): # The sequence name in the blast output has to be the same in the fasta containing protein sequences
													aux = 1
											if aux: 
												extracted_seqs.write(proteome_line)
										else: break
								else: break
								proteome_search.seek(0)

def concatenate_seqs():
	for fasta in os.listdir(current_directory):
		if fasta.endswith(".6.blastp.fasta"):
			fasta_file = fasta
			new_blast_files = fasta.replace(".6.blastp.fasta", "") + '.concatenated'
			header = ">" + fasta.replace(".6.blastp.fasta", "") + "\n"
			with open(fasta_file, 'r') as blast_output, open(new_blast_files, 'w+') as concatenate_seqs:
				concatenate_seqs.write(header)
				while True:
					fasta_lines = blast_output.readline()
					if fasta_lines:
						proteins_seqs = re.search(protein_seq_in_proteome, fasta_lines)
						if proteins_seqs:
							seq = proteins_seqs.group()
							concatenate_seqs.write(seq)
					else: break

def merge_concatenated_seqs():
	with open('phylo_seqs.fasta', 'w') as outfile:
		for conc in os.listdir(current_directory):
			if conc.endswith(".concatenated"):
				conc_file = conc
				with open(conc_file) as infile:
					outfile.write(infile.read())
				outfile.write("\n")

def remove_concatenated_seqs():
	for conc in os.listdir(current_directory):
		if conc.endswith(".concatenated"):
			os.remove(conc)

### Regex ###

protein_name_in_blast = r"^\S*\s(\S*)"
protein_seq_in_proteome = r"(?!>)^[^\s]+" # selects only protein sequence
protein_name_in_proteome = r"(?!\w)^[^\s]+" # selects protein name with '>'

### Command line arguments ###

if len(sys.argv) <= 1:
	sys.argv.append("-h")

if sys.argv[1] in ["-h", "--help", "getopt", "usage", "-help", "help"]:
	sys.exit('''
USAGE:  blast_phylogenomics.py [ options ]
Perform BLAST searches in multiple proteomes.
OPTIONS:
	-q|--proteins_query	The protein sequences in FASTA format you want to search in other proteomes.
	-p|--proteomes_dir	Directory containing proteome files in FASTA format.
	-e|--evalue		E-value for BLAST search (default: 1e-10)
''')


### Parser ###

p = argparse.ArgumentParser()
p.add_argument("-q", "--proteins_query", required=True)
p.add_argument("-p", "--proteomes_dir", required=True)
p.add_argument("-e", "--evalue")

args = p.parse_args()

### Code ###

if __name__ == "__main__":
	infile = args.proteins_query
	evalue = args.evalue
	proteomes_dir = args.proteomes_dir
	current_directory = os.getcwd()
	DB_dir = os.path.join(current_directory)

blast_search_with_diamond()
extract_blast_hits()
concatenate_seqs()
merge_concatenated_seqs()
remove_concatenated_seqs()


