class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channels = list(range(0,16))
        self.currentChannel = 0
        self.currentVolume = 10
        self.rangeVolume = list(range(0,21))

    
    def toggle(self):
        self.isOn = not self.isOn

    def volumeUp(self):
        if self.isOn == True:
            if self.isMuted == True:
                self.isMuted == False
            if self.currentVolume < max(self.rangeVolume):
                self.currentVolume +=1
        else:
            pass

    def volumeDown(self):
        if self.isOn == True:
            if self.isMuted == True:
                self.isMuted == False
            if self.currentVolume > min(self.rangeVolume):
                self.currentVolume -=1
        else:
            return None
    
    def channelUp(self):
        if self.isOn == True:
            self.currentChannel +=1
            if self.currentChannel > max(self.channels):
                self.currentChannel = 0
        else:
            return None
        
    def channelDown(self):
        if self.isOn == True:
            self.currentChannel -=1
            if self.currentChannel < min(self.channels):
                self.currentChannel = max(self.channels)
        else:
            return None
        
    def mute(self):
        self.isMuted = not self.isMuted 

    def setChannel(self, newChannel):
        if newChannel in self.channels:
            self.currentChannel = newChannel
        else:
            return None
        
    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print(' TV is: On')
            print('        Channel is:', self.currentChannel)
            if self.isMuted:
                print('        Volume is:', self.currentVolume, '(sound is muted)')
            else:
               print('    Volume is:', self.currentVolume)
        else:
            print('        TV is: Off')


if __name__ == "__main__":
    tv = TV()

    print(tv.isOn)
    tv.toggle()
    print(tv.showInfo())

    print(tv.currentChannel)