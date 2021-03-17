# Scripts used for "Population and comparative genetics of thermotolerance divergence between yeast species"

<body>
<b> G1 plotting: <b>
  G1_ESP1_plotting.ipynb: Generate plots for Figure 1 (A peak of high allele frequency in S. cerevisiae populations at the 5’ end of ESP1).

  G1_pi_plotting.ipynb: Generate plots for Supplementary Figure 1 (Spatial distribution of allele sharing in wine/European S. cerevisiae at thermotolerance genes).

codon_alignment.ipynb: Generate codon-based alignments of all Scer strains (Peter, et al 2018) with European S. paradoxus (Bergström et al., 2014) and North American S. paradoxus subpop B (Durand et al., 2019) using PAL2NAL for input into the McDonald-Kreitman test. 

MK_calc.ipynb: Run McDonald-Krietman test using Biopython library and output MK p values and statistics (Dn, Ds, Pn, Ps).

MK_analysis.ipynb: Resample McDonald Kreitman statistics generated in MK_calc.ipynb.

dxy_calc.py: Calculate Dxy for each file in a directory.

dxy_analysis_1011pops_EuroSpar.ipynb: Calculate Dxy p values using a resampling test for S. cerevisiae populations (Peter et al., 2018) and European S. paradoxus (Bergstrom et al., 2014).

dxy_analysis_1011pops_NASpar.ipynb: Calculate Dxy p values using a resampling test for S. cerevisiae populations (Peter et al., 2018) and North American S. paradoxus subpopulation B (Durand et al., 2019).

dxy_analysis_allScer_allSpar.ipynb: Calculate Dxy p values using a resampling test all S. cerevisiae strains (Peter et al., 2018) and European S. paradoxus (Bergstrom et al., 2014) + North American S. paradoxus subpopulation B (Durand et al., 2019).

prealignment_sequence_prep.ipynb: Generate unaligned sequence files for each combination of S. cerevisiae (Peter, et al 2018) and S. paradoxus population (Bergström et al., 2014; Durand et al., 2019) to be aligned by MUSCLE.

muscle.sh: Bash script for alignment by MUSCLE.

Packages/Software:
[Biopython](https://biopython.org/)

[MUSCLE](http://www.drive5.com/muscle/)

[PAL2NAL](http://www.bork.embl.de/pal2nal/)

https://bremlab.berkeley.edu/

</body>
