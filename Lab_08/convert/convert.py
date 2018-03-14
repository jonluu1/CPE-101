def float_default(string, default = 0):
    try:
        return float(string)
    except:
        return default