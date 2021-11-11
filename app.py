from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/films/list')
def get_Films():

    filmsList = []

    with open('films.csv', 'r') as filmsCsv:
        reader = csv.reader(filmsCsv)
        
        for row in reader:
            filmsList.append({'title': row[0], 'rating':row[1]})

    return render_template('films.html', filmsList=filmsList) 

@app.route('/films/table')
def films_filter():

    stars = request.values.get("stars","")

    filmsList = []
    with open('films.csv', 'r') as filmsCsv:
        reader = csv.reader(filmsCsv)
        for row in reader:
            if row[1] == stars:
                filmsList.append({'title': row[0], 'rating':row[1]})
            

    return render_template('films.html', filmsList=filmsList)
    