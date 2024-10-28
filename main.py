from fastapi import FastAPI, status, Query
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from database import DatabaseConnection, create_user_table, create_seller_table
from usercontroller import router as user_router
from sellercontroller import router as seller_router







@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event: setup the database connection and tables
    print("Starting up...")
    db_instance = DatabaseConnection()  # Create a new instance if none exists
    create_user_table(db_instance)
    create_seller_table(db_instance)

    yield

    print("Shutting down...")
    conn = db_instance.get_connection()  # Use the existing instance to get the connection
    if conn:
        conn.close()

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(seller_router)




@app.get("/")
def read_root():
    
    conn = DatabaseConnection.get_connection()
    if conn is not None:
        conn_status = "Connected with DB"
    else:
        conn_status = "Not connected with DB"
    return JSONResponse(
        status_code= status.HTTP_200_OK,
        content = {"message": "hello world", "db_status": conn_status}
    )


@app.get("/new-api")
def new_api(A : str = Query(None), B:str = Query(None), C:str = Query(None)):
    response_content = {}
    if A is not None:
        response_content["A"] = f"Value of A is: {A}"
    if B is not None:
        response_content["B"] = f"Value of B is: {B}"
    if C is not None:
        response_content["C"] = f"Value of C is: {C}"

    if not response_content:
        response_content["message"] = "No query parameters provided"

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response_content
    )


