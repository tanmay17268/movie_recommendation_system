#if number of users will increase we may use the similar users function to get numOfSimilarUsers similar users and then loop on them.
def similar_users(user_movie_rating, user1, numOfSimilarUsers):
    numOfUsers = len(user_movie_rating)
    pearson_correlation = []

    for user2 in range(numOfUsers):
        if user1 != user2:
            pearson_correlation.append([correlation(user_movie_rating,  user1, user2), user2])

    pearson_correlation.sort(reverse = True)
    return [pearson_correlation[usr][1] for usr in range(numOfSimilarUsers)]

