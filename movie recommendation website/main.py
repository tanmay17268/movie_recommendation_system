from flask import Flask, request, render_template
import pymongo
import user_based_collaborative
import item_based_collaborative
import matrix_factorization

myclient = pymongo.MongoClient("mongodb://tanmay28:tanmay28@movierecommendationsystem-shard-00-00-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-01-wvh6x.mongodb.net:27017,movierecommendationsystem-shard-00-02-wvh6x.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommendationSystem-shard-0&authSource=admin&retryWrites=true")
mydb = myclient["imdb"]
mycol = mydb["movies"]
mycol2 = mydb["ratings"]

def init_user_movie(ratings):
	user_ratings = mycol2.find()
	user_movie = []
	numOfUsers = 1
	for user in user_ratings:
		user_movie.append(user["movies"])
		numOfUsers += 1
	# Comment out these 2 lines, if we want the new user ratings to be added to the database. 1 minor change is also needed
	# data = {"userID":numOfUsers, "movies":ratings}
	# mycol2.insert_one("")
	user_movie.append(ratings)
	return user_movie

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", movies=list(mycol.find()))

@app.route('/', methods=['POST'])
def home_post_request():
	arr = []
	cnt = 0
	for field in request.form:
		if int(request.form[field]) > 0:
			cnt += 1
		arr.append(int(request.form[field]))
	if cnt < 10:
		return "Please rate at least 10 movies"
	user_movie = init_user_movie(arr)
	ubc_recommendations = user_based_collaborative.user_recommendations(user_movie, len(user_movie)-1)
	ibc_recommendations = item_based_collaborative.userRecommendations(user_movie, len(user_movie)-1)
	mf_recommendations = matrix_factorization.matrix_factorization(user_movie, len(user_movie)-1)
	
	ubc_movies = []
	ibc_movies = []
	mf_movies = []
	movieNum = 0
	for movie in mycol.find():
		if movieNum in ubc_recommendations:
			ubc_movies.append(movie)
		if movieNum in ibc_recommendations:
			ibc_movies.append(movie)
		if movieNum in mf_recommendations:
			mf_movies.append(movie)
		movieNum += 1

	return render_template("recommendations.html", ubc_movies=ubc_movies, ibc_movies = ibc_movies, mf_movies = mf_movies)

if __name__ == "__main__":
	app.run()