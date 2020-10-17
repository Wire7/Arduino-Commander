# Arduino Commander, Written by Mohammad Alsada "wire7 @ Github"
# Special thanks to my wife who supported me by all means to finish the CS50x course!


# First Uplaod the standardFirmata firmware on the arduino using the Arduino IDE
import pyfirmata    # Arduino library
import speech_recognition as sr # Speech Recognition "SR" library from Google
import subprocess   # Text to speach functionality
import sys
import time

def say(text):
    subprocess.call(['say', text])

# Setting up Voice Recognition object
r = sr.Recognizer()
# Select the Arduino port (Can be found in the arduino IDE)
board = pyfirmata.Arduino('/dev/cu.wchusbserial1410')
# Program's welcome message
say("Hello, Commander. How may I help you?")


def main():
    while True:  # keep listning for voice commands 
        #r = sr.Recognizer() # VR object Already defined at the top
        # Initiallize recognized text to be an empty string.
        text = ""
        while text == "":
            with sr.Microphone() as source:
                print("Listening :")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio).lower()
                    print("Your command is : {}".format(text))
                except:
                    print("Sorry, could not recognize what you said")
            
        while True:
            if ((("blink" in text) or ("blinking" in text)) and (("led" in text) or ("leds" in text))):
                # Detect numbers in a string and append them in a list "numbers" then use the first detected number only!
                numbers = []
                for word in text.split():
                    if word.isdigit():
                        numbers.append(int(word))  
                    elif word == "one":
                        numbers = [1]      
                if numbers[0] == 0:
                    print("Ok, Not going to blink the LEDs!")
                    break               
                else:
                    blink(numbers[0])
                    break
            # Pre-programmed commands:    
            if ((("dance" in text) or ("dancer" in text)) and (("led" in text) or ("leds" in text))):
                led_dance()
                break
            
            if (("on" in text) and (("led" in text) or ("leds" in text)) and ("red" in text)):
                toggle_led(11,1)
                break

            if (("off" in text) and (("led" in text) or ("leds" in text)) and ("red" in text)):
                toggle_led(11,0)
                break   

            if (("on" in text) and (("led" in text) or ("leds" in text)) and ("blue" in text)):
                toggle_led(12,1)
                break

            if (("off" in text) and (("led" in text) or ("leds" in text)) and ("blue" in text)):
                toggle_led(12,0)
                break   

            if (("on" in text) and (("led" in text) or ("leds" in text)) and ("green" in text)):
                toggle_led(13,1)
                break

            if (("off" in text) and (("led" in text) or ("leds" in text)) and ("green" in text)):
                toggle_led(13,0)
                break

            if (("all" in text) and ("on" in text) and (("led" in text) or ("leds" in text))):
                toggle_led(13,1)
                toggle_led(12,1)
                toggle_led(11,1)
                break

            if (("all" in text) and ("off" in text) and (("led" in text) or ("leds" in text))):
                toggle_led(13,0)
                toggle_led(12,0)
                toggle_led(11,0)
                break

            if (("bambam" in text) or (("bam bam" in text) or ("bum bum" in text))):
                bambam()
                break   
            # Terminate The voice commaned
            if (("voice" in text) and ("command" in text) and (("off" in text) or ("terminate" in text))):
                say("Terminating Voice command, see you soon commander")
                sys.exit()
            
            else:
                break


# Function Defines:
def bambam():
    toggle_led(11,0)
    toggle_led(12,0)
    toggle_led(13,0)
    dt = 0.05
    for _ in range(10):
        board.digital[13].write(1)
        board.digital[12].write(1)
        board.digital[11].write(1)
        time.sleep(dt)
        board.digital[13].write(0)
        board.digital[12].write(0)
        board.digital[11].write(0)
        time.sleep(dt)
    return

def toggle_led(pin, state):
    board.digital[pin].write(state)

def led_dance():
    toggle_led(11,0)
    toggle_led(12,0)
    toggle_led(13,0)
    dt = 0.05   # delay time
    for _ in range(5):
        board.digital[13].write(1)
        time.sleep(dt)
        board.digital[12].write(1)
        time.sleep(dt)
        board.digital[11].write(1)
        time.sleep(dt)
        board.digital[13].write(0)
        time.sleep(dt)
        board.digital[12].write(0)
        time.sleep(dt)
        board.digital[11].write(0)
        time.sleep(dt)
        board.digital[11].write(1)
        time.sleep(dt)
        board.digital[12].write(1)
        time.sleep(dt)
        board.digital[13].write(1)
        time.sleep(dt)
        board.digital[11].write(0)
        time.sleep(dt)
        board.digital[12].write(0)
        time.sleep(dt)
        board.digital[13].write(0)
        time.sleep(dt)

def blink(blinks):
    toggle_led(11,0)
    toggle_led(12,0)
    toggle_led(13,0)
    if blinks > 10:
        while True:
            text = ""
            say(f"Are you sure you want to blink the leds for {blinks} times?")
            with sr.Microphone() as source:
                print("Listning :")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio).lower()
                    print("Your command is : {}".format(text))
                except:
                    print("Sorry, could not recognize what you said")
            if "yes" in text and "no" not in text:
                break
            else:
                return

    dt = 0.15   # Time delay
    for blinks in range(blinks):
        board.digital[13].write(1)
        board.digital[12].write(1)
        board.digital[11].write(1)
        time.sleep(dt)
        board.digital[13].write(0)
        board.digital[12].write(0)
        board.digital[11].write(0)
        time.sleep(dt)
    return
# Function Defines End

main()