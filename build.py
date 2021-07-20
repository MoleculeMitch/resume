# phase1: refactor this code into a main() function
#phase2: write a forloop that loops through the list/dict and executes the templating
def get_pages():
    return [{
        'filename': 'contents/index.html',
        'output': 'docs/index.html',
        'title': 'About',
    },
    {
        'filename': 'contents/blog.html',
        'output': 'docs/blog.html',
        'title': 'Blog',
    },
    {
        'filename': 'contents/contact.html',
        'output': 'docs/contact.html',
        'title': 'Contact',
    }] 


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
    for page in get_pages():
        title = page['title']
        filename = page['filename']
        output = page['output']
        print('filename =', filename, 'title =', title, 'output =', output)
        write_page(title, filename, output)

main()

