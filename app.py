import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        serverlang = request.form["serverlang"]
        dbprovider = request.form["dbprovider"]
        endpoints = request.form["endpoints"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Code an EXPRESS program with a Postgres database with endpoints for the following GET all countries with stats, PUT new country with stats",
            #prompt=generate_prompt(serverlang, dbprovider, endpoints),
            temperature=0.8,
            max_tokens=512,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(serverlang, dbprovider, endpoints):
    return """ Code a {0} program with a {1} database with {2} endpoints for the following.

    """.format(serverlang, dbprovider, endpoints)