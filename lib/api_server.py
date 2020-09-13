from flask import Flask, request
import json
#Workaround for the bug in https://github.com/jarus/flask-testing/issues/143
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields, reqparse, abort
from lib.services.db_connect import loginDBConnect

flask_app = Flask(__name__)
app = Api(app = flask_app)

register_api = app.namespace('register', description='signup API')
user_validate_api = app.namespace("user_validate", description="user validation API")
common_services_api = app.namespace("common_services", description="common services API")

ldb = loginDBConnect()


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

	def login_creds(self):
		resource_fields = user_validate_api.model("Login credentials",
		   {'user_id': fields.String(description="Email ID of user", required=True),
			'password': fields.String(description="Encrypted password", required=True)
			})
		return resource_fields


@register_api.route("/")
class signUp(Resource):
	@register_api.expect(dataFields().user_reg())
	def post(self):
		json_data = request.json
		user_id = json_data["user_id"]
		password = json_data["password"]
		first_name = json_data["first_name"]
		last_name = json_data["last_name"]
		dob = json_data["dob"]
		gender = json_data["gender"]
		if user_id in ldb.get_user_ids():
			abort(409, "User ID already exists")
		ret = ldb.insert_value(user_id, password, first_name, last_name, dob, gender)
		return {"message": "User created", "result": ret}


@user_validate_api.route("/")
class login(Resource):
	@user_validate_api.expect(dataFields().login_creds())
	def post(self):
		pass
		#add login creds fetch function
		return {"message": "User Validated", "data": json.dumps(rows)}
