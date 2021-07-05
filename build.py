print('building ssg')

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
index = open('html/index.html', 'w+').write(index_html)
blog = open('html/blog.html', 'w+').write(blog_html)
contact = open('html/contact.html', 'w+').write(contact_html)
