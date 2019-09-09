from program import app
from flask import render_template, request
from datetime import datetime

import requests
import json



@app.route('/')
@app.route('/index')
def index():
    timenow = str(datetime.today())
    return render_template('index.html', time=timenow)


@app.route('/100days')
def p100days():
    return render_template('100days.html')


@app.route('/chuckjokes')
def chuck():
    joke = get_chuck_jokes()
    return render_template('chuckjokes.html', joke=joke)


def get_chuck_jokes():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokecolor' in request.form:
        color = request.form.get('pokecolor')
        pokemon = get_poke_color(color)
    return render_template('pokemon.html', pokemon=pokemon)


def get_poke_color(color):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + color.lower())
    if r.status_code >= 500:
        print("No such color")
    else:
        pokedata = r.json()
        pokemon = []

        for i in pokedata['pokemon_species']:
            pokemon.append(i['name'])
    return pokemon

