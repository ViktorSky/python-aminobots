import collections.abc

__all__ = ("iterable", )


def iterable(__obj: object) -> bool:
    """Return whether the object is iterable (i.e., some kind of iterator).
    
    Note that any object is iterable when it has a __iter__() or __getitem__ method."""
    return isinstance(__obj, collections.abc.Iterable)
