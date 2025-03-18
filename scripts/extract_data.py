import os
import boto3
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset: str, download_path: str):
    """Downloads a dataset from Kaggle."""
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    print(f"Dataset downloaded to {download_path}")

def upload_to_s3(bucket_name: str, folder_path: str):
    """Uploads files from a local folder to an AWS S3 bucket."""
    s3_client = boto3.client('s3')
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.relpath(local_path, folder_path)
            s3_client.upload_file(local_path, bucket_name, s3_path)
            print(f"Uploaded {file} to s3://{bucket_name}/{s3_path}")

if __name__ == "__main__":
    # Set parameters
    KAGGLE_DATASET = "instacart-market-basket-analysis"
    DOWNLOAD_PATH = "data"
    S3_BUCKET_NAME = "your-s3-bucket-name"
    
    # Download dataset from Kaggle
    download_kaggle_dataset(KAGGLE_DATASET, DOWNLOAD_PATH)
    
    # Upload dataset to S3
    upload_to_s3(S3_BUCKET_NAME, DOWNLOAD_PATH)