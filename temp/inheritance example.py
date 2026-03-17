# --- THE PARENT (The Entity) ---
class SmartDevice:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.is_on = False
        print(f"DEBUG: {self.name} initialized by Parent.")

    def toggle(self):
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"{self.name} is now {state}")

# --- CHILD A (The Character - User Controlled) ---
class SmartLight(SmartDevice):
    def __init__(self, name, brand, brightness):
        # super() sends name and brand to SmartDevice
        super().__init__(name, brand) 
        self.brightness = brightness # Unique to Light

    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} brightness set to {self.brightness}%")

# --- CHILD B (The Enemy - Auto/AI Controlled) ---
class SecurityCamera(SmartDevice):
    def __init__(self, name, brand, resolution):
        super().__init__(name, brand)
        self.resolution = resolution # Unique to Camera
        self.is_recording = False

    def auto_record(self):
        if self.is_on:
            self.is_recording = True
            print(f"{self.name} is now recording in {self.resolution}!")
        else:
            print(f"Cannot record: {self.name} is powered off.")

# --- THE "GAME" LOOP ---
light = SmartLight("Bedroom Light", "Philips", 80)
camera = SecurityCamera("Front Door", "Nest", "1080p")

print("--- Action ---")
light.toggle()          # Uses Parent method
light.set_brightness(50) # Uses Child method

camera.auto_record()    # Fails because it's off
camera.toggle()         # Uses Parent method
camera.auto_record()    # Works now!