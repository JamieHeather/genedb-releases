# geneDB releases
### v 0.1.0 
#### Jamie Heather @ MGH, 2023-04

This repo aims to collate publicly available releases of the [IMGT/GENE-DB resource of immunoglobulin and T cell receptor germline genes](https://www.imgt.org/download/GENE-DB/). I am not affiliated with IMGT in any way, I've just gathered these data to make it easier to compare between different releases of this resource, as to the best of my knowledge IMGT only hosts current releases. However given that people publish papers and tools using and referencing this database, it seems that a public historical record is necessary for ensuring reproducibility.

The releases themselves are stored in the `releases/` directory, named by date of access, source of access, and IMGT provided release number. The majority of the pre-2022 historical releases were recovered using [the Internet Archive's Wayback Machine](https://web.archive.org/) ('WBM' label), using the `scripts/harvest-wayback.py` script. Some entries (absent most files) were incidentally banked by me using my tool [IMGTgeneDL](https://github.com/JamieHeather/IMGTgeneDL) (producing reference sets for [stitchr](https://github.com/JamieHeather/stitchr)) ('JH-GeneDL'). Newer entries have been directly downloaded from GENE-DB itself ('GENEDB'). Note that this is likely an incomplete record of published releases.

### IMGT licensing information

As stated [on their website](https://www.imgt.org/about/termsofuse.php) and [in their publications](https://doi.org/10.1093/nar/gkab1136), IMGT's policy regarding sharing of their data is that:

"*... IMGT® software and data are provided to the academic users and NPO's (Not for Profit Organization(s)) under the [CC BY-NC-ND 4.0 license](https://creativecommons.org/licenses/by-nc-nd/4.0/). Any other use of IMGT® material, from the private sector, needs a financial arrangement with CNRS.*"

