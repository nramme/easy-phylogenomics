import re, os, subprocess, sys, argparse, shutil 
from Bio import SeqIO

### Command line arguments ###

if len(sys.argv) <= 1:
    sys.argv.append("-h")

if sys.argv[1] in ["-h", "--help", "getopt", "usage", "-help", "help"]:
    sys.exit('''
USAGE:  blastp_with_diamond.py [ options ]
Perform BLAST searches in multiple proteomes.
OPTIONS:
    -p|--proteomes_dir	Directory containing proteome files in FASTA format.
    -e|--evalue		E-value for BLAST search (default: 1e-10)
    -t|--threads	Number of CPU threads (default: all available virtual cores in the machine)
''')

### Parser ###

p = argparse.ArgumentParser()
p.add_argument("-q", "--proteins_query")
p.add_argument("-p", "--proteomes_dir", required=True)
p.add_argument("-e", "--evalue")
p.add_argument("-t", "--threads")

args = p.parse_args()

### Regex ###

protein_seq = r"(?!>)^[^\s]+" # selects only protein sequence
protein_name = r"(?!\w)^[^\s]+" # selects protein name with '>'


def makedb_with_diamond():
    for proteome in os.listdir(proteomes_dir):
        if proteome.endswith(".faa") or proteome.endswith(".fasta") or proteome.endswith(".fa") or proteome.endswith(".fna") or proteome.endswith(".fas"):
            DB = os.path.join(current_directory, r'DB_dir')
            if not os.path.exists(DB):
                os.makedirs(DB)
                make_db = ['diamond','makedb','--in', proteomes_dir + proteome,'--db', "DB_dir/" + proteome]
            else:
                make_db = ['diamond','makedb','--in', proteomes_dir + proteome,'--db', "DB_dir/" + proteome]
            subprocess.call(make_db, cwd=current_directory)

def blastp_with_diamond():
    DB_dir = current_directory + "/DB_dir/"
    for proteome in os.listdir(DB_dir):
        with os.scandir(current_directory) as entries: # scans the current directory to locate subdirectories
            for entry in entries:
                if entry.is_dir():
                    with os.scandir(entry) as subentries:
                        for subentry in subentries:
                            if subentry.is_file():
                                if subentry.name.endswith(".splitted.fa"):
                                    if args.evalue:
                                        blast_diamond = blast_diamond = ['diamond' ,'blastp', '-q', entry.name + "/" + subentry.name, '-d', "DB_dir/" + proteome, '-e',evalue,'-k 1', '-f', '6', '-o', entry.name + "/" + proteome.replace(".dmnd", "") + '.6.blastp']
                                    elif args.threads:
                                        blast_diamond = blast_diamond = ['diamond' ,'blastp', '-p', threads,'-q', entry.name + "/" + subentry.name, '-d', "DB_dir/" + proteome, '-e 1e-10','-k 1', '-f', '6', '-o', entry.name + "/" + proteome.replace(".dmnd", "") + '.6.blastp']
                                    elif args.evalue and args.threads:
                                        blast_diamond = blast_diamond = ['diamond' ,'blastp', '-p', threads,'-q', entry.name + "/" + subentry.name, '-d', "DB_dir/" + proteome, '-e',evalue,'-k 1', '-f', '6', '-o', entry.name + "/" + proteome.replace(".dmnd", "") + '.6.blastp']
                                    else:
                                        blast_diamond = ['diamond' ,'blastp', '-q', entry.name + "/" + subentry.name, '-d', "DB_dir/" + proteome, '-e 1e-10', '-k 1', '-f', '6', '-o', entry.name + "/" + proteome.replace(".dmnd", "") + '.6.blastp']
                                    subprocess.call(blast_diamond)

### Code ###

if __name__ == "__main__":
    evalue = args.evalue
    threads = args.threads
    proteomes_dir = args.proteomes_dir
    current_directory = os.getcwd()

makedb_with_diamond()
blastp_with_diamond()
