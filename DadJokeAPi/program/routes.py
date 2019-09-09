from program import app
from flask import render_template, request
from program.jokeinventory import assets
import random


@app.route('/')
@app.route('/index')
def index():
    dadjoke = get_dad_joke()
    return render_template('index.html', dadjoke=dadjoke)

def get_dad_joke():
    n = random.randint(0, (len(assets)-1))
    dadjoke = assets[n]['joke']
    print(dadjoke)
    return dadjoke

"""
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
"""
