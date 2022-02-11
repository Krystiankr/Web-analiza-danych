import os
import re
import time

import requests
from bs4 import BeautifulSoup

destination = r"C:\Users..."
source_url = "http://wmii.uwm.edu.pl..."
allows_extension = "\."

r = requests.get(source_url)
r.encoding = r.apparent_encoding
doc = BeautifulSoup(r.text, "html.parser")

print("Displaying folders in this directory.")
for el in doc.findAll("img", {"alt": "[DIR]"}):
    parent_text: str = el.parent.parent.text
    parent_text = parent_text.split('/')[0]
    print(parent_text)
    print(f"Opening next directory {parent_text}")
    path = os.path.join(destination, parent_text)

    # Check if dir exists
    if not os.path.isdir(f"{destination}\{parent_text}"):
        print(f"Create new directory {parent_text}")
        os.mkdir(path)
    else:
        print(f"{parent_text} folder already exists.")

    child_link = f"{source_url}/{parent_text}"
    r = requests.get(child_link)
    r.encoding = r.apparent_encoding
    child_doc = BeautifulSoup(r.text, "html.parser")
    for href_child in child_doc.findAll(href=re.compile(allows_extension)):
        print(href_child['href'])
        full_link = rf"{source_url}//{parent_text}//{href_child['href']}"
        print(f"Full link = {full_link}")
        where_save = f"{destination}\\{parent_text}\\{href_child['href']}"
        print(f"Where save {where_save}")
        r = requests.get(full_link, allow_redirects=True)
        with open(where_save, 'wb') as f:
            f.write(r.content)
        # open(where_save, 'wb').write(r.content)
    print()
print("-------------Koniec-------------")
