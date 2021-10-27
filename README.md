# easy-phylogenomics
This repository contains scripts that facilitate the manipulation of large amounts of data for phylogenomic analysis.

# Requirements #

- [Python >= 3](https://www.python.org/downloads/)
- [DIAMOND](https://github.com/bbuchfink/diamond)
- [Mafft](https://mafft.cbrc.jp/alignment/software/) 


**<p>I) split_fasta_into_folders.py</p>**
<ul>
<p>Split the fasta file into folders containing the sequences of the same name.</p>
OPTIONS:<br>
 <ul>
-f|--fasta_file<br>
-d|--output_directory (Default: current directory)
</ul>
</ul>

```bash
split_fasta_into_folders.py  \
	-f sequences.fasta \
	-d /path/to/dir/ \
```
	
**<p>II) blastp_with_diamond.py</p>**
<ul>
<p>Perform BLASTP searches in multiple proteomes using as query the splited sequences inside the folders.</p>
OPTIONS:<br>
<ul>
    -p|--proteomes_dir	Directory containing proteome files in FASTA format.<br>
    -e|--evalue		E-value for BLAST search (Default: 1e-10)<br>
    -t|--threads	Number of CPU threads (Default: all available virtual cores in the machine)
</ul>
</ul>

```bash
blastp_with_diamond.py  \
	-p path/to/folders \
	-e 1e-05 \
	-t 10
```

**<p>III) extract_blast_hits.py</p>**
<ul>
<p>Extract the sequences from blastp output.</p>
OPTIONS:<br>
<ul>
    -p|--proteome_dir
</ul>
</ul>

```bash
extract_blast_hits.py  \
	-p path/to/folders \
```

**<p>IV) run_mafft.py</p>**
- [Kazutaka Katoh, Daron M. Standley, MAFFT Multiple Sequence Alignment Software Version 7: Improvements in Performance and Usability, Molecular Biology and Evolution, Volume 30, Issue 4, April 2013, Pages 772–780, https://doi.org/10.1093/molbev/mst010](https://academic.oup.com/mbe/article/30/4/772/1073398)
<ul>
<p>Multiple alignment program for amino acid or nucleotide sequences.</p>
</ul>

```bash
run_mafft.py
```
	
# Co-author #

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/EberhardtRafael"><img src="https://avatars.githubusercontent.com/u/88341243?v=4" width="100px;" alt=""/><br /><sub><b>Rafael Eberhardt</b></sub></a><br />
