from app.service.gptSummaryChain import runSummaryChain


async def summarizerNode(state: dict):
    summary = runSummaryChain(state["transcript"])
    return {"summary": summary}
