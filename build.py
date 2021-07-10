# phase1: refactor this code into a main() function
def main():
    print('building ssg')
    pages = [{
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

    for page in pages:
        title = page['title']
        file_name = page['filename']
        output = page['output']


# variables that read top and bottom html
    top_html = open('templates/top.html').read()
    bottom_html = open('templates/bottom.html').read()

#variables that read the middle contents of html
    mid_index_html = open('contents/index.html').read()
    mid_blog_html = open('contents/blog.html').read()
    mid_contact_html = open('contents/contact.html').read()

# combining tops + html middle contents + bottoms
    index_html = top_html + mid_index_html + bottom_html
    blog_html = top_html + mid_blog_html + bottom_html
    contact_html = top_html + mid_contact_html + bottom_html

#writing/creating the new html pages: stored in html directory
    open('docs/index.html', 'w+').write(index_html)
    open('docs/blog.html', 'w+').write(blog_html)
    open('docs/contact.html', 'w+').write(contact_html)


main()

# phase1 of main() is currently is currently functioning