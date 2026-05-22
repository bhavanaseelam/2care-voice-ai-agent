import time


def start_timer():

    return time.time()


def end_timer(start_time):

    end_time = time.time()

    latency = end_time - start_time

    return round(latency, 2)