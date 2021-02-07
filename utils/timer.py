import time


def timer(algorithm_function):
    def modified_function(*args):
        time_before = time.time()
        result = algorithm_function(*args)
        time_after = time.time()
        execution_time = time_after - time_before
        return result, execution_time
    return modified_function
