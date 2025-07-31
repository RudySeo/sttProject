from typing import TypedDict
from app.service.keywordChain import runKeywordChain


async def keywordNode(state: dict):
    summary = state["summary"]
    keyword_str = await runKeywordChain({"summary": summary})
    # 쉼표 또는 줄바꿈으로 나뉜 키워드 처리
    keywords = [
        k.strip() for k in keyword_str.replace("\n", ",").split(",") if k.strip()
    ]

    # 상태 유지하며 키워드 추가
    return {**state, "keyword": keywords}
