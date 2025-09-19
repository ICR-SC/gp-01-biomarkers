
# Building docker as singularity base image
```bash
docker save good-conda:latest -o good-conda.tar
singularity build good-conda.sif docker-archive://good-conda.tar
```

## Run the Python script
    singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env python /app/analysis.py"

## Run the R script
    singularity exec --bind data:/app/data,results:/app/results good-conda.sif bash -c "source /opt/conda/etc/profile.d/conda.sh && conda run -n good-env Rscript /app/analysis.R"
