import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*argsm, **kwargs):
        res = func(*argsm, **kwargs)
        return json.dumps(res)
    return wrapped