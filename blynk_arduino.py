import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem1201')
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
