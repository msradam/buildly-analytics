from flask import Flask
from flask_restplus import Resource, Api

from docker_hub_analytics import retrieve_hub_repo_data
from github_analytics import retrieve_repo_data
from gitter import gitter

app = Flask(__name__)
api = Api(app)

@api.route('/docker_hub')
class DockerHubAnalytics(Resource):
    def get(self):
        return retrieve_hub_repo_data.get_hub_analytics_json()


@api.route('/github')
class GithubAnalytics(Resource):
    def get(self):
        return retrieve_repo_data.get_github_meta()


@api.route('/gitter')
class GitterAnalytics(Resource):
    def get(self):
        return gitter.get_chat_meta()


if __name__ == '__main__':
    app.run()

