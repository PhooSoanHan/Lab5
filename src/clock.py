import time
import threading
from hal import hal_lcd as LCD

# Initialize LCD
lcd = LCD.lcd()

def time_display():
    while True:
        # Get current time
        local_time = time.localtime()
        time_str = time.strftime("%H:%M:%S", local_time)
        date_str = time.strftime("%d:%m:%Y", local_time)

        # Display the time and date on the LCD
        lcd.lcd_clear()
        lcd.lcd_display_string(time_str, 1)
        lcd.lcd_display_string(date_str, 2)
        
        # Flash the colon in the time display
        time.sleep(0.5)
        lcd.lcd_display_string(time_str.replace(":", " "), 1)
        time.sleep(0.5)

def main():
    clock_thread = threading.Thread(target=time_display)
    clock_thread.daemon = True
    clock_thread.start()
    
    while True:
        time.sleep(1)

# Main entry point
if __name__ == "__main__":
    main()