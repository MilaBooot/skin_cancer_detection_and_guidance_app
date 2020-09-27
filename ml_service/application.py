from flask import Flask, request
#Workaround for the bug in https://github.com/jarus/flask-testing/issues/143
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, fields, abort
import json
import base64
from PIL import Image
import io
import numpy as np
import cv2
from hackathon_ml_api_wrapper import predict_cancer

application = flask_app = Flask(__name__)
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
		   {'image': fields.String(description="image", required=True),
			'questions': fields.List(fields.Nested(reponse_dict, required=True))})
		return resource_fields


@ml_api.route("/predict")
class login(Resource):
	@ml_api.expect(dataFields().predict_data())
	@ml_api.response(200, '{result:{"data":{"cancer":"yes/no", "value":proablity value (float), \
	"type": "type of cancer predicted", "Risk Factor": (Low/Medium/High)}}}')
	@ml_api.response(401, 'User ID not found')
	def post(self):
		json_data = request.json
		image = json_data["image"]
		response = json_data["questions"]
		image_data = self.convert_imgdata(image)
		try:
			data = predict_cancer(image_data, response)
		except KeyError:
			abort(401, result=msgFormats().error_msg("User ID not found"))
		return msgFormats().data_msg(data)

	def convert_imgdata(self, img_str):
		imgdata = base64.b64decode(img_str)
		image = Image.open(io.BytesIO(imgdata))
		return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


if __name__ == "__main__":
        application.run(host="0.0.0.0", port=5001, debug=True)
