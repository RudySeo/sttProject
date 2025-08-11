from app.service.uploadNotion import uploadNotion


async def notionNode(state: dict):
    return await uploadNotion(state)
