import logging

from flask import request
from flask_restplus import Resource
from rest_api.api.whatsapp.serializers import params_msg, params_contact
from rest_api.api.whatsapp.genstatic import StaticFile
from rest_api.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('api/whatsapp', description='')

@ns.route('/send')
class sendMsg(Resource):

    @api.expect(params_msg)
    def post(self):
        params = request.json
        file = StaticFile()
        data = file.send(params)
        return data
        return True

@ns.route('/add_contact')
class addContact(Resource):

    @api.expect(params_contact)
    def post(self):
        params = request.json
        file = StaticFile()
        data = file.add(params)
        return data
        return True