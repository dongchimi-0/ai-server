# schemas.py
from pydantic import BaseModel
from typing import List, Optional


# 블록 구조 (텍스트 or 이미지)
class Block(BaseModel):
    type: str                 # "text" 또는 "image"
    content: Optional[str] = None
    url: Optional[str] = None


# 요청받는 상품 정보 구조
class ProductIn(BaseModel):
    name: str
    price: Optional[int] = None
    options: Optional[str] = None
    category_path: Optional[str] = None
    image_urls: List[str]     # 여러 이미지 지원


# 응답 구조: 설명 + 블록 리스트
class DescriptionOut(BaseModel):
    description: str
    blocks: List[Block]
