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
        html_contents = open(filename).read()
    )

    open(output, 'w+').write(result)

def getPageOrder(page):
    return page['order']

def main():
    all_html_files = glob.glob('contents/*.html')
    pages=[]
    current_order = 1
    for files in all_html_files:
        filename = os.path.relpath(files)
        clipped_filename = os.path.basename(filename)
        output = 'docs/' + clipped_filename
        title_parse = os.path.basename(filename).upper()
        title, extension = os.path.splitext(title_parse)
        
        if title == 'INDEX':
            title = 'ABOUT'
            order = 0
        elif title == 'CONTACT':
            order = len(all_html_files) - 1
        else:
            order = current_order
            current_order += 1

        pages.append({
            'filename': filename,
            'output': output,
            'title': title,
            'clipped_filename': clipped_filename,
            'order': order
        })
    
    #sort pages into new sort
    '''
    page_sort = [1,0,2]
    if (len(pages) >= 3):
        for i in range(3, len(pages)):
            page_sort.append(i)
    '''

    pages.sort(key=getPageOrder)

    for page in pages:
        title = page['title']
        output = page['output']
        filename = page['filename']
        clipped_filename = page['clipped_filename']
        write_page(title, filename, output, pages)
        pprint.pprint(pages, indent = 2, width = 30)