from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return "{} by {} ({} post{})".format(self.title,
                                           self.author,
                                           len(self.posts),
                                            's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        # do pole posts přidáme objekt Post
        a = Post(title, content)
        self.posts.append(a)


    def json(self):
        # v poli posts jsou objekty na které se postupně aplikuje motoda .json()
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts], # Post("a","b").json()
        }
