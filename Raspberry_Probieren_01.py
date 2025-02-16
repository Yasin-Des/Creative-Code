from machine import UART, Pin
import time
# Initialize UART (using Pico's GPIO TX and RX pins)
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5)) # Change Pin(4) and Pin(5) to match your actual connections
# Function to send a command to the DFPlayer Mini
def send_command(cmd, param1=0, param2=0):
high_byte = param1 >> 8
low_byte = param1 & 0xFF
checksum = 0xFFFF - (0xFFFF & (0x7E + 0xFF + 6 + cmd + high_byte + low_byte)) + 1
checksum_high = checksum >> 8
checksum_low = checksum & 0xFF
command = bytearray([
0x7E, 0xFF, 0x06, cmd, 0x00, high_byte, low_byte, checksum_high, checksum_low, 0xEF
])
uart1.write(command)
# Initialize DFPlayer Mini
def initialize_player():
# Set volume to 30 (range: 0-30)
send_command(0x06, 0, 30)
time.sleep(1)
# Main function for looping music playback
def loop_play():
# Set loop playback mode for all files
send_command(0x11, 0, 1) # Playback mode: 1 means loop playback for all files
print("Starting looped music playback...")
# Main program
initialize_player()
loop_play()
# Run continuously (keep the program running to maintain playback state)
while True:
# DFPlayer supports loop playback by itself, so there's no need to resend commands
time.sleep(1) # Delay to reduce CPU usage of the main program
