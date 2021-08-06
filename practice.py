import glob
import os
import pprint

#accesses /content and output files from /docs
all_html_files = glob.glob('contents/*.html')
all_output_files = glob.glob('docs/*.html')

#loops through all_html_files and makes a list of just the names of the files
# which are the titles of each page
all_html_files = glob.glob('contents/*.html')
all_output_files = glob.glob('docs/*.html')

pages=[]
for files, file in zip(all_html_files, all_output_files):
    filename = os.path.relpath(files)
    output = os.path.relpath(file)
    title_parse = os.path.basename(filename).upper()
    title, extension = os.path.splitext(title_parse)

# try moving this block to line 38
    if title == 'INDEX':
        title = 'ABOUT'

    pages.append({
        'filename': filename,
        'output': output,
        'title': title,
    })

pprint.pprint(pages, indent = 2, width = 30)

for page in pages:
    print('these are the pages:', page)