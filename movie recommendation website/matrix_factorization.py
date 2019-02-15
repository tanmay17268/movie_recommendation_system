import numpy
import pymongo

myclient=pymongo.MongoClient("mongodb://tanmay28:tanmay28@movierecommendationsystem-shard-00-00-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-01-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-02-wvh6x.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommendationSystem-shard-0&authSource=admin&retryWrites=true")
mydb = myclient["imdb"]
mycol1 = mydb["user_features"]
mycol2 = mydb["features_movie"]

def matrix_factorization(user_movie, usr):
    user_movie = numpy.array(user_movie)
    maxSteps = 15
    learningRate = 0.0002
    regularization = 0.02
    error = float('inf')
    numOfUsers = len(user_movie)
    numOfMovies = len(user_movie[0])

    numOfFeatures = 5

    # This is done so that the accuracy of prediction increases over time
    user_features = []
    for row in mycol1.find():
        user_features.append(row["features"])
    features_movie = []
    for row in mycol2.find():
        features_movie.append(row["movie"])
    user_features = numpy.array(user_features)
    features_movie = numpy.array(features_movie)

    while error>0.001 and maxSteps>0:
        for user in range(numOfUsers):
            for movie in range(numOfMovies):
                if user_movie[user][movie] != 0:
                    error_user_movie = user_movie[user][movie] - numpy.dot(user_features[user,:], features_movie[:,movie])
                    for feature in range(numOfFeatures):
                        user_features[user][feature] = user_features[user][feature] + learningRate*(2*error_user_movie*features_movie[feature][movie] - regularization*user_features[user][feature])
                        features_movie[feature][movie] = features_movie[feature][movie] + learningRate*(2*error_user_movie*user_features[user][feature] - regularization*features_movie[feature][movie])
        error = 0
        for user in range(numOfUsers):
            for movie in range(numOfMovies):
                if user_movie[user][movie] != 0:
                    error += ((user_movie[user][movie] - numpy.dot(user_features[user,:], features_movie[:,movie]))**2)
                    for feature in range(numOfFeatures):
                        error += ((regularization/2)*(user_features[user][feature]**2 + features_movie[feature][movie]**2))
        maxSteps -= 1
    
    user_id = 0
    for row in mycol1.find():
    	mycol1.update_one(row, { "$set" : {"userID":user_id, "features":list(user_features[user_id])} })
    	user_id += 1
    
    feature_no = 0
    for row in mycol2.find():
    	mycol2.update_one(row, { "$set" : {"feature":feature_no, "movie":list(features_movie[feature_no])} })
    	feature_no += 1
    
    new_user_movie = numpy.dot(user_features, features_movie)
    rank = []
    
    for movie in range(numOfMovies):
        if user_movie[usr][movie] == 0:
            rank.append((new_user_movie[usr][movie], movie))

    rank.sort(reverse = True)
    recommendList = [movie[1] for movie in rank]
    return recommendList[:10]

if __name__ == "__main__":
    user_movie_rating = [
        [2.5, 3.5, 3.0, 3.5, 2.5, 3.0],
        [3.0, 3.5, 1.5, 5.0, 3.5, 3.0],
        [2.5, 3.0, 0.0, 3.5, 0.0, 4.0],
        [0.0, 3.5, 3.0, 4.0, 2.5, 4.5],
        [3.0, 4.0, 2.0, 3.0, 2.0, 3.0],
        [3.0, 4.0, 0.0, 5.0, 3.5, 3.0],
        [0.0, 4.5, 0.0, 4.0, 1.0, 0.0]]
    print(matrix_factorization(user_movie_rating, 6))
