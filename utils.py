import glob
import os
import pprint
from jinja2 import Template

    
def write_page(title, filename, output, pages):
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    print('these are the outputs:', output)
    result = template.render(
        pages_list = pages,
        current_page_title = title,
        html_contents = open(filename).read()
    )
    #print('these are the outputs:', output)
    open(output, 'w+').write(result)

def main():
    all_html_files = glob.glob('contents/*.html')
    # just_the_filename = 'about.html' # or from a os.path method...?
    # output_filename = 'docs/' + just_the_filename 
    pages=[]
    for files in all_html_files:
        filename = os.path.relpath(files)
        clipped_filename = os.path.basename(filename)
        output = 'docs/' + clipped_filename
        title_parse = os.path.basename(filename).upper()
        title, extension = os.path.splitext(title_parse)
        if title == 'INDEX':
            title = 'ABOUT'

        pages.append({
            'filename': filename,
            'output': output,
            'title': title,
            'clipped_filename': clipped_filename,
        })
    
    #sort pages into new sort
    page_sort = [1,0,2,3]
    pages = [pages[i] for i in page_sort]

    for page in pages:
        title = page['title']
        output = page['output']
        filename = page['filename']
        clipped_filename = page['clipped_filename']
        write_page(title, filename, output, pages)
        pprint.pprint(pages, indent = 2, width = 30)