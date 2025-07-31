from app.service.gptSummaryChain import runSummaryChain


async def summarizerNode(state: dict):
    summary = await runSummaryChain(state["transcript"])
    return {"summary": summary}
