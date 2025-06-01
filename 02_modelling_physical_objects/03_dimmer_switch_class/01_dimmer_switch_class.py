
class dimmerSwitch:
    def __init__(self):
        self.switchState = False
        self.brightnessLevel = 0

    def turnOn(self):
        self.switchState = True
        
    def turnOff(self):
        self.switchState = False
    
    def raiseLevel(self):
        if self.brightnessLevel <10:
            self.brightnessLevel +=1

    def lowerLevel(self):
        if self.brightnessLevel >0:
            self.brightnessLevel -=1

    def show(self):
        print("Switch State:", self.switchState)
        print("Brightness Level:", self.brightnessLevel)
        pass


oDimmer = dimmerSwitch()

oDimmer.turnOn()
for i in range(0, 3):
    oDimmer.raiseLevel()

print(oDimmer.show())