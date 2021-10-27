import re, os, sys, argparse

### Command line arguments ###

if len(sys.argv) <= 1:
	sys.argv.append("-h")

if sys.argv[1] in ["-h", "--help", "getopt", "usage", "-help", "help"]:
	sys.exit('''
USAGE:  extract_blast_hits.py [ options ]
Extract the sequences from blastp output.
    -p|--proteome_dir
''')

def extract_blast_hits():
    with os.scandir(current_directory) as entries:
        for entry in entries:
            if entry.is_dir():
                #print(entry.name)
                with os.scandir(entry) as subentries:
                    for subentry in subentries:
                        if subentry.is_file():
                            if subentry.name.endswith(".blastp"):
                                with open(entry.name + "/" + subentry.name, 'r') as f:
                                    if f.read(1):
                                        lines = f.readline()
                                        spt = lines.split('\t')[1]
                                        for proteome in os.listdir(proteomes_dir):
                                            if proteome.endswith(".fasta") or proteome.endswith(".faa") or proteome.endswith(".fa") or proteome.endswith(".fas"):
                                                ext_proteins_files = current_directory + "/" + entry.name + "/" + subentry.name + ".fasta"
                                                proteome_files = proteomes_dir + proteome
                                                #print(proteome_files)
                                                with open(proteome_files, 'r') as proteome_search, open(ext_proteins_files, 'a') as extracted_seqs:
                                                    while True:
                                                        proteome_line = proteome_search.readline()
                                                        if proteome_line:
                                                            #print(proteome_line)
                                                            proteome_seqs = re.search(protein_name_in_proteome, proteome_line)
                                                            if proteome_seqs:
                                                                #print(proteome_seqs.group(0))
                                                                aux = 0
                                                                if spt == proteome_seqs.group(0).replace(">", ""): 
                                                                    aux = 1
                                                                    #print("ok")
                                                            if aux: 
                                                                extracted_seqs.write(proteome_line)
                                                                print(proteome_line)
                                                                #print(ext_proteins_files)
                                                        else: break
                                                        #proteome_search.seek(0)

def concatenate_seqs():
    with os.scandir(current_directory) as entries:
        for entry in entries:
            if entry.is_dir():
                #print(entry.name)
                with os.scandir(entry) as subentries:
                    for subentry in subentries:
                        if subentry.is_file():
                            if subentry.name.endswith(".fasta"):
                                with open(entry.name + "/" + subentry.name, 'r') as f, open(entry.name + "/" + "all_proteins.fasta", 'a') as output:
                                    #if f.read():
                                    while True:
                                        lines = f.readline()
                                        if lines:
                                            print(lines)
                                            output.write(lines)
                                        else: break

### Regex ###

protein_name_in_proteome = r"(?!\w)^[^\s]+" # selects protein name with '>'

### Parser ###

p = argparse.ArgumentParser()
p.add_argument("-p", "--proteomes_dir", required=True)

args = p.parse_args()

### Code ###

if __name__ == "__main__":
	proteomes_dir = args.proteomes_dir
	current_directory = os.getcwd()

extract_blast_hits()
concatenate_seqs()