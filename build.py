import glob
import os
import pprint

# def pages():
#     return []
    
def write_page(title, filename, output):
    template = open('templates/base.html').read()
    content = open(filename).read()
    combined_content = template.replace('{{content}}', content).replace('{{title}}', title)

    if title == 'About':
        combined_content = combined_content.replace('{{about_xtra_class}}', 'active').replace('{{linkedin}}', 'about-linkedin').replace('{{github}}', 'about-github')
    elif title == 'Blog':
        combined_content = combined_content.replace('{{blog_xtra_class}}', 'active').replace('{{linkedin}}', 'blog-linkedin').replace('{{github}}', 'blog-github')
    elif title == 'Contact':
        combined_content = combined_content.replace('{{contact_xtra_class}}', 'active').replace('{{linkedin}}', 'contact-linkedin').replace('{{github}}', 'contact-github')
    else: pass

    open(output, 'w+').write(combined_content)
    
    

def main():
    all_html_files = glob.glob('contents/*.html')
    all_output_files = glob.glob('docs/*.html')

    pages=[]
    for files, file in zip(all_html_files, all_output_files):
        filename = os.path.relpath(files)
        output = os.path.relpath(file)
        title_parse = os.path.basename(filename)
        title, extension = os.path.splitext(title_parse)

        pages.append({
            'filename': filename,
            'output': output,
            'title': title,
        })
    pprint.pprint(pages, indent = 2, width = 30)
main()
