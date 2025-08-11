import asyncio

from app.graph.edge.sttSummaryEdge import buildSttSummaryGraph


async def runGraph(audioPath: str, title: str):
    graph = buildSttSummaryGraph()
    return await graph.ainvoke({"audioFilePath": audioPath, "title": title})
