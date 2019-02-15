"""
	It creates the 2 matrices needed in matrix factorization recommendation system and store them in MongoDB.
	Since we want to get better result everytime we call matrix factorization method, so we will store the 2 matrices and won't create them randomly everytime.
	This will help us to reduce the error in their product.
	Otherwise initizialing the 2 matrices with random value everytime won't make our search results better over time.
"""
import pymongo
import numpy

# please replace the <PASSWORD> with the password to run the code
myclient=pymongo.MongoClient("mongodb://tanmay28:<PASSWORD>@movierecommendationsystem-shard-00-00-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-01-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-02-wvh6x.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommendationSystem-shard-0&authSource=admin&retryWrites=true")
mydb = myclient["imdb"]
mycol1 = mydb["user_features"]

mycol2 = mydb["features_movie"]
numOfUsers = 621
numOfMovies = 376
numOfFeatures = 5

user_features = numpy.random.rand(numOfUsers, numOfFeatures)
user = 0
for i in user_features:
    data = {"userID":user, "features":list(i)}
    mycol1.insert_one(data)
    user += 1
features_movie = numpy.random.rand(numOfFeatures, numOfMovies)
feature = 0
for i in features_movie:
    data = {"feature":feature, "movie":list(i)}
    mycol2.insert_one(data)
    feature += 1
