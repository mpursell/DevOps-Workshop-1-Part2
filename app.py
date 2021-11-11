from flask import Flask, render_template
from flask import request 
from werkzeug.utils import redirect
import csv

app = Flask(__name__)

def append_CSV(film, rating):
    with open('films.csv', 'a') as csv:

        string = film + ',' + rating
        csv.write(string + '\n')

    csv.close()



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
    filmsCsv.close()
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
            
    filmsCsv.close()
    return render_template('films.html', filmsList=filmsList)

@app.route('/films/submit', methods = ['POST'])
def submit_film():

    filmName = request.form.get('Film')
    rating = request.form.get('Stars')

    append_CSV(filmName, rating)

    return render_template('/films/submit')
    