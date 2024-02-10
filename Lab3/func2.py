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

# 1
def check():
    for movie in movies:
        if movie['imdb'] > 5.5:
            return True
        else:
            return False
check()
# 2
def check2():
    result = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            result += [movie["name"]]
    print(result)       
check2()
# 3
def check2():
    category = input()
    for movie in movies:
        if movie["category"] == category:
            return movie      
check2()
# 4
def check3(movies):
    result = ["What is the name", "We Two", "Ringing Crime"]
    final = 0.0
    for movie in movies:
        for i in range(len(result)):
            if movie["name"] == result[i]:
                final += movie["imdb"]
    print(final/len(result))
check3(movies)
# 5
def check3(movies):
    result = input()
    final = 0.0
    cou = 0
    for movie in movies:
        if movie["category"] == result:
            final += movie["imdb"]
            cou += 1
    print(final/cou)
check3(movies)
