def correlation(user_movie_rating, user1, user2):
    usr1_mean, usr1_movies, usr2_mean, usr2_movies, usr1_sq_pref, usr2_sq_pref, prod_sum = 0, 0, 0, 0, 0, 0, 0
    numOfMovies = len(user_movie_rating[0])

    for movie in range(numOfMovies):
    	if user_movie_rating[user1][movie]!=0:
    		usr1_mean += user_movie_rating[user1][movie]
    		usr1_movies += 1
    	if user_movie_rating[user2][movie]!=0:
    		usr2_mean += user_movie_rating[user2][movie]
    		usr2_movies += 1
    
    if usr2_movies == 0:
    	return 0
    usr1_mean = usr1_mean/usr1_movies
    usr2_mean = usr2_mean/usr2_movies

    for movie in range(numOfMovies):
        if user_movie_rating[user1][movie]!=0 and user_movie_rating[user2][movie]!=0:
            prod_sum += ((user_movie_rating[user1][movie] - usr1_mean)*(user_movie_rating[user2][movie] - usr2_mean))
            usr1_sq_pref += ((user_movie_rating[user1][movie] - usr1_mean)**2)
            usr2_sq_pref += ((user_movie_rating[user2][movie] - usr2_mean)**2)

    num = prod_sum
    den = ((usr1_sq_pref*usr2_sq_pref)**0.5)
    return 0 if den == 0 else (num/den)

def user_recommendations(user_movie_rating, user1):
    numOfMovies = len(user_movie_rating[0])
    numOfUsers = len(user_movie_rating)
    movies = [[0, 0] for i in range(numOfMovies)]
    for user2 in range(numOfUsers):
        if user1 == user2:
            continue
        similarity = correlation(user_movie_rating, user1, user2)
        for movie in range(numOfMovies):
            if user_movie_rating[user2][movie]!=0 and user_movie_rating[user1][movie]==0:
                movies[movie][0] += (user_movie_rating[user2][movie]*similarity)
                movies[movie][1] += similarity
    rank = []
    for movie in range(numOfMovies):
        if movies[movie][1]!=0:
            rank.append((movies[movie][0]/movies[movie][1], movie))
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
    print(user_recommendations(user_movie_rating, 6))
