from flask_restplus import fields
from rest_api.api.restplus import api

params_contact = api.model('Whatsapp add contact', {
    'number': fields.String(required=True, description='Number'),
    'name': fields.String(required=False, description='Contact Name'),
})

params_msg = api.model('Whatsapp sedn message', {
    'target': fields.String(required=True, description='Target/Number'),
    'msg': fields.String(required=False, description='message'),
})
