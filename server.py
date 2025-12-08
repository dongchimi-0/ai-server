# server.py
from fastapi import FastAPI
from schemas import ProductIn, DescriptionOut
from ai_server_core import generate_product_description, generate_blocks

app = FastAPI()


@app.post("/ai/description", response_model=DescriptionOut)
async def ai_description(body: ProductIn):

    # 1) GPT로 설명 생성
    text = generate_product_description(body.model_dump())

    # 2) 설명 + 이미지 → blocks 조합
    blocks = generate_blocks(text, body.image_urls)

    # 3) description + blocks 같이 반환
    return DescriptionOut(
        description=text,
        blocks=blocks
    )
