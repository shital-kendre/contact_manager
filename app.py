"""import flask from Flask, jsonify, request, render_template

app = Flask(__name__)

contacts = []

@app.route('/')
def home():
    return "Welcome Home"

@app.route('/create', methods = ['POST'])
def create_contact():

    data = request.form
    name = data.get('name')
    phone = data.get('phone')

    if not name or not phone:
        return jsonify({"Response" : "failed",
                        "Error" : "Invalid details"})




if __name__ == '__main__':
    app.run()"""


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # ✅ Fix 1: Import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend to call API

# In-memory storage
contacts = []
next_id = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def create_contact():
    """Add a new contact."""
    global next_id
    data = request.json or request.form  # ✅ Fix 2: Support both JSON & Form

    name = data.get("name")
    phone = data.get("phone")
    
    if not name or not phone:
        return jsonify({"response": "failed", "error": "Name and phone are required"}), 400

    contact = {
        "id": next_id,
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    next_id += 1
    return jsonify(contact)

@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404
    return jsonify(contact), 200

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """Update an existing contact."""
    data = request.json or request.form
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404

    contact["name"] = data.get("name", contact["name"])
    contact["phone"] = data.get("phone", contact["phone"])
    return jsonify(contact)

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """Delete a contact by ID."""
    global contacts
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404
    
    contacts.remove(contact)  # ✅ Fix 3: Properly remove contact
    return jsonify({"response": "successful", "message": "Contact deleted"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=False)




"""Problem Statement: Contact Manager API
Objective:
Design and implement a simple Contact Manager API using Flask. The API will allow users to create, view, update, and delete contacts. This service is aimed at managing a personal or small team contact list without the need for a database—data will be stored in memory.

Requirements:

Create Contact:

Provide an endpoint to add a new contact by supplying a name and a phone number.
Each contact should be assigned a unique identifier.
View Contacts:

Implement an endpoint to retrieve a list of all contacts in JSON format.
Implement another endpoint to retrieve the details of a specific contact using its unique identifier.
Update Contact:

Allow users to update the information (name or phone number) of an existing contact by its unique identifier.
Delete Contact:

Allow users to delete a contact by its unique identifier.
Error Handling:

The API should handle invalid inputs gracefully by returning clear error messages and appropriate HTTP status codes.
In‑Memory Storage:

Use a simple Python list or dictionary to store contact entries. Note that data will be lost when the server is restarted, which is acceptable for this prototype.
Constraints:

The API must be implemented using Flask in Python.
Data must be exchanged in JSON format.
No persistent storage is required; use in‑memory storage.
Use Cases:

A user wants to maintain a simple list of contacts (e.g., family, friends, or colleagues) and be able to add new contacts, update existing ones, or delete outdated information.
A developer needs a lightweight API to experiment with CRUD operations in Flask.
This API serves as a foundation for learning RESTful API design, which can later be expanded with a database for persistent storage.
"""
"""from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for contacts and an ID counter
contacts = []
next_id = 1

@app.route('/contacts', methods=['GET'])
def get_contacts():
    
    return jsonify(contacts), 200

@app.route('/contacts', methods=['POST'])
def create_contact():
    
    global next_id
    # Accept JSON data (or form data if needed)
    data = request.get_json() or request.form
    name = data.get("name")
    phone = data.get("phone")
    
    if not name or not phone:
        return jsonify({"response": "failed", "error": "Name and phone are required"}), 400

    contact = {
        "id": next_id,
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    next_id += 1
    return jsonify(contact), 201

@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404
    return jsonify(contact), 200

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    
    data = request.get_json() or request.form
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404

    # Update the contact with new values if provided
    contact["name"] = data.get("name", contact["name"])
    contact["phone"] = data.get("phone", contact["phone"])
    return jsonify(contact), 200

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
   
    global contacts
    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"response": "failed", "error": "Contact not found"}), 404
    
    contacts = [c for c in contacts if c["id"] != contact_id]
    return jsonify({"response": "successful", "message": "Contact deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)"""
