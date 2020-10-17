# Arduino-Commander
A voice controlled Arduino


This project is a voice command controlled Arduino where 3 LEDs are connected to it and controlled using voice commands. The application is written in Python3 and it mainly uses the open source library of Speech Recognition from Google, also the pyFirmata library which allows the programe to communicate with the Arduino board.

The idea behind the project is to convert the user's speech into somehow a text which then, can be used as a trigger for the Arduino to perform some actions, here, to turn on, turn off or blink an LED or (LEDs) and to terminate the program and exit!

Speech Recognition from Google is a library for performing speech recognition, with support for several engines and APIs, online and offline, it listens to the user voice and then converts it (transcribes it) into a string of text, each of the string's words are compared against some previously set conditions using "if" statements and when the "if" statement is true then the command gets executed, but the must be a communication link between the program running on the computer and the Arduino connected to it and here comes pyFirmata which is a Python interface for the Firmata protocol which must be uploaded to the Arduino board first using the Arduino IDE and selecting "Standard Firmata" from Examples -> Firmata -> StandardFirmata. The pyFirmate library provides a way to allowing the computer running this program to communicate with Arduino.

Finally, this project links between programming and microcontrollers. It has big potentials if developed more because controlling an LED allows us to control larger things such as house appliances handsfree!
