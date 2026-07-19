#Parent Class
class SmartDevice:
    def __init__(self,name,device_id,power_status):
        self.name = name
        self.__device_id = device_id
        self.__power_status = power_status

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self,new_id):
        if new_id != "":
            self.__device_id = new_id
        else :
            print("Device ID cannot be empty!")

    @property
    def power_status(self):
        return self.__power_status

    def  turn_on(self):
        self.__power_status = "ON"
        print(f"{self.name} is ON")
    def turn_off(self):
        self.__power_status = "OFF"
        print(f"{self.name} is OFF")

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Device ID : {self.__device_id}")
        print(f"Power : {self.__power_status}")

#First Child Class
class TemperatureSensor(SmartDevice):
    def __init__(self,name,device_id,power_status,temperature):
        super().__init__(name,device_id,power_status)
        self.temperature = temperature

    def read_temperature(self):
        print("Temperature: " + str(self.temperature) + "Celsius")

#Second Child Class
class SmartLight(SmartDevice):
    def __init__(self,name,device_id,power_status,brightness):
        super().__init__(name,device_id,power_status)
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self,value):
        if 0 <= value <= 100:
            self.__brightness = value
            print("Brightness set to " + str(value))
        else:
            print("Brightness cannot be between 0 and 100!")

    def increase_brightness(self):
        if self.__brightness > 100:
            self.brightness += 1
            print("Brightness:  " + str(self_brightness))
        else:
            print("Already at Maximum!")

    def decrease_brightness(self):
        if self.__brightness < 0:
            self.brightness -= 1
            print("Brightness: " + str(self.__brightness))
        else:
            print("Already at Minimum!")

#Third Child Class
class SecurityCamera(SmartDevice):
   def __init__(self,name,device_id,power_status,recording_status):
       super().__init__(name,device_id,power_status)
       self.recording_status = recording_status

   def start_recording(self):
       self.recording_status = "Recording"
       print(f"{self.name} is now recording!")

   def stop_recording(self):
       self.recording_status = "Idle"
       print(f"{self.name} has stopped recording!")


#Creating Objects
sensor = TemperatureSensor("Temp Sensor", "TS001", "OFF", 36.5)
light = SmartLight("Living Room Light", "SL002", "OFF", 50)
camera = SecurityCamera("Front Door Cam", "SC003", "OFF", "Idle")


#Menu
while True:
    print("\nSmart Device Menu")
    print("1. Display Device Info")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start or Stop Recording")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\n-- Sensor --")
        sensor.display_info()
        print("\n-- Light --")
        light.display_info()
        print("\n-- Camera --")
        camera.display_info()

    elif choice == "2":
        device = input("Which device? (sensor/light/camera): ")
        if device == "sensor":
            sensor.turn_on()
        elif device == "light":
            light.turn_on()
        elif device == "camera":
            camera.turn_on()

    elif choice == "3":
        device = input("Which device? (sensor/light/camera): ")
        if device == "sensor":
            sensor.turn_off()
        elif device == "light":
            light.turn_off()
        elif device == "camera":
            camera.turn_off()

    elif choice == "4":
        sensor.read_temperature()

    elif choice == "5":
        print("1. Increase  2. Decrease  3. Set value")
        b = input("Enter choice: ")
        if b == "1":
            light.increase_brightness()
        elif b == "2":
            light.decrease_brightness()
        elif b == "3":
            val = int(input("Enter value (0-100): "))
            light.brightness = val

    elif choice == "6":
        print("1. Start  2. Stop")
        r = input("Enter choice: ")
        if r == "1":
            camera.start_recording()
        elif r == "2":
            camera.stop_recording()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")