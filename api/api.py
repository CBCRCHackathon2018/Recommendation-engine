from flask import Flask
from flask import jsonify
import json
from pprint import pprint
from random import randint

from SmartParser import SmartParser
from SearchPhotos import PhotoSearch

app = Flask(__name__)

@app.route('/')
def index():
    return 'This API is for the CBCRAHackathon - Team PaypalGang'

@app.route("/shows/<userId>")
def get_shows(userId):

    user_keywords = get_user_keywords(userId)

    with open('show_data.json') as f:
        data = json.load(f)

        for d in data:
            show_keywords = get_show_keywords(d["description"].split('.')[0])
            d["image"] = get_show_image(show_keywords, user_keywords)

    return jsonify(data)

def get_user_keywords(userId):

    with open('user_keywords.json') as f:
        data = json.load(f)
        for d in data:
            if d["id"] == userId:
                return d["keywords"]

    #fallback if user doesn't exist
    return "canada radio"

def get_show_keywords(description):
    sp = SmartParser()
    sp.SetText(description)
    return sp.NounChunks()

def get_show_image(showKeywords, userKeywords):
    pexels = PhotoSearch()
    keywords = showKeywords + userKeywords.split(' ')
    response = pexels.MakeRequest(keywords)
    number_of_photos = len(response['photos'])
    picture = response['photos'][randint(0, number_of_photos - 1)]['src']['medium']
    return picture
