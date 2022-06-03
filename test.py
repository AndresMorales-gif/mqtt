"""import asyncio
import websockets

async def handler(websocket, path):
    print(path)
    name = await websocket.recv()
    print(name)
    await websocket.send('Hola')


async def main():
    async with websockets.serve(handler, "localhost", 8001, subprotocols=['mqtt']):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())"""

import asyncio
from codecs import StreamReader, StreamWriter


async def handler(reader: StreamReader, writer: StreamWriter):
    print('espera')
    while True:
        print('1')
        message_read = await reader.read(1024)
        if not message_read:
            print('exit')
            break
        print(message_read)
        writer.write(str.encode("hola"))
        print('3')
        await writer.drain()
    writer.close()


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    serve = asyncio.start_server(handler, 'localhost', 8001)
    server = loop.run_until_complete(serve)
    try:
        loop.run_forever()  # <6>
    except KeyboardInterrupt:  # CTRL+C pressed
        pass

    print('Server shutting down.')
    server.close()  # <7>
    loop.run_until_complete(server.wait_closed())  # <8>
    loop.close()  # <9>


if __name__ == "__main__":
    main()
