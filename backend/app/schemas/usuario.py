
from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
	nombre: str
	email: EmailStr
	rol: str = "residente"

class UsuarioCreate(UsuarioBase):
	password: str

class UsuarioResponse(UsuarioBase):
	id: int
	creado_en: Optional[str]  = None

	class Config:
		from_attributes = True
