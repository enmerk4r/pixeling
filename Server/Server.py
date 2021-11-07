from flask import Flask, jsonify, request, Blueprint
import os
import json
# from Blueprints.post_route import PostRoute

app = Flask(__name__)
# app.register_blueprint(PostRoute)

@app.route('/upload-model', methods=['POST'])
def upload_model():
    print("[POST] /upload-model")

    json_data = request.get_json()
    location = json_data["save_location"]
    mesh = json_data["mesh"]

    try:
        with open(location, "w") as f:
            f.write(json.dumps(mesh))
        return jsonify({"saved": True})
    except Exception as e:
        return jsonify({"saved": False, "reason": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)