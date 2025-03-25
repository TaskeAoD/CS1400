
class TrafficLight:

    #Constructor
    def __init__(self, colorIndex):
      self.colorIndex = colorIndex
      self.COLORS = ["Green", "Yellow", "Red"]

    #Class function: Changes the light from Green -> Yellow -> Red
    def changeLight(self):
      self.colorIndex += 1
      if self.colorIndex == 3:
        self.colorIndex = 0

    def __str__(self):
        return self.COLORS[self.colorIndex]

trafficLight1 = TrafficLight(0)
trafficLight2 = TrafficLight(2)

print("Traffic Light 1:", trafficLight1)
print("Traffic Light 2:", trafficLight2)
choice = ""
while choice != "q":
  choice = input("Press Enter to change the traffic lights (q to quit").lower()
  trafficLight1.changeLight()
  trafficLight2.changeLight()
  print("Traffic Light 1:", trafficLight1)
  print("Traffic Light 2:", trafficLight2)
