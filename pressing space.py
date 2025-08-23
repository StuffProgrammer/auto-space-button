from pynput.keyboard import Key, Controller
import time
import pygame
# import ImageGrab
import pyautogui
keyboard = Controller()
pygame.init()

from PIL import Image
def is_color_near_center(target_color, tolerance=10):
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Calculate the center coordinates
    center_x, center_y = screen_width // 2, screen_height // 2

    # Capture a small region around the center (e.g., 10x10 pixels)
    region_size = 10
    left = center_x - region_size // 2
    top = center_y - region_size // 2
    region = pyautogui.screenshot(region=(left, top, region_size, region_size))

    # Convert the screenshot to a PIL image for pixel analysis
    image = Image.frombytes('RGB', region.size, region.tobytes())

    # Check each pixel in the region
    for x in range(region_size):
        for y in range(region_size):
            pixel_color = image.getpixel((x, y))
            if all(abs(pixel_color[i] - target_color[i]) <= tolerance for i in range(3)):
                return True  # Color found near the center

    return False

def is_color_in_area(color, region):
    try:
        # Take a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=region)

        # Convert the screenshot to a PIL Image for pixel access
        image = screenshot.convert("RGB")

        # Get the pixel data
        pixels = image.load()

        # Iterate through the pixels in the region
        for x in range(image.width):
            for y in range(image.height):  
                if pixels[x, y] == color:
                    return True  # Color found

        return False  # Color not found
    except Exception as e:
        print(f"Error: {e}")
        return False

def getColorUnderMouse():
    x, y= pyautogui.position()
    pixel = pyautogui.screenshot(
        region=(
            x, y, 1, 1
        )
    )
    return pixel.getcolors()  
def getColour(x, y):
    pixel = pyautogui.screenshot(
        region=(
            x, y, 1, 1
        )
    )
    return pixel.getcolors() 
#1920 / 2 and 1080 / 2
#while not getColour(1111, 930) == [(1, (0, 0, 0))]:
    time.sleep(0)
running = True
while running == True:
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_q] or getColour(1071, 390) == [(1, (254, 239, 201))]:
        #running = False
    if is_color_in_area((255, 218, 98), (int(960 - 100), int(560 - 100), 200, 200)):
    #if is_color_near_center((255, 218, 98), 1):
        keyboard.press(Key.space)  
        keyboard.release(Key.space)
        time.sleep(0.1)

    #print(str(getColorUnderMouse()) + "at" + str(pyautogui.position()))
print("program ended")
pygame.quit()

         