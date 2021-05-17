#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    except:
        print("Inside result: {}".format(None))
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
