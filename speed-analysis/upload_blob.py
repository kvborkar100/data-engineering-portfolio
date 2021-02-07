import os
from typing import Container
from azure.storage.blob import BlobClient

file_dir = "/home/krushna/Documents/Krushna/Projects/portfolio/files"

os.chdir(file_dir)
files = os.listdir()


connection_string = "BlobEndpoint=https://practiceblobs.blob.core.windows.net/;QueueEndpoint=https://practiceblobs.queue.core.windows.net/;FileEndpoint=https://practiceblobs.file.core.windows.net/;TableEndpoint=https://practiceblobs.table.core.windows.net/;SharedAccessSignature=sv=2019-12-12&ss=b&srt=sco&sp=rwdlacx&se=2021-05-31T13:58:19Z&st=2021-02-07T05:58:19Z&spr=https,http&sig=VfLJiusCvuIg0yY7LR7qgfC7Oyz3v%2B%2BUlu1WkhWB8Q0%3D"

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
