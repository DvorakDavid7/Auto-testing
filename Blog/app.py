MENU_TEXT = "c- to create a blog, l- to list blogs, r- to read one, p- to create a post, q- quit: "
# konstanta

blogs = dict()

def menu():
    print_blogs()
    selection = input(MENU_TEXT)


def print_blogs():
    for key, blog in blogs.items():  # [(key,blog), (key, blog),...]
        print("- {}".format(blog))
