library(readr)
library(dplyr)
library(ggplot2)

load_data <- function(file_path) {
  df <- read_tsv(file_path, skip = 2)
  return(df)
}

clean_data <- function(df) {
  df <- df %>%
    select(Hugo_Symbol, Variant_Classification, Tumor_Sample_Barcode) %>%
    na.omit()
  return(df)
}

save_data <- function(df, output_path) {
  write_tsv(df, output_path)
}

analyse_data <- function(df) {
  summary <- df %>%
    count(Hugo_Symbol, sort = TRUE) %>%
    head(10)
  print(summary)
  p <- ggplot(summary, aes(x = reorder(Hugo_Symbol, -n), y = n)) +
    geom_bar(stat = "identity") +
    xlab("Gene") +
    ylab("Mutation Count") +
    ggtitle("Top 10 Mutated Genes") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  return(p)
}

# Example usage
#args <- commandArgs(trailingOnly=TRUE)
data_file <- "data/raw/aml_tcga_gdc/data_mutations.txt"
df <- load_data(data_file)
df_clean <- clean_data(df)
save_data(df_clean, "data/processed/cleaned_mutations_R.tsv")
p <- analyse_data(df_clean)
ggsave("results/top_mutated_genes_R.png", plot = p, width = 8, height = 5)
