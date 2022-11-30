# Connect to raspberry pi high quality camera, get a snapshot, and show it
# on the screen.

import io
import picamera
import pygame
import pygame.camera
import time

pygame.init()
pygame.camera.init()

# Set up the camera
camera = picamera.PiCamera()

# Set camera properties
camera.resolution = (640, 480)
camera.framerate = 15
camera.shutter_speed = 1000000
camera.exposure_mode = 'off'
camera.awb_mode = 'auto'

# Get a stream to write the image to
stream = io.BytesIO()

# Create a pygame window at 30%
screen = pygame.display.set_mode((640, 480))

# Create a pygame surface to display the image
surface = pygame.Surface((640, 480))

# Start the camera preview
camera.start_preview()

# Wait for the user to press a key
input("Press Enter to capture image...")

# Capture the image
camera.capture(stream, format='jpeg')

# Rewind the stream to the beginning so we can read its content
stream.seek(0)

# Load the image from the stream
image = pygame.image.load(stream)

# Blit the image to the surface
surface.blit(image, (0, 0))

# Draw the surface to the screen
screen.blit(surface, (0, 0))

# Update the display
pygame.display.update()

# Wait for the user to press a key
input("Press Enter to quit...")