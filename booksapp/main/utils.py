import math

def round_decimal(dec, pre):
    return  math.floor(dec * math.pow(10, pre)) / math.pow(10, pre)

