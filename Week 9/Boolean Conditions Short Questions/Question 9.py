light = float(input())
temperature = float(input())

def turn_camera_on():
    print("On")

if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        turn_camera_on()

if (light < 0.01) != (temperature > 0.0):
    turn_camera_on()