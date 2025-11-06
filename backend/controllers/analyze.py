import base64
import os
import tempfile
from pathlib import Path
from fastapi import APIRouter, UploadFile, Form, File
from fastapi.responses import JSONResponse
from backend.prompt_engineering import PromptEngineer
from backend.di import openAIClient, OPENAI_DEPLOYMENT_NAME


router = APIRouter()

@router.post("/analyze")
async def analyzes_prototyping(
    image: UploadFile = File(...),
    application_type: str = Form(...),
    description: str = Form(...)
):
    try:
        prompt = PromptEngineer.build_prompt_analyzes_prototyping(
            application_type=application_type,
            description=description
        )
        content = await image.read()

        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(image.filename).suffix) as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name

        with open(temp_file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')

        chat_prompt = [
            {
                "role": "system",
                "content": "Você é uma IA especialista em engenharia de software e designer de produtos de software, que analisa prototipos e diagramas de arquitetura de software, aplicativos e sistemas."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{encoded_string}"}
                    },
                    {
                        "type": "text", 
                        "text": "Por favor, analise a imagem e o texto acima e forneça uma analise detalhada destacando os pontos positivos e negativos e recomendações de melhoria."
                            "Afim de permitir que os designers possam criar um prototipo mais eficiente, menos ambiguo e mais alinhado com os pré-requisitos necessários para serem disponibilizados para o time de desenvolvimento."
                    }
                ]
            }
        ]

        response = openAIClient.chat.completions.create(
            model= OPENAI_DEPLOYMENT_NAME,
            messages = chat_prompt,
            max_completion_tokens=1500,
            stop=None,
            stream= False,
        )
        os.remove(temp_file_path)

        return JSONResponse(content=response.to_dict(), status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
