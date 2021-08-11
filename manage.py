from utils import main
import sys


def manage_py():
    new_contents = '''
    <div class='row-fluid'>
        <div class='col-fluid'>
        <h1> New Content! </h1>
        </div>
    </div>
    '''
    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        main()
    elif command == "new":
        print("New page was specified")
        open('contents/new_content_page.html', 'w+').write(new_contents)
    else:
        print(
            '''Usage:
            Rebuild site: python manage.py build
            Create new page: python manage.py new'''
        )
manage_py()