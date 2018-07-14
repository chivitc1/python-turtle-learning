"""
File: flag.py
Defines a Flag class: toggle to True when menu item click, otherwize is False.
"""
class Flag(object):
    """Represents a Boolean flag."""

    def __init__(self, value=False):
        """Sets the initial state."""

        self._value = value

    def value(self, newValue=None):
        """Getter and setter."""

        if not newValue is None:
            self._value = newValue
        return self._value