# easy-phylogenomics
This repository contains scripts that facilitate the manipulation of large amounts of data for phylogenomic analysis.

# Requirements #

- [Python >= 3](https://www.python.org/downloads/)
- [DIAMOND](https://github.com/bbuchfink/diamond) 


USAGE:  split_fasta_into_folders.py [ options ]\
Split the fasta file into folders containing the sequences of the same name.\
    -f|--fasta_file\
    -d|--output_directory (Optional. Default: current directory) [ options ]\

```bash
split_fasta_into_folders.py  \
	-f sequences.fasta \
	-d /path/to/dir/ \
```

# Co-author #

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/EberhardtRafael"><img src="https://avatars.githubusercontent.com/u/88341243?v=4" width="100px;" alt=""/><br /><sub><b>Rafael Eberhardt</b></sub></a><br />
