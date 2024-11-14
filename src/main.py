from hal import hal_adc as adc  
from hal import hal_servo
from time import sleep

# Map ADC value to servo angle (0-180 degrees)
def adc_to_servo_angle(adc_value):
    angle = (adc_value * 180) / 1023
    return angle

def main():
    hal_servo.init()
    adc.init() 

    while True:
            adc_value = adc.get_adc_value(1)
            servo_angle = adc_to_servo_angle(adc_value)
            hal_servo.set_servo_position(servo_angle)
            print(f"ADC Value: {adc_value}, Servo Angle: {servo_angle}")
            sleep(0.1)
    
if __name__ == "__main__":
    main()