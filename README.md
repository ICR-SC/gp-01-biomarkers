# Biomarkers Project for Good Practice Course
**A project for a good practice workflow using both R and python**  
Author: Rachel Alcraft  
Last updated: 17-09-25  

This project is the repo created as a result of the Good Practice ion Research COding 5 session course at the Institute of Cancer Research.

The documentation for the project is in [an accompanying website](https://icr-sc.github.io/good-practice/good/overview/)  
The YouTube PlayList of videos for the course is [here](https://studio.youtube.com/playlist/PLKk58i7WAwK7gj3oZLR9MKQ-qTjOT7_t2/videos)  


## Data
https://www.cbioportal.org/datasets  
https://cbioportal-datahub.s3.amazonaws.com/aml_tcga_gdc.tar.gz  

## Python code
To activate the python environment type in the console:
```bash
source environment/bin/activate
```
To run the main python script type in the console:
```bash
 python src/python/analysis.py
```

## R Code
The environment should activate from the lock file on opening (VSCode or RStudio).  
To run the main R script, typpe in the console:
```bash
Rscript src/R/analysis.R
```

---  

## References
- Cerami et al. The cBio Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics Data. Cancer Discovery. May 2012; 401. [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/22588877)
- Gao et al. Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal. Sci. Signal. 6, pl1 (2013). [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/23550210)
- de Bruijn et al. Analysis and Visualization of Longitudinal Genomic and Clinical Data from the AACR Project GENIE Biopharma Collaborative in cBioPortal. Cancer Res (2023). [PubMed](https://pubmed.ncbi.nlm.nih.gov/37668528/)
- DataSet: https://www.cbioportal.org/study/plots?id=aml_tcga_gdc



