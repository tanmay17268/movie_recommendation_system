import csv
import imdb
import pymongo

f = open('links.csv', 'r')

# please replace the <PASSWORD> with the password to run the code
myclient=pymongo.MongoClient("mongodb://tanmay28:<PASSWORD>@movierecommendationsystem-shard-00-00-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-01-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-02-wvh6x.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommendationSystem-shard-0&authSource=admin&retryWrites=true")
mydb = myclient["imdb"]
mycol = mydb["movies"]

csv_links_reader = csv.reader(f)

fields_links = next(csv_links_reader)
genres = {"Comedy":0, "Sci-Fi":0, "Horror":0, "Romance":0, "Action":0, "Thriller":0, "Drama":0, "Mystery":0, "Crime":0, "Adventure":0, "Fantasy":0, "Documentary":0}
z = 0

for row in csv_links_reader:
    z += 1
    imdbID = row[1]
    access = imdb.IMDb()
    movie = access.get_movie(imdbID)
    data = {}
    try:
        data = {"title":movie['title'], "year":movie['year'], "thumbnail_image":movie['cover url'], "genre":movie['genres'], "rating":movie['rating'], "synopsis":movie["synopsis"]}
    except:
        data = {"title":movie['title'], "year":movie['year'], "thumbnail_image":movie['cover url'], "genre":movie['genres'], "rating":movie['rating'], "synopsis":movie["plot"]}
    
    mycol.insert_one(data)
    print(z, movie['title'])

    genre = movie['genres']
    for i in genre:
        if(i in genres):
            genres[i] += 1

    flag = 0    #Stop reading movies if at least 10 movies of each popular genre is stored
    for i in genres.keys():
        if genres[i]<10:
            flag = 1
    if flag==0:
        break

f.close()
