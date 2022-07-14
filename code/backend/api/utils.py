def isfloat(v):
    try:
        float(v)
        return True
    except ValueError as e:
        return False
