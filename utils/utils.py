import inspect


URL = "https://aviata.kz/"

def whoami():
    return inspect.stack()[1][3]