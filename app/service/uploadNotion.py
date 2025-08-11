from fastapi import HTTPException  # fastapi에서 import 권장
import httpx
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


async def uploadNotion(state: dict):

    keywords = list(state.get("keywords", []))
    summary = state.get("summary", "")
    transcript = state.get("transcript", "")
    title = state.get("title", "")
    date_str = datetime.today().strftime("%Y-%m-%d")

    children = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "📝 회의록"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": f"📅 날짜: {date_str}"}},
                ]
            },
        },
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📌 회의 내용"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",  # bulleted_list_item이 아닌 paragraph가 적합할 수 있음
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": transcript}}],
            },
        },
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🧠 요약"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": summary}}]
            },
        },
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🔑 키워드"}}]
            },
        },
    ] + [
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": f"`{item}`"}}]
            },
        }
        for item in keywords
    ]

    payload = {
        "parent": {"type": "page_id", "page_id": PARENT_PAGE_ID},
        "properties": {
            "title": {"title": [{"type": "text", "text": {"content": title}}]}
        },
        "children": children,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.notion.com/v1/pages", headers=headers, json=payload
        )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {
        "message": "회의록이 성공적으로 생성되었습니다.",
        "notion_response": response.json(),
    }
