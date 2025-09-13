import pandas as pd
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.python.analysis import load_data, clean_data, save_data, analyze_data

def create_sample_data(tmp_path):        
    data = {
        "Hugo_Symbol": ["TP53", "BRCA1", "EGFR", "TP53", "BRCA1", "PTEN", "EGFR", "TP53", "PTEN", "BRCA2"],
        "Other_Column": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    df = pd.DataFrame(data)
    input_path = f"{tmp_path}/sample_data.csv"
    with open(input_path, 'w') as f:
        f.write("# The cBioPortalFiles\n")
        f.write("# have 2 comment rows  \n")    
    df.to_csv(f"{tmp_path}/sample_data.csv", index=False, sep="\t", mode="a")
    return df

def test_pipeline_smoke(tmp_path):
    df = create_sample_data(tmp_path) # ADDITIONAL TEST DATA CREATION
    df_loaded = load_data(f"{tmp_path}/sample_data.csv")    
    assert not df_loaded.empty    
    df_cleaned = clean_data(df_loaded)    
    assert not df_cleaned.empty
    save_data(df_cleaned, f"{tmp_path}/cleaned_data.csv")
    assert os.path.exists(f"{tmp_path}/cleaned_data.csv")
    print(df_cleaned)
    fig = analyze_data(df_cleaned)    
    fig.savefig(f"{tmp_path}/top_mutated_genes.png")
    assert os.path.exists(f"{tmp_path}/top_mutated_genes.png")

if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_pipeline_smoke(tmpdirname)

    