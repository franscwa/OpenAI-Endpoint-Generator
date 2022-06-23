"""
This is a Python program that uses the Openai API to generate a code completion. 
The program takes in user parameters from an HTML form and uses those parameters to generate a prompt. 
The prompt is then used to generate a code completion which is displayed on the HTML page. 
The program also has a feedback feature that allows users to send feedback to a database.
"""

from crypt import methods
import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from boto3 import resource

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

dynamodb = boto3.resource('api-gen-feedback', 
    aws_access_key_id=keys.ACCESS_KEY_ID,
     aws_secret_access_key=keys.SECRET_ACCESS_KEY,
      aws_session_token=keys.SESSION_TOKEN)
    


#OpenAI API call
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        #Gets user parameters from HTML form
        serverlang = request.form["serverlang"]
        dbprovider = request.form["dbprovider"]
        endpoints = request.form["endpoints"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(serverlang, dbprovider, endpoints),
            temperature=0.6,
            max_tokens=1024,
        )

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

#Sends feedback to DynamoDB

@app.route("/feedback", methods =("POST"))
def successFeedback(serverlang, dbprovider, endpoints, feedback):
   if request.method == "POST":
    thisPrompt = request.form["responseprompt"]
    response = FeedbackTable.put_item(
       Response = {
           'prompt'     : thisPrompt,
           'temperature'  : 0.5,
           'successful' : True,
           'top_p'  : 1
       }
     )

def failedFeedback(serverlang, dbprovider, endpoints, feedback):
   if request.method == "POST":
    thisPrompt = request.form["responseprompt"]
    response = FeedbackTable.put_item(
       Response = {
           'prompt'     : thisPrompt,
           'temperature'  : 0.5,
           'successful' : False,
           'top_p'  : 1
       }
     )
   


    


def generate_prompt(serverlang, dbprovider, endpoints):
    return """ Write a program in {} with {} to write API endpoints for the following {}.

    """.format(serverlang, dbprovider, endpoints)
