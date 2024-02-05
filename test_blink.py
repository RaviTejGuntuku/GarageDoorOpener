import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
import os
from dotenv import load_dotenv


async def takePicture():

    load_dotenv()
    blink = ""

    async with ClientSession() as session:

        blink = Blink(session=session)

        # Can set no_prompt when initializing auth handler
        auth = Auth({"username": os.getenv("BLINK_USERNAME"),
                    "password": os.getenv("BLINK_PASSWORD")}, no_prompt=True)
        blink.auth = auth
        await blink.start()

        print(blink.cameras)

        camera = blink.cameras['G8V1-9001-3113-34AR']
        await camera.snap_picture()       # Take a new picture with the camera

        await blink.refresh()             # Get new information from server
        await camera.image_to_file('garage_current_image.jpg')

        thumbnail_response = await camera.get_thumbnail()
        print(thumbnail_response)

    return blink

blink = asyncio.run(takePicture())
