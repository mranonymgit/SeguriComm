from fastapi import FastAPI
from app.routers.usuarios import router as usuarios_router

app = FastAPI(
    title="SeguriComm API",
    description="API RESTful para el sistema de seguridad comunitaria y atención de emergencias.",
    version="0.1.0"
)

# Incluimos los routers
app.include_router(usuarios_router)

@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a la API de SeguriComm",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}