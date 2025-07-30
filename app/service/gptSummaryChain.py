from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI

# OpenAI 모델
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 프롬프트 정의
prompt = ChatPromptTemplate.from_messages(
    [("system", "너는 텍스트를 간결하게 요약하는 비서야."), ("human", "{text}")]
)

# RunnableSequence로 체인 구성
summaryChain = prompt | llm


# 실행 함수
def runSummaryChain(text: str) -> str:
    return summaryChain.invoke({"text": text}).content
