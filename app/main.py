# app/main.py
from fastapi import FastAPI, Form, HTTPException
from .agent import JobGenieAgent
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = JobGenieAgent()

@app.post("/generate")
async def generate(job_description: str = Form(...), cv_text: str = Form(...)):
    try:
        cover_letter = agent.generate_cover_letter(job_description, cv_text)
        
        return JSONResponse(content={"cover_letter": cover_letter})

    except Exception as e:
        print(f"❌ Error generating cover letter: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": "Failed to generate cover letter. Please try again later."}
        )
    
@app.get("/health")
async def health_check():
    return {"status": "ok"}