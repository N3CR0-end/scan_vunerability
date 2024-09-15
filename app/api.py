from flask import Blueprint, request, jsonify
import uuid
from .scanner import start_scan, get_scan_status, get_scan_results

api_bp = Blueprint('api', __name__)

@api_bp.route('/scan', methods=['POST'])
def scan():
    data = request.json
    scan_id = str(uuid.uuid4())
    target = data.get('target')
    
    start_scan(scan_id, target)
    return jsonify({"scan_id": scan_id}), 202

@api_bp.route('/scan/<scan_id>', methods=['GET'])
def status(scan_id):
    status = get_scan_status(scan_id)
    return jsonify({"status": status})

@api_bp.route('/scan/<scan_id>/results', methods=['GET'])
def results(scan_id):
    results = get_scan_results(scan_id)
    return jsonify({"results": results})
