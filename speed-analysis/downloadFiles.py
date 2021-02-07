import requests
from bs4 import BeautifulSoup
import re
import time
import wget

def get_urls(url):
    page = requests.get(url)
    urls = {}
    # print(page.status_code)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        tag_url = soup.select(
            "#table_view > div > div:nth-child(3) > div:nth-child(4) > p:nth-child(4) > a")
        for fileURL in tag_url:
            urls[fileURL.text] = fileURL["href"]
    return urls


def downloadFiles(url, urls):
    print(f"Found total {len(urls)} files")
    print("Initiating Download...")
    file_num = 1

    for key, value in urls.items():
        blob_name = key.strip()+".csv"
        print(f"Downloading file {file_num} - {key} - {blob_name}")
        file_url = url + value
        # print(file_url)
        # print(key.strip())
        wget.download(file_url, f"/home/krushna/Documents/Krushna/Projects/portfolio/files/{blob_name}")
        print(f"File {blob_name} - Downloaded")
        file_num += 1
        time.sleep(10)


if __name__ == "__main__":
    url = "https://myspeed.trai.gov.in/"
    urls = get_urls(url)
    downloadFiles(url, urls)



