# HumanChain AI Safety Incident Log API

A simple Flask-based RESTful API to log and manage AI safety-related incidents. This project is part of an internship task submission for HumanChain.

---

## 📁 Project Structure

```
├── app.py               # Main Flask application
├── seed.py              # Script to populate MongoDB with sample incidents
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (MONGO_URI)
└── README.md            # Project documentation
```

---

## 🔧 Features

- Add a new AI safety incident
- Retrieve all logged incidents
- Get a single incident by its ID
- Delete an incident
- Seed the database with sample incidents

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/raolalit9759/human-chain-ai-safety-api.git
cd human-chain-ai-safety-api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file with:

```
MONGO_URI=mongodb://localhost:27017/human_chain_db
```

Ensure MongoDB is running on your local machine.

### 5. Run the Application

```bash
python app.py
```

### 6. Seed Sample Data (Optional)

Run this once to insert testing data:

```bash
python seed.py
```

Post Artifact
![image](https://github.com/raolalit9759/human-chain-ai-safety-api/blob/59dfd9cd5d5b9f33c97895b19be0baf28bb9c086/seed.app_post_artifact.png?raw=true)

---

## 📫 API Endpoints

### `GET /incidents`

Returns a list of all incidents.

### `POST /incidents`

Create a new incident.

```json
{
  "title": "Example Incident",
  "description": "Details of the issue...",
  "severity": "High"  // Allowed: Low, Medium, High
}
```

### `GET /incidents/<id>`

Fetch a specific incident by ID.

### `DELETE /incidents/<id>`

Delete a specific incident by ID.

---

## 🧪 Sample Curl Commands

**Create Incident:**

```bash
curl -X POST http://localhost:5000/incidents \
-H "Content-Type: application/json" \
-d '{"title":"AI Model Failure","description":"Unexpected output from AI","severity":"High"}'
```
Post Artifact
![image](https://github.com/user-attachments/assets/c0b4d83e-5585-401e-8de8-685264f4f569)
![image](https://github.com/user-attachments/assets/8d75f41f-741b-4828-91ae-264f274a082e)


**Get All Incidents:**

```bash
curl http://localhost:5000/incidents
```
![image](https://github.com/user-attachments/assets/21dbaef7-e259-46a3-b696-a1fbdd4d92f7)

---

## 🧠 Technologies Used

- Language: Python 3
- Framework: Flask
- Database: MongoDB
- ODM: Flask-PyMongo

---

## 🙋‍♂️ Author

**Lalit Rao**\
[GitHub Profile](https://github.com/raolalit9759)

---

## ✅ Status

Final version — ready for submission to HumanChain.


