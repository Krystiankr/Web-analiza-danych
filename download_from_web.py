from bs4 import BeautifulSoup
from typing import List
from tqdm import tqdm
import requests
import os
import re


def get_all_dirs(url) -> List[str]:
    def format_name(name):
        parent_text = name.parent.parent.text
        parent_text = parent_text.split('/')[0]
        return parent_text
    return [format_name(dir_name) for dir_name in url.findAll("img", {"alt": "[DIR]"})]


def get_all_files(url) -> List[str]:
    return [href_child['href'] for href_child in url.findAll(href=re.compile(allows_extension))]


def recursion_dir(source_url: str, destination: str, show_progress=True):
    r = requests.get(source_url)
    r.encoding = r.apparent_encoding
    doc = BeautifulSoup(r.text, "html.parser")
    with tqdm(total=1, desc="Searching", unit="file", disable=not show_progress) as myprogressbar:
        all_files = get_all_files(doc)
        myprogressbar.total += len(all_files) - 1
        for file in all_files:
            myprogressbar.update()
            full_link = rf"{source_url}//{file}"
            where_save = f"{destination}\\{file}"
            r = requests.get(full_link, allow_redirects=True)
            with open(where_save, 'wb') as f:
                f.write(r.content)
    for sub_dir in get_all_dirs(doc):
        path = os.path.join(destination, sub_dir)
        # Check if dir exists
        if not os.path.isdir(f"{destination}\{sub_dir}"):
            print(f"Create new directory {sub_dir}")
            os.mkdir(path)
        else:
            print(f"{sub_dir} folder already exists.")
        full_link = rf"{source_url}{sub_dir}"
        dest = f"{destination}\\{sub_dir}"
        print(f"full {full_link}")
        recursion_dir(full_link, dest)
    print("-------------Koniec-------------")
    
    
destination = r"C:\Users\..."
source_url = "http://wmii.uwm.edu.pl/...."
allows_extension = "\."

recursion_dir(source_url, destination)
