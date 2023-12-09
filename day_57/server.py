from flask import Flask, render_template
import random
import datetime
import requests
import json

app = Flask(__name__)

@app.route('/')
def home(name=None):
    random_number = random.randint(1,10)
    return render_template("index.html", name=name, random_number=random_number, CURRENT_YEAR=datetime.datetime.now().strftime('%Y'))

@app.route("/guess/<name>")
def name_guess(name):
    agify_url = f'https://api.agify.io/?name={name}'
    agify_response = requests.get(agify_url)
    agify_json = json.loads(agify_response.text)
    agify_age = agify_json['age']

    genderize_url = f'https://api.genderize.io/?name={name}'
    genderize_response = requests.get(genderize_url)
    genderize_json = json.loads(genderize_response.text)
    genderize_gender = genderize_json['gender']

    return render_template("guess.html", name=name, genderize_gender=genderize_gender, agify_age=agify_age)

    # return f"<h1>Hey {name},</h1>" \
    #        f"<h2>I think you are {genderize_gender},</h2>" \
    #        f"<h3>And maybe {agify_age}. years old</h3>"

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_json = json.loads(blog_response.text)
    return render_template("blog.html", posts=blog_json)
if __name__ == "__main__":
    app.run(debug=True)