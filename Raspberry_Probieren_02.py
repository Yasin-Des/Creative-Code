import machine
import time

# Configure ultrasonic sensor pins
TRIG = machine.Pin(2, machine.Pin.OUT)  # Ultrasonic sensor TRIG pin connected to GPIO2
ECHO = machine.Pin(3, machine.Pin.IN)   # Ultrasonic sensor ECHO pin connected to GPIO3

# Initialize the TRIG pin to a low level
TRIG.low()
time.sleep(2)  # Wait for the sensor to stabilize

# Function to measure distance
def measure_distance():
    # Send trigger signal
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    # Wait for the echo signal to return
    while ECHO.value() == 0:
        pass
    start_time = time.ticks_us()  # Echo start time

    while ECHO.value() == 1:
        pass
    end_time = time.ticks_us()  # Echo end time

    # Calculate distance (unit: cm)
    duration = time.ticks_diff(end_time, start_time)
    distance = (duration * 0.0343) / 2  # Speed of sound = 343 m/s
    return distance

# Main loop: send data via the USB serial port
while True:
    distance = measure_distance()  # Get distance measurement
    print(f"Distance: {distance:.2f} cm")  # print() automatically adds a newline
    time.sleep(1)  # Wait one second between measurements
