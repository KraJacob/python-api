import logging
import uuid
from datetime import datetime

from flask import request
from flask_restplus import Resource
from controllers.serializers import comment_post, comment_get
from controllers.restplus import api
from repositories.models import mongoConnection

log = logging.getLogger(__name__)
collection = mongoConnection("localhost", "demo", "recette")
ns = api.namespace('comments', description='Operations related to recipes')


@ns.route('/')
class CommentCollection(Resource):

    @api.marshal_list_with(comment_get)
    def get(self):
        """
            Returns list of recipes
        """
        comments = list(collection.find({}))
        return comments

    @api.response(201, 'Category successfully created.')
    @api.expect(comment_post)
    def post(self):
        """
        Creates a new comment
        """
        data = request.json
        data['_id'] = str(uuid.uuid4())
        collection.insert_one(data)
        return None, 201


@ns.route('/<string:id>')
@api.response(404, 'Recipe not found.')
class CommentItem(Resource):

    @api.marshal_with(comment_get)
    def get(self, id):
        """
            Returns a comment.
        """
        return collection.find_one({"_id": id})

    @api.response(204, 'Comment successfully updated.')
    @api.expect(comment_post)
    def put(self, id):
        """
        Updates a comment
        """
        data = request.json
        data['_id'] = id
        collection.replace_one(collection.find_one({'_id': id}), data, False)
        return None, 204

    @api.response(204, 'Comment successfully deleted.')
    def delete(self, id):
        """
        Deletes comment.
        """
        collection.delete_one(collection.find_one({'_id': id}))
        return None, 204
