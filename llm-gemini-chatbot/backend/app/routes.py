from fastapi import FastAPI, Query
from app.gemini_tasks import generate_essay, generate_poem

def setup_routes(app: FastAPI):
    # Gemini endpoints
    @app.get("/essay-direct")
    def essay_direct(topic: str = Query(..., description="Topic to generate essay about")):
        return {"result": generate_essay(topic)}

    @app.get("/poem-direct")
    def poem_direct(topic: str = Query(..., description="Topic to generate poem about")):
        return {"result": generate_poem(topic)}

 
