import re, os, subprocess, sys

### Command line arguments ###

if len(sys.argv) <= 1:
    sys.argv.append("-h")

#if sys.argv[1] in ["-h", "--help", "getopt", "usage", "-help", "help"]:
#    sys.exit('''
#    Running run_mafft.py
#
#	Mafft: Multiple alignment program for amino acid or nucleotide sequences. [Kazutaka Katoh, Daron M. Standley, MAFFT Multiple Sequence Alignment Software Version 7: Improvements in Performance and Usability, Molecular Biology and Evolution, Volume 30, Issue 4, April 2013, Pages 772–780, https://doi.org/10.1093/molbev/mst010]
#''')

def run_mafft():
    with os.scandir(current_directory) as entries:
        for entry in entries:
            if entry.is_dir():
                #print(entry.name)
                with os.scandir(entry) as subentries:
                    for subentry in subentries:
                        if subentry.is_file():
                            if subentry.name.endswith("all_proteins.fasta"):
                                out_file = current_directory + "/" + entry.name + ".aln"
                                in_file = current_directory + "/" + entry.name + "/" + "all_proteins.fasta"
                                aln = ["mafft" + " "+ in_file +" " +">" +" " + out_file]
                                print(aln)
                                subprocess.call(aln, shell=True)

### Code ###

if __name__ == "__main__":
	current_directory = os.getcwd()

run_mafft()
