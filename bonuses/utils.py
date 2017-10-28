import time
from collections import Counter
from functools import wraps

from flask import request, current_app


def make_bruteforce_ip_filter(window_cfg, threshold_cfg, lag_cfg):

    def decorator(func):

        tracking_time = None
        counter = None

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal tracking_time, counter

            window = current_app.config[window_cfg]
            threshold = current_app.config[threshold_cfg]
            lag = current_app.config[lag_cfg]

            current_time = int(time.time()) // window * window
            if current_time != tracking_time:
                tracking_time = current_time
                counter = Counter()

            request_ip = request.remote_addr
            counter[request_ip] += 1
            if counter[request_ip] > threshold:
                time.sleep(lag)

            return func(*args, **kwargs)

        return wrapper

    return decorator
