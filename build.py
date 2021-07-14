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
#  get pages returns the list of dict get_pages()
def write_page(title, filename, output):
    template = open('templates/base.html').read() 
    content = open(filename).read()
    combined_content = template.replace('{{content}}', content)
    open(output, 'w+').write(combined_content)

def main():
    for page in get_pages():
        title = page['title']
        filename = page['filename']
        output = page['output']
        print('filename =', filename, 'title =', title, 'output =', output)
        write_page(title, filename, output)      
main()




# variables that read top and bottom html
    # top_html = open('templates/top.html').read()
    # bottom_html = open('templates/bottom.html').read()

#variables that read the middle contents of html
    # mid_index_html = open('contents/index.html').read()
    # mid_blog_html = open('contents/blog.html').read()
    # mid_contact_html = open('contents/contact.html').read()    

# combining tops + html middle contents + bottoms
    # index_html = top_html + mid_index_html + bottom_html
    # blog_html = top_html + mid_blog_html + bottom_html
    # contact_html = top_html + mid_contact_html + bottom_html

#writing/creating the new html pages: stored in html directory, this is the output
    # open('docs/index.html', 'w+').write(index_html)
    # open('docs/blog.html', 'w+').write(blog_html)
    # open('docs/contact.html', 'w+').write(contact_html)


#def main():
#     name= 'dan'
#     func(name)
#def func(name):
#     print('hello', name)
# main()

