# requirement
# 1. A car  (name, speedLimit, start(), stop(), speedUP(), speedDown(), showSpeed())
# 2. user can start the car 
# 3. user can see Speed,
# 4. can change speed (speedUp 10+, speedDown 10-)
# 5. can stop the car


class Car:
    carBrand = ""
    speedLimit = 0
    currentSpeed = 0
    isStarted = False
  
    def dashboard(self):
        print(f"-->You are in {self.carBrand}<--")
        print(f"-->Speed limit = {self.speedLimit}km/h<---")
        print(f"-->Current speed = {self.currentSpeed}km/h<---")   
    
    def start(self):
        if self.isStarted:
            print(f"{self.carBrand} is already started.")
        else:
            self.isStarted = True
            print(f"{self.carBrand} is started!")
            
        self.dashboard()   
   
    # ADDED showSpeed()
    def showSpeed(self):
        print(f"-->Current speed = {self.currentSpeed}km/h<---")
        
    def speedUp(self):
        if self.isStarted:
            self.currentSpeed += 10
            
            if self.currentSpeed > self.speedLimit:
                self.currentSpeed -= 10
                print("You are at max speed.")
        else:
            print(f"Start {self.carBrand} car first!")
            
        self.dashboard()
        
    def speedDown(self):
        if self.isStarted:
            self.currentSpeed -= 10
            
            if self.currentSpeed < 0:
                self.currentSpeed += 10
                print("You are at min speed.")
        else:
            print(f"Start {self.carBrand} car first!")
            
        self.dashboard()

    def stop(self):
        if self.isStarted:
            self.currentSpeed = 0
            self.isStarted = False
            print(f"{self.carBrand} is Stopped!")
        else:
            print(f"{self.carBrand} is already Stopped!")
            
        self.dashboard()


# prepare a new car.
Toyota = Car()
Toyota.carBrand = "Toyota"
Toyota.speedLimit = 300

Hundayi = Car()
Hundayi.carBrand = "Hundayi"
Hundayi.speedLimit = 100


# *********

while True:
    print("---------------")
    print("1. Start ")
    print("2. Show Speed ")
    print("3. speedUp by +10")
    print("4. speedDown by -10")
    print("5. stop ")
    print("6. exit ")
    print("---------------")
    
    choice = int(input("Choose an option: "))
    print(f"\nYou have chosen {choice}\n")
    
    if choice == 1:
        Hundayi.start()
        
    elif choice == 2:
        Hundayi.showSpeed()
        
    elif choice == 3:
        Hundayi.speedUp()
        
    elif choice == 4:
        Hundayi.speedDown()
        
    elif choice == 5:
        Hundayi.stop()
        
    elif choice == 6:
        break