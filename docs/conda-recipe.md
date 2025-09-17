# Conda Recipes for Good practice

## Python recipe
```bash
conda create -n good-python python=3.13 pandas matplotlib pytest -y
conda activate good-python
```
## R recipe
```bash
conda create -n good-r r-base=4.3 r-tidyverse r-ggplot2 r-testthat -y
conda activate good-r
Rscript -e "install.packages('htmlTable', repos = 'https://cloud.r-project.org')"
```

## Mixed recipe
```bash
conda create -n good-both python=3.13 r-base=4.3 pandas matplotlib pytest r-tidyverse r-ggplot2 r-testthat -y
conda activate good-both

```
