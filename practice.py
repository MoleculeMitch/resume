import glob
import os
import pprint

#accesses /content and output files from /docs
all_html_files = glob.glob('contents/*.html')
all_output_files = glob.glob('docs/*.html')

#loops through all_html_files and makes a list of just the names of the files
# which are the titles of each page
pages=[]
for files, file in zip(all_html_files, all_output_files):
    file_name = os.path.relpath(files)
    base_name = os.path.basename(files)
    content_files = os.path.basename(files)
    output_file = os.path.relpath(file)
    name_only, extension= os.path.splitext(base_name)
    
    pages.append({
        'filename': file_name,
        'output': output_file,
        'title': name_only,
    })

# pages.append({
#     'filename': all_html_files,
#     'output': all_output_files,
#     'title': title
# })

pprint.pprint(pages, indent = 2, width = 30)