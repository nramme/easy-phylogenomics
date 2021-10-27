import re, os, subprocess, sys

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