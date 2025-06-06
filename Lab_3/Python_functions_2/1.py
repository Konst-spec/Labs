def highRated(movie):
    return movie["imdb"] > 5.5

def listOfMovies(movies):
    a = []
    for i in movies:
        if highRated(i):
            a.append(i)
    return a

def movesByCategory(movies, category):
    a = []
    for i in movies:
        if i["category"] == category:
            a.append(i)
    return a

def avgIMDB(movies):
    sum = 0
    for i in movies:
        sum += i["imdb"]
    return sum / len(movies)

def avgIMDBbyCategory(movies, category):
    a = movesByCategory(movies, category)
    return avgIMDB(a)

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(highRated(movies[0]))
print()
b = listOfMovies(movies)
print(b)
print()
c = movesByCategory(movies, "Suspense")
print(c)
print()
print(avgIMDB(movies))
print(avgIMDBbyCategory(movies, "Suspense"))