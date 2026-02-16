import json
import urllib.request
import re

url = "https://huggingface.co/api/datasets/evaleval/EEE_datastore/tree/main?recursive=true"
total_items = 0
file_count = 0
page = 1

while url:
    print(f"Fetching page {page}...")
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
            # Check headers for Link
            link_header = response.headers.get('Link')
            # print(f"Link Header: {link_header}")
            
            files_in_page = [item for item in data if item.get('type') == 'file']
            
            total_items += len(data)
            file_count += len(files_in_page)
            
            print(f"  Items: {len(data)}, Files in page: {len(files_in_page)}")
            
            if len(files_in_page) > 0:
                print(f"  Sample file: {files_in_page[0]['path']}")

            # Parse next link
            url = None
            if link_header:
                links = link_header.split(',')
                for link in links:
                    if 'rel="next"' in link:
                        match = re.search(r'<([^>]+)>', link)
                        if match:
                            url = match.group(1)
                            
        page += 1
        if page > 50: # safety
             print("Hit page limit")
             break
             
    except Exception as e:
        print(f"Error: {e}")
        break

print(f"Total processed items: {total_items}")
print(f"Total files found: {file_count}")
