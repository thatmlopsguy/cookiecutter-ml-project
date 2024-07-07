import functools
import warnings
import timeit

def deprecated_msg(msg: str):
    warning_color = "\033[93m"  # orange/yellow ascii escape sequence
    end = "\033[0m"  # end ascii escape sequence
    warnings.simplefilter("always", DeprecationWarning)
    warnings.warn(
        f"{warning_color}{msg}{end}",
        category=DeprecationWarning,
        stacklevel=2,
    )
    warnings.simplefilter("default", DeprecationWarning)


def deprecated(reason: str):
    """Logs a warning that a function is deprecated"""

    def wrap(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            deprecated_msg(msg=f"{func.__name__} is deprecated! explanation: {reason}")
            return func(*args, **kwargs)

        return wrapped

    return wrap

def collect_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "reset" in kwargs and kwargs["reset"]:
            wrapper.time_taken = 0
            wrapper.count = 0
        else:
            start = timeit.default_timer()
            result = func(*args, **kwargs)
            wrapper.time_taken += (timeit.default_timer() - start) * 1000.0
            wrapper.count += 1
            return result

    wrapper.time_taken = 0
    wrapper.count = 0
    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        duration = (timeit.default_timer() - start) * 1000.0
        wrapper.time_taken = duration
        return result

    return wrapper
