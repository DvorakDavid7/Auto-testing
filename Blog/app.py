from blog import Blog

# konstanty
MENU_TEXT = "c- to create a blog, l- to list blogs, r- to read one, p- to create a post, q- quit: "
POST_TEMPLATE = "{}: {}"


blogs = dict()

def menu():
    print_blogs()
    selection = input(MENU_TEXT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection =="r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_TEXT)




def print_blogs():
    for key, blog in blogs.items():  # [(key,blog), (key, blog),...]
        print("- {}".format(blog))


def ask_create_blog():
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")
    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Enter the blog title you want to read: ")
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))



def ask_create_post():
    pass
