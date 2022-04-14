import sqlite3

# Connect to the database (new/existing)
db = sqlite3.connect('mydb.db')
cursor = db.cursor()

movies = [
    {'title': 'Zero', 'year': 2018, 'director': 'Aanand L Rai', 'actor': 'Shah Rukh Khan', 'actress': 'Anushka Sharma'},
    {'title': 'Bajrangi Bhaijaan', 'year': 2015, 'director': 'Kabir Khan', 'actor': 'Salman Khan', 'actress': 'Kareena Kapoor'},
    {'title': 'Ek Tha Tiger', 'year': 2012, 'director': 'Kabir Khan', 'actor': 'Salman Khan', 'actress': 'Katrina Kaif'},
    {'title': '3 Idiots', 'year': 2009, 'director': 'R K Hirani', 'actor': 'Aamir khan', 'actress': 'Kareena Kapoor'},
    {'title': 'Tees Maar Khan', 'year': 2008, 'director': 'Farah Khan', 'actor': 'Akshay Kumar', 'actress': 'Katrina Kaif'},
    {'title': 'Chennai Express', 'year': 2013, 'director': 'Rohit Shetty', 'actor': 'Shah Rukh Khan', 'actress': 'Deepika Padukone'},
    {'title': 'Om Shanti Om', 'year': 2007, 'director': 'Farah Khan', 'actor': 'Shah Rukh Khan', 'actress': 'Deepika Padukone'}
]

# Creating table 'Movies'
cursor.execute("CREATE TABLE Movies14 (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Inserting data into the table
for movie in movies:
    cursor.execute(f"INSERT INTO Movies VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select all movies
print("\nSelect all movies:")
cursor.execute("SELECT * FROM Movies;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'Shah Rukh Khan'
print("Select all movies with the actor 'Shah Rukh Khan':")
cursor.execute("SELECT title, year, director FROM Movies WHERE actor='Shah Rukh Khan';")
for i in cursor.fetchall():
    print(i)
print("\n")


# Printing the table in a dataframe
# import pandas as pd
# print(pd.read_sql("SELECT * FROM Movies;", db),end="\n\n")
# print(pd.read_sql("SELECT title, year, director FROM Movies WHERE actor='Shah Rukh Khan';", db))