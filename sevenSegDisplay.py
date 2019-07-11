# This program use 7 segments to display numbers and letters in the
# hexadecimal range. Each segment is made of 3 LEDSs.

from gpiozero import *
from time import sleep

seg0 = LED(18)
seg1 = LED(23)
seg2 = LED(24)
seg3 = LED(19)
seg4 = LED(16)
seg5 = LED(20)
seg6 = LED(26)

def clear():
    seg0.off()
    seg1.off()
    seg2.off()
    seg3.off()
    seg4.off()
    seg5.off()
    seg6.off()

# dictionary below: the patterns are easy to index as strings(sets)

pattern = {
    0: "1111110",
    1: "0110000",
    2: "1101101",
    3: "1111001",
    4: "0110011",
    5: "1011011",
    6: "1011111",
    7: "1110000",
    8: "1111111",
    9: "1111011",
    "0": "1111110",
    "1": "0110000",
    "2": "1101101",
    "3": "1111001",
    "4": "0110011",
    "5": "1011011",
    "6": "1011111",
    "7": "1110000",
    "8": "1111111",
    "9": "1111011",
    "a": "1110111",
    "b": "0011111",
    "c": "0001101",
    "d": "0111101",
    "e": "1001111",
    "f": "1000111",
    "A": "1110111",
    "B": "0011111",
    "C": "1001110",
    "D": "0111101",
    "E": "1001111",
    "F": "1000111",
}

def display(number):
    clear()
    this_pattern = pattern[number]
    if this_pattern[0] == "1":
        seg0.on()
    if this_pattern[1] == "1":
        seg1.on()
    if this_pattern[2] == "1":
        seg2.on()
    if this_pattern[3] == "1":
        seg3.on()
    if this_pattern[4] == "1":
        seg4.on()
    if this_pattern[5] == "1":
        seg5.on()
    if this_pattern[6] == "1":
        seg6.on()

# examples:

display(0)
sleep(1)

display(1)
sleep(1)

display(2)
sleep(1)

display(3)
sleep(1)

display(4)
sleep(1)

display(5)
sleep(1)

display(6)
sleep(1)

display(7)
sleep(1)

display(8)
sleep(1)

display(9)
sleep(1)

display("a")
sleep(1)

display("b")
sleep(1)

display("c")
sleep(1)

display("d")
sleep(1)

display("e")
sleep(1)

display("f")
sleep(1)

display("C")
sleep(1)
