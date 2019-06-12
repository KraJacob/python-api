import logging
import uuid
from datetime import datetime

from flask import request
from flask_restplus import Resource
from controllers.serializers import startup_post, startup_get
from controllers.restplus import api
from repositories.models import mongoConnection

log = logging.getLogger(__name__)
collection = mongoConnection("localhost", "", "personnel")
ns = api.namespace('personnels', description='Operations related to recipes')


@ns.route('/')
class PersonnelCollection(Resource):

    @api.marshal_list_with(startup_get)
    def get(self):
        """
            Returns list of recipes
        """
        personnel = list(collection.find({}))
        return personnel

    @api.response(201, 'Category successfully created.')
    @api.expect(startup_post)
    def post(self):
        """
        Creates a new recipe
        """
        data = request.json
        data['_id'] = str(uuid.uuid4())
        collection.insert_one(data)
        return None, 201


@ns.route('/<string:id>')
@api.response(404, 'Personnel not found.')
class PersonnelItem(Resource):

    @api.marshal_with(startup_get)
    def get(self, id):
        """
            Returns a recipe with a list of posts.
        """
        return collection.find_one({"_id": id})

    @api.response(204, 'Personnel successfully updated.')
    @api.expect(startup_post)
    def put(self, id):
        """
        Updates a Personnel
        """
        data = request.json
        data['_id'] = id
        collection.replace_one(collection.find_one({'_id': id}), data, False)
        return None, 204

    @api.response(204, 'Personnel successfully deleted.')
    def delete(self, id):
        """
        Deletes blog Personnel.
        """
        collection.delete_one(collection.find_one({'_id': id}))
        return None, 204