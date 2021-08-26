import re, os, subprocess, sys, argparse, shutil 
from Bio import SeqIO

### Command line arguments ###

if len(sys.argv) <= 1:
	sys.argv.append("-h")

if sys.argv[1] in ["-h", "--help", "getopt", "usage", "-help", "help"]:
	sys.exit('''
USAGE:  split_fasta.py [ options ]
Split the fasta file into folders containing the sequences of the same name.
    -f|--fasta_file
    -d|--output_directory (Optional. Default: current directory)
''')

### Regex ###

sequence_name = r"(?!\w)^[^\s]+" # selects the sequence name with '>'      

### Functions ###

sequence_names = []
sequence_folders = []

def select_sequences(): # selects the sequences that are going to be saparated in folders and fasta files
    with open(infile, 'r') as blast_output:
        while True:
            infile_lines = blast_output.readline()
            if infile_lines:
                sequence_codes = re.search(sequence_name, infile_lines) # search the sequence name in fasta file
                if sequence_codes:
                    seq_codes = sequence_codes.group(0).replace('>','') # removes the ">" 
                    if seq_codes not in sequence_names:
                        sequence_names.append(seq_codes) # keep the name in a list
            else: break

def create_sequence_folder(): # creates a folder for each sequence
    for items in sequence_names:
        print(items)
        if args.output_directory:
            path = os.path.join(out_dir,items)
        else:
            path = os.path.join(current_directory,items)
        os.mkdir(path)

def split_multifasta(): # split the fasta file, so each sequence goes to the folder of the same name
    f_open = open(infile, "rU")
    for rec in SeqIO.parse(f_open, "fasta"):
        seq_id = rec.id
        sequence = rec.seq
        id_file = open(seq_id+".splitted.fa", "w")
        id_file.write(">"+str(seq_id)+"\n"+str(sequence))
        id_file.close()
    f_open.close()

def move_files(): # move each fasta file to the right folder
    if args.output_directory:
        for f in os.listdir(current_directory):
            if f.endswith(".splitted.fa"):
                for folders in os.listdir(out_dir):
                    if f.replace(".splitted.fa","") == folders: # compare the name of the file and the name of the folder
                        fasta_location = current_directory + "/" + f
                        new_folder = out_dir + "/" +  folders + "/" + f
                        os.replace(fasta_location, new_folder) # moves the fasta files to the folder with the same name
    else:
        for folders in os.listdir(current_directory):
            if os.path.isdir(folders):
                for f in os.listdir(current_directory):
                    if f.endswith(".splitted.fa"):
                        if f.replace(".splitted.fa","") == folders: # compare the name of the file and the name of the folder
                            fasta_location = current_directory + "/" + f
                            new_folder = current_directory + "/" +  folders + "/" + f
                            os.replace(fasta_location, new_folder) # moves the fasta files to the folder with the same name


### Parser ###

p = argparse.ArgumentParser()
p.add_argument("-f", "--fasta_file", required=True)
p.add_argument("-d", "--output_directory")

args = p.parse_args()

### Code ###

if __name__ == "__main__":
    infile = args.fasta_file
    out_dir = args.output_directory
    current_directory = os.getcwd()

select_sequences()
create_sequence_folder()
split_multifasta()
move_files()