import time

class taximeter:
    fare_stopped = 0.02
    fare_moving= 0.05


    def greeting():
        print('*' * 50)
        print('*' *10 + " Welcome to digital taximeter " + '*' * 10)
        print('*' * 50)
    
    greeting()

    def __init__(self):
        print(5)