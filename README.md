Movie Recommendation System

File Directory Structure
1. mongoDB collections
    It contains the mongoDB collections in both .json and .wt format.
2. movie recommendation website
    It contains the source code of the frontend and the backend of my website, which can be found at https://tb-movie-recommendation-system.herokuapp.com/.
3. storing data in mongo_db
    It contains the python codes for storing necessary data in mongoDB.
    
Dependency Libraries
1. csv
    This was used to read the csv files obtained from movielens, which contained the imdb movie id and user ratings.
2. pymongo
    This was used to connect with our mongodb database.
3. imdb
    It was used to scrape the imdb website to obtain the movie name, year, genre, thumbnail image etc. using the movie id obtained from movielens.
4. numpy
    It was used to perform the dot operation of 2 matrices in the matrix factorization technique.
5. flask
    It was used to connect with the frontend and render post requests.

References:
1. F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872
2. Flask - https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492 
3. User-User collaborative filtering - http://dataaspirant.com/2015/05/25/collaborative-filtering-recommendation-engine-implementation-in-python/
4. Item-Item collaborative filtering - https://medium.com/@wwwbbb8510/python-implementation-of-baseline-item-based-collaborative-filtering-2ba7c8960590
5. Matrix Factorization - a) https://lazyprogrammer.me/tutorial-on-collaborative-filtering-and-matrix-factorization-in-python/
                          b) http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/
