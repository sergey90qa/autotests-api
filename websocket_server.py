import asyncio

import websockets

from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received message: {message}")
        response = f"Echo: {message}"
        for _ in range(5):
            await websocket.send(response)

async def main():
    sever = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await sever.wait_closed()

asyncio.run(main())