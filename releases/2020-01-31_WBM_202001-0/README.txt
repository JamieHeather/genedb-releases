This directory contains the list of genes managed in the IMGT/GENE-DB database and the IMGT/GENE-DB reference sequences in FASTA format.

1) List of IMGT/GENE-DB genes:
* The file IMGTGENEDB-GeneList includes the list of genes with the following fields separated by ";":
  - the species
  - the IMGT/GENE-DB gene name
  - the IMGT gene functionality 
  - the IMGT and HGNC gene definition
  - the number of alleles 
  - the chromosome
  - the chromosomal localization
  - the IMGT/LIGM-DB reference sequence for the allele *01
  - the NCBI Gene ID


2) IMGT/GENE-DB reference sequences in FASTA format:

* The file IMGTGENE-DB-ReferenceSequences.fasta-nt-WithGaps-F+ORF+inframeP includes IMGT/GENE-DB nucleotide reference sequences for functional, 
  open reading frame and in-frame pseudogene genes and alleles, with IMGT gaps for V and C genes and alleles.

* The file IMGTGENE-DB-ReferenceSequences.fasta-nt-WithoutGaps-F+ORF+inframeP includes IMGT/GENE-DB nucleotide reference sequences for functional, 
  open reading frame and in-frame pseudogene genes and alleles, without IMGT gaps.

* The file IMGTGENE-DB-ReferenceSequences.fasta-nt-WithoutGaps-F+ORF+allP includes IMGT/GENE-DB nucleotide reference sequences for functional, 
  open reading frame and all pseudogene genes and alleles, without IMGT gaps.

* The file IMGTGENE-DB-ReferenceSequences.fasta-AA-WithGaps-F+ORF+inframeP includes IMGT/GENE-DB amino acid reference sequences for functional, 
  open reading frame and in-frame pseudogene genes and alleles, with IMGT gaps for V and C genes and alleles.

* The file IMGTGENE-DB-ReferenceSequences.fasta-AA-WithoutGaps-F+ORF+inframeP includes IMGT/GENE-DB amino acid reference sequences for functional, 
  open reading frame and in-frame pseudogene genes and alleles, without IMGT gaps.


The IMGT/GENE-DB FASTA header contains 15 fields separated by '|':

1. IMGT/LIGM-DB accession number(s)
2. IMGT gene and allele name
3. species
4. IMGT gene and allele functionality
5. exon(s), region name(s), or extracted label(s)
6. start and end positions in the IMGT/LIGM-DB accession number(s)
7. number of nucleotides in the IMGT/LIGM-DB accession number(s)
8. codon start, or 'NR' (not relevant) for non coding labels
9. +n: number of nucleotides (nt) added in 5' compared to the corresponding label extracted from IMGT/LIGM-DB
10. +n or -n: number of nucleotides (nt) added or removed in 3' compared to the corresponding label extracted from IMGT/LIGM-DB
11. +n, -n, and/or nS: number of added, deleted, and/or substituted nucleotides to correct sequencing errors, or 'not corrected' if non corrected sequencing errors
12. number of amino acids (AA): this field indicates that the sequence is in amino acids
13. number of characters in the sequence: nt (or AA)+IMGT gaps=total
14. partial (if it is)
15. reverse complementary (if it is)


An IMGT/GENE-DB reference sequence for a given IG or TR gene is provided, in the 5' > 3' DNA strand orientation corresponding to the 'sense', 'plus' or 'coding strand' of that gene (IMGT Index > DNA strand orientation).
The orientation (direct or opposite) of an IG or TR gene in a given IMGT locus is given in Locus Gene order (IMGT Index > Genomic orientation)
IMGT Repertoire (IG and TR) > 1. Locus and genes > 3. Locus descriptions > Locus gene order.


IMGT®, the international ImMunoGeneTics information system®, is a high-quality integrated knowledge resource specializing in the immunoglobulins (IG) or antibodies, 
T cell receptors (TR), and major histocompatibility (MH) of human and other vertebrate species, proteins of the immunoglobulin superfamily (IgSF) and MH superfamily (MhSF), 
related proteins of the immune systems (RPI) of vertebrates and invertebrates, therapeutic monoclonal antibodies (mAb), and fusion proteins for immune applications (FPIA), 
created in 1989 by Marie-Paule Lefranc (LIGM, Université Montpellier 2, CNRS).
IMGT, a European project since 1992, works in close collaboration with
EBI. IMGT® consists of several databases, Web resources and interactive tools
available at the IMGT home page (http://www.imgt.org).

IMGT/GENE-DB, which is distributed in the current directory, is the IMGT genome database for IG and TR genes from human, mouse and other vertebrates, on the Web since February 2003.
IMGT/GENE-DB online (http://www.imgt.org) provides a full characterization of the genes and of their alleles: IMGT gene name and definition, chromosomal localization, number of alleles, 
and for each allele, the IMGT allele functionality, and the IMGT reference sequences and other sequences from the literature. 
IMGT/GENE-DB allele reference sequences are available in FASTA format (nucleotide and amino acid sequences with IMGT gaps according to the IMGT unique numbering, or without gaps). 
IMGT/GENE-DB includes links to the IMGT Repertoire standardized resources (Chromosomal localization, Locus representation, Tables of alleles, Alignments of alleles, 
IMGT Protein displays, IMGT Colliers de Perles, etc.), to the IMGT/LIGM-DB and IMGT/3Dstructure-DB structures and IMGT/2Dstructure-DB IMGT databases.
IMGT/GENE-DB is the official repository of all of the IG and TR genes and alleles approved by the World Health Organization (WHO)/International Union of Immunological 
Societies (IUIS) Nomenclature Subcommittee for IG and TR. Reciprocal links exist between IMGT/GENE-DB and the Human Genome Nomenclature Committee (HGNC) database, 
NCBI Gene at the National Center for Biotechnology Information (NCBI) and Vega Genome Browser (Wellcome Trust Sanger Institute). 


IMGT/GENE-DB program and data updates are available from the top of the query page.

Statistics are available from the IMGT/GENE-DB query page.

- Citing IMGT®, the international ImMunoGeneTics information system®
Lefranc M.-P., Giudicelli V., Ginestoux C., Jabado-Michaloud J., Folch G.,
Bellahcene F., Wu Y., Gemrot E., Brochet X., Lane J., Regnier L.,
Ehrenmann F., Lefranc G. and Duroux P. Nucl. Acids Res, 37, D1006-D1012 (2009); doi:10.1093/nar/gkn838. PMID: 18978023.


- Citing IMGT/GENE-DB
Giudicelli V., Chaume D. and Lefranc M.-P. 
IMGT/GENE-DB: a comprehensive database for human and mouse immunoglobulin and T cell receptor genes. Nucl. Acids Res. 2005, 33, D593-D597. PMID: 15608269.

For more information on IMGT®, the international ImMunoGeneTics information system® and on-line access to IMGT/GENE-DB, see the IMGT home page (http://www.imgt.org).

IMGT downloads is free of charge for public institutions and depends on an agreement with CNRS for private companies. 

Contacts: 
Marie-Paule Lefranc <Marie-Paule.Lefranc.igh.cnrs.fr>
Patrice <Duroux Patrice.Duroux@igh.cnrs.fr>
Véronique Giudicelli <Veronique.Giudicelli@igh.cnrs.fr>
