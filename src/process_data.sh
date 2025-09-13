#!/bin/bash
for file in data/raw/*.csv; do
    echo "Processing $file" 
    # Uncomment the next line to actually copy the files
    cp "$file" data/processed/    
done