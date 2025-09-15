library(testthat)
source("../../src/R/analysis.R")

test_that("pipeline smoke test", {
  df <- data.frame(
    Hugo_Symbol = c("TP53", "BRCA1", NA, "EGFR"),
    Variant_Classification = c("Missense_Mutation", "Nonsense_Mutation", "Frame_Shift_Del", NA),
    Tumor_Sample_Barcode = c("Sample1", "Sample2", "Sample3", "Sample4")
  )  
  cleaned <- clean_data(df)
  expect_true(nrow(cleaned) > 0)
  expect_true(all(c("Hugo_Symbol", "Variant_Classification", "Tumor_Sample_Barcode") %in% colnames(cleaned)))
})