import os
from typing import Container
from azure.storage.blob import BlobClient

file_dir = "/home/krushna/Documents/Krushna/Projects/portfolio/files"

os.chdir(file_dir)
files = os.listdir()


connection_string = "Your_Account_String_Here"

container_name = "files"

counter = 1

for file in files:
    blob = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=file)
    print(f"Uploading {file} {counter} to Azure Container...")

    try:
        with open(file, "rb") as data:
            blob.upload_blob(data)
        counter += 1
        print(f"file {file} has been uploaded successfully")
    except:
        print(f"Error while uploading {file} to Azure Container")

print("All files are uploaded to the Azure Container")
