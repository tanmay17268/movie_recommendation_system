Movie Recommendation System

File Directory Structure
1. mongoDB collections
    It contains the mongoDB collections in both .json and .wt format.
2. movie recommendation website
    It contains the source code of the frontend and the backend of my website, which can be found at https://tb-movie-recommendation-system.herokuapp.com/.
3. storing data in mongo_db
    It contains the python codes for storing necessary data in mongoDB.
    
Dependency Libraries
1. csv - 
    This was used to read the csv files obtained from movielens, which contained the imdb movie id and user ratings.
2. pymongo - 
    This was used to connect with our mongodb database.
3. imdb - 
    It was used to scrape the imdb website to obtain the movie name, year, genre, thumbnail image etc. using the movie id obtained from movielens.
4. numpy - 
    It was used to perform the dot operation of 2 matrices in the matrix factorization technique.
5. flask - 
    It was used to connect with the frontend and render post requests.
    
Codebase
1. storing_data_in_mongo_db/storing_movies_in_mongo_db.py - 
    It creates a collection called movies in the mongodb database. Each document in the collection contains the following fields - title (title of the movie), year (year of realease of the movie), thumbnail_image, rating (imdb rating of the movie), synopsis (summary of the movie). The above information about a movie is obtained from the imdb library, which takes an imdb_movie_id as input and returns a json string containing the above information. The imdb_movie_id is obtained from the links.csv file (downloaded from movielens). Some of the popular genres were stored in the dictionary to maintain a count of how many movies of each genre is recorded. As soon as at least 10 movies of each genre is read, we will stop reading the csv file further. This was done so as to ensure that some number of movies from each genre is present.

2. storing_data_in_mongo_db/creating_dummy_users.py
    It creates a collection called ratings in the mongodb database. Each document in the collection contains the following fields - userID (unique number assigned to each user to identify them distinctly), movies (A list of ratings given by the user for every movie, if the user hasn't rated the movie, the default rating is considered as 0). The above information about the user ratings was obtained by reading the ratings.csv file obtained from movielens. In short it created dummy users which will be later needed for the collaborative filtering.
    
3. storing_data_in_mongo_db/matrix_factor.py
    It creates 2 collection - user_features, features_movie. These store the data of two factorized matrices, which will be used in matrix_factorization. Since we want to improve our search result with every search result, therefore the state of the matrices after minimizing the error will be stored.

4. movie_recommendation_website/main.py
    It controls the backend of my flask website, i.e. where should each link be redirected and how to handle the post request.

5. movie_recommendation_website/user_based_collaborative.py
    It returns 10 movies, that a user should watch depending upon his current preferences. It uses the user_based_collaborative method to find these 10 movies. Users will be rated similar using the pearson correlation formula.

6. movie_recommendation_website/item_based_collaborative.py
    It returns 10 movies, that a user should watch depending upon his current preferences. It uses the item_based_collaborative method to find these 10 movies. Items will be rated similar using the cosine similarity.
    
7. movie_recommendation_website/matrix_factorization.py
    It returns 10 movies, that a user should watch depending upon his current preferences. It uses the matrix factorization technique to find these 10 movies. The bigger matrix is factorized into 2 smaller matrices of size (numOfUsers)X5 and 5%(numOfMovies).

References:
1. F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872
2. Flask - https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492 
3. User-User collaborative filtering - http://dataaspirant.com/2015/05/25/collaborative-filtering-recommendation-engine-implementation-in-python/
4. Item-Item collaborative filtering - https://medium.com/@wwwbbb8510/python-implementation-of-baseline-item-based-collaborative-filtering-2ba7c8960590
5. Matrix Factorization - a) https://lazyprogrammer.me/tutorial-on-collaborative-filtering-and-matrix-factorization-in-python/
                          b) http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/
