import numpy as np
import time

# this function calculates factorial up to n order
def factorial(n):
    result = 1
    for i in range(1,n+1,1):
        result = result*i
    return result

# this function calculates the sin(x) using Talyor expansion up to order n
def sin_talyor(x,order):
    if order%2 == 0:
        n = int(order/2) - 1
    else:
        n = order//2
    result = 0
    for i in range(0,n+1,1):
        divisor = factorial(2*i+1)
        numerator = np.power(-1,i)*np.power(x,2*i+1)
        result = result + (numerator/divisor)
    return result

# this function compares result of sin(x) from Talyor expression to the one calculated using nump.sin
def sin_compare(x, n, decimal):
    start_time = time.time()
    np_result = np.round(np.sin(x), decimal)
    np_duration = time.time() - start_time
    start_time = time.time()
    talyor_result = np.round(sin_talyor(x,n), decimal)
    talyor_duration = time.time() - start_time
    print(f"""
        Computing sin({x}). \n
        The numpy.sin result is: {np_result}, the duration is {np_duration}. \n
        The Talyor explansion result with order {n} is: {talyor_result}, the duration is {talyor_duration}.
        """)

