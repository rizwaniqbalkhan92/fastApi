from fastapi import HTTPException
from fastapi import Path
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Patients Portal."}
 

def get_patients():
    with open('patientDummyData.json','r') as f:
        data = json.load(f)
        return data
    


@app.get("/view_patients")
def view_patients():
    return get_patients()

@app.get("/view_patients/{id}")
def view_specific_patient(id: int = Path(..., ge=1,description = "Enter a valid Patient ID",title = "Patient ID")):
    try:
        patients = get_patients()
        for patient in patients:
            if patient['patient_id'] == id:
                return patient
    except FileNotFoundError:
        return {"message": "File not found"}
    except Exception as e:
        return {"message": str(e)}
    raise HTTPException(status_code=404, detail="Patient not found")

