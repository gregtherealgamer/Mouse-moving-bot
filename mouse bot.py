import pyautogui
import time

# set the speed and duration of the movement
speed = 0.1
duration = 10

# calculate the distance to travel
distance = speed * duration

# move the mouse in a circular pattern
for i in range(10):
    pyautogui.moveRel(distance, 0, duration=duration)
    pyautogui.moveRel(0, distance, duration=duration)
    pyautogui.moveRel(-distance, 0, duration=duration)
    pyautogui.moveRel(0, -distance, duration=duration)
    pyautogui.click()
