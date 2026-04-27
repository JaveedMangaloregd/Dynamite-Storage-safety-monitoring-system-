from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from security import verify_token
from dynamodb import table
from predict import predict_status
from auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)

security = HTTPBearer()

@app.get("/sensor_status")
def get_sensor_data(token=Depends(security)):
    verify_token(token.credentials)

    response = table.scan()
    items = response["Items"]

    results = []

    for item in items:
        status = predict_status(item)

        results.append({
            "temperature": item["temperature"],
            "gas": item["gas"],
            "smoke": item["smoke"],
            "flame": item["flame"],
            "status": status
        })

    return results