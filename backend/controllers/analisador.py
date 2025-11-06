from fastapi import APIRouter, UploadFile, Form, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/analisar")
async def analisar_prototipagem(
    imagem: UploadFile = File(...),
    tipo_aplicacao: str = Form(...),
    resumo: str = Form(...)
):
    print(imagem, tipo_aplicacao, resumo)
    return JSONResponse(content={"message": "OK"})
