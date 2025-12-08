# ai_server_core.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------
# GPT에게 상품 설명 생성 요청
# -----------------------------
def generate_product_description(product: dict) -> str:

    prompt = f"""
너는 남녀 공용 캐주얼 의류 쇼핑몰의 상품 상세 페이지를 작성하는 카피라이터야.
아래 정보를 참고해서 한국어로 300~500자 정도의 상세 설명을 써줘.

[상품 정보]
- 상품명: {product.get("name")}
- 가격: {product.get("price")}원
- 옵션: {product.get("options")}
- 카테고리: {product.get("category_path")}

이미지를 참고해서 실루엣·핏·색감·디테일·무드를 자연스럽게 설명해줘.
"""

    image_contents = [
        {
            "type": "image_url",
            "image_url": {"url": url}
        }
        for url in product.get("image_urls", [])
        if url
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    *image_contents,
                ],
            }
        ],
    )

    return response.choices[0].message.content.strip()


# -----------------------------
# 설명 + 이미지 블록 조합 생성
# -----------------------------
def generate_blocks(description_text: str, image_urls: list):
    blocks = []

    # 설명 먼저 넣고
    blocks.append({
        "type": "text",
        "content": description_text
    })

    # 뒤에 이미지 1장씩 넣기
    for url in image_urls:
        if url:
            blocks.append({
                "type": "image",
                "url": url
            })

    return blocks
