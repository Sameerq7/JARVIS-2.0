import time
import sys

def print_slow(text, delay=0.1):
     # Start printing on a new line
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    

