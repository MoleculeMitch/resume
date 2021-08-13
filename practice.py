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
for files in all_html_files:
    filename = os.path.relpath(files)
    just_filename = os.path.basename(filename)
    output = 'docs/' + just_filename
    title_parse = os.path.basename(filename).upper()
    title, extension = os.path.splitext(title_parse)

    print('this is output:', output)
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