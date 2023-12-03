import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wraped_function():
        current_time = time.time()
        function()
        after_function = time.time()
        print(f"{function.__name__} run speed:{after_function-current_time}")
    return wraped_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i*i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i*i

fast_function()
slow_function()