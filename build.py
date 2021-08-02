import glob
import os
import pprint
from jinja2 import Template

    
def write_page(title, filename, output, pages):
    template_html = open('templates/base.html').read()
    template = Template(template_html)

    result = template.render(
        title = title,
        content = open(filename).read()
    )

    # if title == 'ABOUT':
    #     combined_content = combined_content.replace('{{about_xtra_class}}', 'active').replace('{{linkedin}}', 'about-linkedin').replace('{{github}}', 'about-github')
    # elif title == 'BLOG':
    #     combined_content = combined_content.replace('{{blog_xtra_class}}', 'active').replace('{{linkedin}}', 'blog-linkedin').replace('{{github}}', 'blog-github')
    # elif title == 'CONTACT':
    #     combined_content = combined_content.replace('{{contact_xtra_class}}', 'active').replace('{{linkedin}}', 'contact-linkedin').replace('{{github}}', 'contact-github')
    # else: pass
    # open(output, 'w+').write(combined_content)
    open(output, 'w+').write(result)
    print(result)
    

def main():
    all_html_files = glob.glob('contents/*.html')
    all_output_files = glob.glob('docs/*.html')

    pages=[]
    for files, file in zip(all_html_files, all_output_files):
        filename = os.path.relpath(files)
        output = os.path.relpath(file)
        title_parse = os.path.basename(filename).upper()
        title, extension = os.path.splitext(title_parse)

        pages.append({
            'filename': filename,
            'output': output,
            'title': title,
        })

        if title == 'INDEX':
            title = 'ABOUT'

        write_page(title, filename, output, pages)
    pprint.pprint(pages, indent = 2, width = 30)
main()
