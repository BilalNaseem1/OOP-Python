# Another word that you'll come across in OOP is instance. The words
# instance and object are essentially interchangeable; however, to be precise, we
# would say that a LightSwitch object is an instance of the LightSwitch class.


class lightSwitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False


switch = lightSwitch()

def status(sx):
    if sx == False:
        return "not Turned on"
    else:
        return "Turned on"

status = status(switch.switchIsOn)
print(f"The switch is {status}")

switch.turnOn()

print(f"The switch is {switch.switchIsOn}")
