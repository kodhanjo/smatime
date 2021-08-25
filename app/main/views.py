import os
from flask import render_template,request,redirect,url_for, abort, flash
from . import main


@main.route('/')
def index():
    items= [
        {'ID': 1, "image": '#', 'name': 'blackhair', 'price': 50},
        {'ID': 2, "image": '#', 'name': 'Box', 'price': 90},
        {'ID': 3, "image": '#', 'name': 'beards', 'price': 70},
        {'ID': 4, "image": '#', 'name': 'dreadlocks', 'price': 55},
        {'ID': 5, "image": '#', 'name': 'banana', 'price': 65},
        {'ID': 6, "image": '#', 'name': 'Facialhair', 'price': 75},
        {'ID': 7, "image": '#', 'name': 'buzzcut', 'price': 80},
        {'ID': 8, "image": '#', 'name': 'fade', 'price': 120}
    ]
    return render_template('index.html', items=items)


