import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use("Agg")

def load_data(file_path):
    """Load data from a CSV file."""
    df = pd.read_csv(file_path, sep="\t", header=2, index_col=False)
    return df

def clean_data(df):
    """Clean the DataFrame by dropping rows with missing values."""
    df_cleaned = df#.dropna()
    return df_cleaned

def save_data(df, output_path):
    """Save the DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)

def analyze_data(df):
    """Perform basic analysis on the DataFrame."""
    print("DataFrame Summary:")
    summary = df["Hugo_Symbol"].value_counts().head(10)
    print(summary)
    fig, ax = plt.subplots()
    summary.plot(kind="bar", ax=ax)
    ax.set_title("Top 10 Most Mutated Genes")
    ax.set_xlabel("Gene")
    ax.set_ylabel("Mutation Count")    
    return fig

if __name__ == "__main__":
    df = load_data("data/raw/aml_tcga_gdc/data_mutations.txt")
    df_cleaned = clean_data(df)
    save_data(df_cleaned, "data/processed/cleaned_data.csv")
    fig = analyze_data(df_cleaned)
    fig.savefig("results/top_mutated_genes_python.png")
        
    

