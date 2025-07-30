from app.service.sttService import transcribeAudio


async def sttNode(state: dict):
    transcript = transcribeAudio(state["audioFilePath"])
    return {"transcript": transcript}
