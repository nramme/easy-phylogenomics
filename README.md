# easy-phylogenomics
This repository contains scripts that facilitate the manipulation of large amounts of data for phylogenomic analysis.

# Requirements #

- [Python >= 3](https://www.python.org/downloads/)
- [DIAMOND](https://github.com/bbuchfink/diamond) 


<p>USAGE:  split_fasta_into_folders.py [ options ]</p>
<p>Split the fasta file into folders containing the sequences of the same name.</p>
OPTIONS:<br>
 <ul>
-f|--fasta_file<br>
-d|--output_directory (Default: current directory)
</ul>

```bash
split_fasta_into_folders.py  \
	-f sequences.fasta \
	-d /path/to/dir/ \
```

<p>USAGE:  blastp_with_diamond.py [ options ]</p>
<p>Perform BLASTP searches in multiple proteomes using as query the splited sequences inside the folders.</p>
OPTIONS:<br>
<ul>
    -p|--proteomes_dir	Directory containing proteome files in FASTA format.<br>
    -e|--evalue		E-value for BLAST search (Default: 1e-10)<br>
    -t|--threads	Number of CPU threads (Default: all available virtual cores in the machine)
</ul>

```bash
blastp_with_diamond.py  \
	-p path/to/folders \
	-e 1e-05 \
	-t 10
```

# Co-author #

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/EberhardtRafael"><img src="https://avatars.githubusercontent.com/u/88341243?v=4" width="100px;" alt=""/><br /><sub><b>Rafael Eberhardt</b></sub></a><br />
