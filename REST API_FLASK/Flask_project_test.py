from flask import Flask  # First 5 lines are how you define an API
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)  # Wrapping inside a database


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes}, comments = {self.comments})"


# with app.app_context():
#     db.create_all()  # This code should be run only once, otherwise it will overwrite the existing database

names = {"Beray": {"age": 21, "gender": "male"},  # Dictionary
         "Edis": {"age": 21, "gender": "male"}}


class HelloWorld(Resource):     # Created a class, that inherits from Resource
    def get(self, name, age):   # Overriding get method, you can also do it for post, put...
        return {"name": name, "age": age}  # What the program will return (it should be key-map lookup,
        # JSON serializable


class Testing(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")
api.add_resource(Testing, "/test/<string:name>")  # adding resources,
# Testing is the class, /test is how you will call it,
# and after that you can add /<string(int)(boolean):name> for parameters

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)
video_put_args.add_argument("comments", type=int, help="Comments of the video", required=True)

videos = {}


def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid...")


def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")


class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204  # Delete successfully


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":  # should be written to start the program
    app.run(debug=True)  # debug=True is written only in developer mode!
