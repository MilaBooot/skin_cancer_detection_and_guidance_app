from flask import Flask, request
#Workaround for the bug in https://github.com/jarus/flask-testing/issues/143
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields, abort
import json

flask_app = Flask(__name__)
app = Api(app = flask_app)

ml_api = app.namespace('mlService', description='ML service API')


class msgFormats:
	def default_msg(self, msg):
		return {"result": msg}

	def error_msg(self, errmsg):
		return {"error": errmsg}

	def data_msg(self, data):
		json_data = json.dumps(data)
		return {"result": {"data": data}}


class dataFields:
	def predict_data(self):
		reponse_dict = ml_api.model("reponse_dict", {"id":fields.String, "answer":fields.String})
		resource_fields = ml_api.model("ML predict data",
		   {'image': fields.List(fields.Integer(description="image", required=True)),
			'questions': fields.List(fields.Nested(reponse_dict, required=True))})
		return resource_fields


@ml_api.route("/predict")
class login(Resource):
	@ml_api.expect(dataFields().predict_data())
	@ml_api.response(200, 'Success')
	@ml_api.response(401, 'User ID not found')
	def post(self):
		json_data = request.json
		image = data["image"]
		response = data["questions"]
		print(image)
		print(response)
		#try:
	#		data = ldb.get_user_details(user_id)
#		except KeyError:#
			#abort(401, result=msgFormats().error_msg("User ID not found"))
		return msgFormats().data_msg(data)

