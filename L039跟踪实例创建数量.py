class ObjectNumCalc:
    count = 0

    def __init__(self):
        ObjectNumCalc.count += 1

    def __del__(self):
        ObjectNumCalc.count -= 1

    
