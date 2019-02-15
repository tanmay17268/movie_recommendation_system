def calculateAdjustedRatings(user_movie):
    numOfUsers = len(user_movie)
    numOfMovies = len(user_movie[0])
    mean = [0 for i in range(numOfMovies)]

    for movie in range(numOfMovies):
        rating_sum = 0
        users_rated = 0
        for user in range(numOfUsers):
            if user_movie[user][movie] != 0:
                rating_sum += user_movie[user][movie]
                users_rated += 1
        mean[movie] = 0 if users_rated == 0 else (rating_sum/users_rated)

    user_movie_adjusted_rating = [[] for user in range(numOfUsers)]
    for user in range(numOfUsers):
        for movie in range(numOfMovies):
            if user_movie[user][movie] != 0:
                if user_movie[user][movie]-mean[movie] != 0:
                    user_movie_adjusted_rating[user].append(user_movie[user][movie]-mean[movie])
                else:
                    user_movie_adjusted_rating[user].append(1e-8)
            else:
                user_movie_adjusted_rating[user].append(0)
    return mean, user_movie_adjusted_rating

def cosineSimilarity(user_movie):
    numOfUsers = len(user_movie)
    numOfMovies = len(user_movie[0])
    item_similarity = [[0 for i in range(numOfMovies)] for j in range(numOfMovies)]
    # the three tupleas in item_item_wt will be just used to calculate item_similarity for the cosine similiarity
    # first will store the sum of rating[movie1]*rating[movie2] rated by different users
    # second will store the sum of squares of rating[movie1] given by different users
    # third will store the sum of squares of rating[movie2] given by different users
    item_item_wt = [[[0, 0, 0] for i in range(numOfMovies)] for j in range(numOfMovies)]

    for movie1 in range(numOfMovies):
        for user in range(numOfUsers):
            if user_movie[user][movie1]==0:
                continue
            for movie2 in range(numOfMovies):
                if movie1==movie2 or user_movie[user][movie2]==0:
                    continue
                item_item_wt[movie1][movie2][0] += (user_movie[user][movie1]*user_movie[user][movie2])
                item_item_wt[movie1][movie2][1] += (user_movie[user][movie1]**2)
                item_item_wt[movie1][movie2][2] += (user_movie[user][movie2]**2)

        for movie2 in range(numOfMovies):
            if movie1==movie2 or item_item_wt[movie1][movie2][1]==0:
                continue
            item_item_wt[movie1][movie2][1] = item_item_wt[movie1][movie2][1]**0.5
            item_item_wt[movie1][movie2][2] = item_item_wt[movie1][movie2][2]**0.5
            num = item_item_wt[movie1][movie2][0]
            den = item_item_wt[movie1][movie2][1]*item_item_wt[movie1][movie2][2]
            den = 1e-8 if den == 0 else den
            item_similarity[movie1][movie2] = num/den
    return item_similarity

def predictedRating(user, movie1, item_item, user_movie, movies_rating_mean):
    mean_movie1 = 2.5 if movies_rating_mean[movie1] == 0 else movies_rating_mean[movie1]
    numOfMovies = len(user_movie[0])
    ratings_sum, weights_sum = 0, 0

    for movie2 in range(numOfMovies):
        if movie2 == movie1 or user_movie[user][movie2] == 0 or item_item[movie1][movie2] == 0:
            continue
        mean_movie2 = 2.5 if movies_rating_mean[movie2] == 0 else movies_rating_mean[movie2]
        ratings_sum += ((user_movie[user][movie2] - mean_movie2)*item_item[movie1][movie2])
        weights_sum += abs(item_item[movie1][movie2])
    
    if weights_sum ==0:
        return mean_movie1
    return mean_movie1 + ratings_sum/weights_sum

def userRecommendations(user_movie, user):
    movies_rating_mean, user_movie_adjusted_rating = calculateAdjustedRatings(user_movie)
    item_item_similarity = cosineSimilarity(user_movie_adjusted_rating)
    numOfMovies = len(user_movie[0])
    rank = []

    for movie in range(numOfMovies):
        if user_movie[user][movie] == 0:
            usr_rating = predictedRating(user, movie, item_item_similarity, user_movie, movies_rating_mean)
            rank.append((usr_rating, movie))

    rank.sort(reverse = True)
    recommendList = [movie[1] for movie in rank]
    return recommendList[:10]

if __name__ == "__main__":
    user_movie = [
        [2.5, 3.5, 3.0, 3.5, 2.5, 3.0],
        [3.0, 3.5, 1.5, 5.0, 3.5, 3.0],
        [2.5, 3.0, 0.0, 3.5, 0.0, 4.0],
        [0.0, 3.5, 3.0, 4.0, 2.5, 4.5],
        [3.0, 4.0, 2.0, 3.0, 2.0, 3.0],
        [3.0, 4.0, 0.0, 5.0, 3.5, 3.0],
        [0.0, 4.5, 0.0, 4.0, 1.0, 0.0]]
    print(userRecommendations(user_movie, 6))
    
