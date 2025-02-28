from __future__ import annotations # this import is done to allow adding type hints for the classes while being defined


class Point:
    """Point class represents and manipulates x,y coordinates."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Creates a new point at x, y, where by default the point is created at (0,0)."""
        self.x = x
        self.y = y


class Circle:
    """Circle class represents and manipulates center point and radius of a circle."""

    pass


class SMSsStore:
    """SMSsStore class represents the inbox of a phone that includes the messages with relevant information."""

    pass
