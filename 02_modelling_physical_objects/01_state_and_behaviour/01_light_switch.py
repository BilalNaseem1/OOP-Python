switchIsOn = False

def turnOn():
    global switchIsOn
    switchIsOn = True


def turnOff():
    global switchIsOn
    switchIsOn = False


print(switchIsOn)
turnOn()

# turning on
turnOn()
print(switchIsOn)

# turning off
turnOff()
print(switchIsOn)
