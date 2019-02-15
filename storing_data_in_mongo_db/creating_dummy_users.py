import csv
import pymongo

f = open('ratings.csv','r')

# please replace the <PASSWORD> with the password to run the code
myclient=pymongo.MongoClient("mongodb://tanmay28:<PASSWORD>@movierecommendationsystem-shard-00-00-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-01-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-02-wvh6x.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommendationSystem-shard-0&authSource=admin&retryWrites=true")
mydb = myclient["imdb"]
mycol = mydb["ratings"]

csv_ratings_reader = csv.reader(f)
numOfUsers = 620
numOfMovies = 376

fields_ratings = next(csv_ratings_reader)
user = [-1 for i in range(numOfUsers)]
user_movie = [[0 for i in range(numOfMovies)] for j in range(numOfUsers)]

usr = 0
for row in csv_ratings_reader:
    row[0] = int(row[0])
    row[1] = int(row[1])
    row[2] = float(row[2])
    if row[1]>376:
        continue
    if user[row[0]] == -1:
        user[row[0]] = usr
        usr += 1
    user_movie[user[row[0]]][row[1]-1] = row[2]

for i in range(numOfUsers):
    data = {"userID":i, "movies":user_movie[i]}
    mycol.insert_one(data)
    
f.close()
