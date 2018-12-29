
def raise_if_not_type(obj, expecting, msg=None, raises=ValueError):
    criteria = expecting if isinstance(expecting, list) else [expecting]
    criteria = list(map(lambda t: t if t else type(t), criteria))
    if not type(obj) in criteria:
        if not msg:
            raise raises()
        raise raises(msg)
