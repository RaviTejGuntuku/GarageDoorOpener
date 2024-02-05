import cv2
from numpy import *
import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth


def fileToDetect(imgFile):
    img = cv2.imread(imgFile)
    height, width, _ = img.shape
    mask = zeros((height+2, width+2), uint8)

    start_pixel = (360, 200)
    diff = (5, 5, 5)

    retval, _, _, _ = cv2.floodFill(
        img, mask, start_pixel, (0, 255, 0), diff, diff)

    cv2.imwrite(imgFile.replace(".jpg", "") + "_result.jpg", img)

    return retval > 50000


async def takePicture(image_name):

    blink = ""

    async with ClientSession() as session:

        blink = Blink(session=session)

        # Can set no_prompt when initializing auth handler
        auth = Auth({"username": "ravikumar.guntuku@gmail.com",
                    "password": "Fadd3n$6120"}, no_prompt=True)
        blink.auth = auth
        await blink.start()

        # print(blink.cameras)

        camera = blink.cameras['G8V1-9001-3113-34AR']
        await camera.snap_picture()       # Take a new picture with the camera

        await blink.refresh()             # Get new information from server
        await camera.image_to_file(image_name)

        # thumbnail_response = await camera.get_thumbnail()
        # print(thumbnail_response)

    return blink


def isGarageOpen():
    img_path = "garage_current_image.jpg"
    asyncio.run(takePicture(img_path))

    return fileToDetect(img_path)


print(isGarageOpen())
