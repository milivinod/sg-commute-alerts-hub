from fastapi import FastAPI

#creates an instance of a FastAPI application
app = FastAPI(title="SG Commute Alerts Hub")

#when someone sens a GET request to /api/health, then run the function below it and return its result
@app.get("/api/health")

def health():
    return {"status": "ok"} #FastAPI auto converts dictionaries in Python to JSON format
