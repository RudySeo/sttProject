from langgraph.graph import StateGraph
from typing import TypedDict
from app.graph.node.sttNode import sttNode
from app.graph.node.summarizerNode import summarizerNode


class GraphState(TypedDict):
    audioFilePath: str  # 오디오 파일경로
    transcript: str  # STT 텍스트 결과
    summary: str  # 요약된 텍스트 결과


def buildSttSummaryGraph():
    graph = StateGraph(GraphState)

    # 노드 등록
    graph.add_node("stt", sttNode)
    graph.add_node("summarizer", summarizerNode)

    # 노드 연결 흐름 구성
    graph.set_entry_point("stt")
    graph.add_edge("stt", "summarizer")
    graph.set_finish_point("summarizer")
    return graph.compile()
