import json
import asyncio
import websockets
import requests

from pydantic import BaseModel

_platform_url = '127.0.0.1:8000'


class LoggedInResponseDataModel(BaseModel):
    token: str
    userId: int


def _login(url: str):
    data = {"username": "root@test.com", "password": "admin"}
    r = requests.post(url, data=data)
    return LoggedInResponseDataModel(**json.loads(r.text))


async def connect_ws(messages_to_send):
    ws_url = f"ws://{_platform_url}/websocket/"
    model = _login(url=f'http://{_platform_url}/api/getusertoken/')
    headers = {"Authorization": f"Bearer {model.token}"}

    async with websockets.connect(
            ws_url,
            extra_headers=headers,
            origin="**FULLY_PLATFORM_URL_ADDRESS**"
    ) as websocket:
        for message_to_send in messages_to_send:
            await websocket.send(json.dumps(message_to_send))
            response = await websocket.recv()
            print(response)

        await asyncio.sleep(10)

messages_to_send = [
    {
        "type": "sayHello",
        "message": {"firstName": "Hasan", "lastName": "Sajedi"}
    },
    ...
]

asyncio.get_event_loop().run_until_complete(connect_ws(messages_to_send))
