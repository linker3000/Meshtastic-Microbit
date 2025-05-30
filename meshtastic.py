from microbit import *

uart.init(baudrate=19200, tx=pin0, rx=pin1)

blink_state = 0
last_blink_time = running_time()
# print("UART-to-USB bridge started")
display.scroll("Ready ", delay=100)

def send_message_a():
    message = "The first ever message sent from a BBC Micro:bit?!\r\n"
    uart.write(message)
    display.scroll("BTN A", delay=100)
    # print("Sent A:", message.strip())

def send_message_b():
    message = "Hello from BBC Micro:bit button B!\r\n"
    uart.write(message)
    display.scroll("BTN B", delay=100)
    # print("Sent B:", message.strip())

while True:
    
    # Button presses
    if button_a.was_pressed():
        send_message_a()
    if button_b.was_pressed():
        send_message_b()
        
    display.set_pixel(4, 4, blink_state * 5)
    if uart.any():
        display.set_pixel(4, 4, 9)  # Show byte received
        printable = ''
        data = uart.read()
        if data:
            text = str(data, 'utf-8')
            for c in text:
                if 32 <= ord(c) <= 126:
                    printable = printable + c
            if printable:
                display.scroll(printable, delay=100)
                
    else:
        # Blink idle indicator
        now = running_time()
        if now - last_blink_time > 500:
            blink_state = 1 - blink_state
            display.set_pixel(4, 4, blink_state * 5)
            last_blink_time = now
    sleep(250)
