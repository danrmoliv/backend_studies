import requests
import json

class Post:
    def __init__(self):
        self.get_all_posts()

    def get_all_posts(self):
        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        blog_response = requests.get(blog_url)
        blog_json = json.loads(blog_response.text)
        self.all_posts = blog_json
        return blog_json

    def get_selected_post(self, id_post):
        for post_item in self.all_posts:
            if str(post_item['id']) == str(id_post):
                return post_item

