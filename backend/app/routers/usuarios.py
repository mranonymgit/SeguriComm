
from fastapi import APIRouter, HTTPException
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(
	prefix="/usuarios",
	tags=["Usuarios"]
)

@router.post("/", response_model = UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate):
    return {
        "id": 1,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rol": usuario.rol,
        "creado_en": "2026-04-18"

    }

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int):
    if usuario_id != 1:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {
        "id": usuario_id,
        "nombre": "Juan Pérez",
        "email": "juan@example.com",
        "rol": "residente",
        "creado_en": "2026-04-18"
    }