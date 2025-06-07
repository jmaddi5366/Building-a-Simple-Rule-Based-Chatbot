from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapterSettings, TurnContext, BotFrameworkAdapter
)
from botbuilder.schema import Activity
import json

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    text = body["text"] if "text" in body else ""
    # Simple rules:
    if text.lower() in ("help", "?"):
        reply = "I can echo your text or tell you my capabilities: echo, help."
    elif text.startswith("echo "):
        reply = text[5:]
    else:
        reply = f"Echo: {text[::-1]}"  # reversed string example
    return web.json_response({"type": "message", "text": reply})

if __name__ == "__main__":
    app = web.Application()
    app.router.add_post("/api/messages", messages)
    web.run_app(app, host="localhost", port=3978)
