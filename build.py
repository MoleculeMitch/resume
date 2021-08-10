import glob
import os
import pprint
from jinja2 import Template

    
def write_page(title, filename, output, pages):
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    result = template.render(
        pages_list = pages,
        current_page_title = title,
        html_contents = open(filename).read(),
        docs_output = open(output).read(),
    )
    
    open(output, 'w+').write(result)
    

def main():
    all_html_files = glob.glob('contents/*.html')
    all_output_files = glob.glob('docs/*.html')

    pages=[]
    for files, file in zip(all_html_files, all_output_files):
        filename = os.path.relpath(files)
        output = os.path.relpath(file)
        title_parse = os.path.basename(filename).upper()
        clipped_filename = os.path.basename(filename)
        title, extension = os.path.splitext(title_parse)

        if title == 'INDEX':
            title = 'ABOUT'

        pages.append({
            'filename': filename,
            'output': output,
            'title': title,
            'clipped_filename': clipped_filename
        })

    
    #sort pages into new sort
    page_sort = [1,0,2]
    pages = [pages[i] for i in page_sort]

    for page in pages:
        title = page['title']
        output = page['output']
        filename = page['filename']
        clipped_filename = page['clipped_filename']
        write_page(title, filename, output, pages)

        
    pprint.pprint(pages, indent = 2, width = 30)
main()
