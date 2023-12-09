from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()

@app.route('/')
def home():
    blog_json = post.all_posts
    return render_template("index.html", posts=blog_json)

@app.route('/post/<id_num>')
def get_post(id_num):
    item_post = post.get_selected_post(id_num)
    return render_template("post.html", blog_post=item_post)

if __name__ == "__main__":
    app.run(debug=True)
