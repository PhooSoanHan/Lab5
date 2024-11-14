import time
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

lcd = LCD.lcd()
buzzer.init()
keypad.init(lambda key: on_key_press(key))

correct_pin = "1234"
input_pin = ""
max_attempts = 3
attempts = 0
safe_locked = True

def display_initial_message():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: ", 2)

def on_key_press(key):
    global input_pin, attempts, safe_locked

    if not safe_locked:
        return
    
    if len(input_pin) < len(correct_pin) and key != '*':
        input_pin += str(key)
        lcd.lcd_display_string("Safe Lock", line=1)
        lcd.lcd_display_string("Enter PIN: " + '*' * len(input_pin), line=2)

    # Make sure the input PIN is the same length as the correct PIN
    if len(input_pin) == len(correct_pin):
        
        if input_pin == correct_pin:
            
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Unlocked", line=1)
            safe_locked = False

        else:
            attempts += 1

            lcd.lcd_clear()
            lcd.lcd_display_string("Wrong PIN", line=1)
            buzzer.turn_on_with_timer(1)
            time.sleep(1)

            if attempts >= max_attempts:
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Disabled", line=1)
                safe_locked = False
            else:
                input_pin = ""
                display_initial_message()


def main():
    global input_pin, attempts, safe_locked

    display_initial_message()

    while True:
        time.sleep(0.1)

# Main entry point
if __name__ == "__main__":
    main()