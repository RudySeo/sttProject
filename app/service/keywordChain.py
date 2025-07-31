from typing import TypedDict
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI


# OpenAI 모델
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 정의
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "너는텍스트에서 핵심 키워드를 뽑아주는 도우미입니다. 키워드는 명사 위주로 간결하게 나열해 주세요.",
        ),
        ("human", "{summary}"),
    ]
)

# RunnableSequence로 체인 구성
keywordChain = prompt | llm


# 실행 함수
async def runKeywordChain(text: str) -> str:
    return keywordChain.invoke({"summary": text}).content
