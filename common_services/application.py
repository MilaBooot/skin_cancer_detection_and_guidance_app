from flask import Flask, request, redirect
#Workaround for the bug in https://github.com/jarus/flask-testing/issues/143
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields, abort, reqparse, inputs
from services.db_connect import dbConnect
import json

application = flask_app = Flask(__name__)
app = Api(app = flask_app)

register_api = app.namespace('register', description='signup API')
user_validate_api = app.namespace("getUserDetails", description="user validation API")
common_services_api = app.namespace("commonServices", description="common services API")

db = dbConnect()


class msgFormats:
	def default_msg(self, msg):
		return {"result": msg}

	def error_msg(self, errmsg):
		return {"error": errmsg}

	def data_msg(self, data):
		json_data = json.dumps(data)
		return {"result": {"data": data}}


class dataFields:
	def user_reg(self):
		resource_fields = register_api.model("User Registration Data",
		   {'first_name': fields.String(description="First Name", required=True),
			'last_name': fields.String(desription="Last Name", required=True),
			'user_id': fields.String(description="Email ID of user", required=True),
			'password': fields.String(description="Encrypted password", required=True),
			"dob": fields.DateTime(description="Date ofr Birth", dt_format="rfc822", required=True),
			"gender": fields.String(description="Gender", required=True)
			})
		return resource_fields

	def add_record(self):
		resource_fields = common_services_api.model("Add Record Data",
		   {'userId': fields.String(description="Email ID of user", required=True),
			'filename': fields.String(description="Filename to save", required=True),
			'description': fields.String(description="Description of file", required=True),
			"fileByteString": fields.String(description="Byte String of the image", required=True)
			})
		return resource_fields


class reqparseArgs:
	def get_user_details(self):
		parser = reqparse.RequestParser()
		parser.add_argument('user_id', default=None, required=True)
		return parser

	def get_doc_list(self):
		parser = reqparse.RequestParser()
		parser.add_argument('latitude', type=float, default=None, required=True)
		parser.add_argument('longitude', type=float, default=None, required=True)
		return parser


@register_api.route("/")
class signUp(Resource):
	@register_api.expect(dataFields().user_reg())
	@register_api.response(200, 'User Created')
	@register_api.response(409, 'User ID already exists')
	@register_api.response(400, 'Insert failed due to bad input')
	def post(self):
		json_data = request.json
		user_id = json_data["user_id"]
		password = json_data["password"]
		first_name = json_data["first_name"]
		last_name = json_data["last_name"]
		dob = json_data["dob"]
		gender = json_data["gender"]
		if user_id in db.get_user_ids():
			abort(409, result=msgFormats().error_msg("User ID already exists"))
		try:
			ret = db.insert_value(user_id, password, first_name, last_name, dob, gender)
		except Exception as err:
			abort(400, result=msgFormats().error_msg(str(err)))
		return msgFormats().default_msg("User Added")


@user_validate_api.route("")
class login(Resource):
	@user_validate_api.response(200, 'Found user detail')
	@user_validate_api.response(401, 'User ID not found')
	@user_validate_api.expect(reqparseArgs().get_user_details())
	def get(self):
		user_id =  request.args.get("user_id", None)
		if user_id is None:
			abort(400, result=msgFormats().error_msg("Bad Request. Missing user_id parameter"))
		try:
			data = db.get_user_details(user_id)
		except KeyError:
			abort(401, result=msgFormats().error_msg("User ID not found"))
		return msgFormats().data_msg(data)


@common_services_api.route("/getDoctors")
class getDocList(Resource):
	@common_services_api.response(200, 'Found doctors nearby')
	@common_services_api.response(401, 'Unservicable area')
	@common_services_api.expect(reqparseArgs().get_doc_list())
	def get(self):
		longitude = request.args.get("longitude", None)
		latitude = request.args.get("latitude", None)
		if longitude is None or latitude is None:
			abort(400, result=msgFormats().error_msg("Bad Request. Incomplete location details"))
		data = db.get_doctors(latitude, longitude)
		return msgFormats().data_msg(data)


@common_services_api.route("/getQuestions")
class getQuestions(Resource):
	@common_services_api.response(200, 'Success')
	def get(self):
		data = db.get_questions()
		return msgFormats().data_msg(data)


@common_services_api.route("/getQuestions/<id>")
class getQuestions(Resource):
	@common_services_api.response(200, 'Success')
	@common_services_api.response(401, 'Resource not found')
	def get(self, id):
		id = int(id)
		try:
			data = db.get_questions(id)
		except KeyError:
			abort(401, result="question id NOT FOUND")
		return msgFormats().data_msg(data)


@common_services_api.route("/addRecord")
class addRecord(Resource):
	@common_services_api.expect(dataFields().add_record())
	@common_services_api.response(200, '{"result": "Record added"}')
	@common_services_api.response(400, '{"result": {"error": "Filename already exists"}}')
	def post(self):
		record_data = request.json
		user_id = record_data.get("userId")
		filename = record_data.get("filename")
		description = record_data.get("description")
		file_bytestr = record_data.get("fileByteString")
		try:
			db.insert_record(user_id, filename, description, file_bytestr)
		except Exception as errmsg:
			abort(400, result=msgFormats().error_msg(str(errmsg)))
		return msgFormats().default_msg("Record Added")

if __name__ == "__main__":
	flask_app.run(debug=True)
