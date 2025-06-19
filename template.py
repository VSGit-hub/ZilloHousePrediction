import os
from pathlib import Path

list_of_files = [
    "main.py",
    "app.py",
    "raw_data",
    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",   
    "config/config.toml",
    "config/params.toml",
    "config/schema.toml",
    "artifacts/data_ingestion",
    "artifacts/data_transformed",
    "artifacts/data_training",
    "artifacts/saved_models",
    "research/research.ipynb",
    "logging/logger.py",
    "logging/__init__.py"
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/predict_result.py"
    "src/components/__init__.py",   
    "src/config_manager/config_manager.py",
    "src/config_manager/__init__.py",
    "src/pipeline/data_ingestion_pipeline.py",
    "src/pipeline/data_transformation_pipeline",
    "src/pipeline/model_trainer_pipeline.py",
    "src/pipeline/model_evaluation_pipeline.py",
    "src/pipeline/predict_result_pipeline.py",
    "src/pipeline/__init__.py",
    "src/utils/common.py",
    "src/utils/__init__.py",
    "src/exception/custom_exception.py",
    "src/exception/__init__.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    # Check if it's a directory (no dot in filename)
    if filepath.suffix == "":
        os.makedirs(filepath, exist_ok=True)
    else:
        # Create parent directory
        filepath.parent.mkdir(parents=True, exist_ok=True)
        # Create empty file if doesn't exist
        if (not filepath.exists()) or (filepath.stat().st_size == 0):
            filepath.touch()
