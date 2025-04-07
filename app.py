from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


SEVERITY_LEVELS = {"Low", "Medium", "High"}


@app.route("/incidents", methods=["GET"])
def get_incidents():
    incidents = mongo.db.incidents.find()
    result = []
    for incident in incidents:
        result.append({
            "id": str(incident["_id"]),
            "title": incident["title"],
            "description": incident["description"],
            "severity": incident["severity"],
            "reported_at": incident["reported_at"]
        })
    return jsonify(result), 200


@app.route("/incidents", methods=["POST"])
def create_incident():
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "description", "severity")):
        return jsonify({"error": "Missing required fields"}), 400
    if data["severity"] not in SEVERITY_LEVELS:
        return jsonify({"error": "Invalid severity value"}), 400

    new_incident = {
        "title": data["title"],
        "description": data["description"],
        "severity": data["severity"],
        "reported_at": datetime.utcnow().isoformat()
    }
    result = mongo.db.incidents.insert_one(new_incident)
    new_incident["id"] = str(result.inserted_id)
    return jsonify(new_incident), 201


@app.route("/incidents/<id>", methods=["GET"])
def get_incident(id):
    incident = mongo.db.incidents.find_one({"_id": ObjectId(id)})
    if not incident:
        return jsonify({"error": "Incident not found"}), 404
    return jsonify({
        "id": str(incident["_id"]),
        "title": incident["title"],
        "description": incident["description"],
        "severity": incident["severity"],
        "reported_at": incident["reported_at"]
    }), 200


@app.route("/incidents/<id>", methods=["DELETE"])
def delete_incident(id):
    result = mongo.db.incidents.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Incident not found"}), 404
    return jsonify({"message": "Incident deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
