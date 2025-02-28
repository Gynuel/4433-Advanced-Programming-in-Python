from solutions import Point, Circle
from pytest import mark, raises
import random


def test_point() -> None:
    p = Point(random.randint(-10, 10), random.randint(-10, 10))
    assert "_x" in dir(p) and "_y" in dir(p) and p._x == p.x and p._y == p.y


@mark.parametrize(
    "x1, y1, x2, y2, distance",
    [
        (0, 0, 0, 0, 0),
        (0, 0, 0, 5, 5),
        (0, 0, 5, 0, 5),
        (0, 0, 3, 4, 5),
        (1, 2, 4, 6, 5),
    ],
)
def test_point_distance_to(x1: int, y1: int, x2: int, y2: int, distance: float) -> None:
    assert Point(x1, y1).distance_to(Point(x2, y2)) == distance


@mark.parametrize("x1, y1, x2, y2, m, c", [(4, 11, 6, 15, 2, 3), (0, 0, 1, 1, 1, 0)])
def test_point_calculate_equation(
    x1: int, y1: int, x2: int, y2: int, m: float, c: float
) -> None:
    assert Point(x1, y1).calculate_equation(Point(x2, y2)) == (m, c)


def test_point_calculate_equation_fails_on_equal_x() -> None:
    with raises(ZeroDivisionError):
        Point(1, 2).calculate_equation(Point(1, 3))


@mark.parametrize("x, y", [(0, 0), (-5, 0), (3, 4), (6, -3)])
def test_point_move_to(x: int, y: int) -> None:
    p = Point(random.randint(-10, 10), random.randint(-10, 10))
    p.move_to(x, y)
    assert p.x == x and p.y == y


@mark.parametrize(
    "r, x, y, expected",
    [(4, 0, 0, 50.27), (0, 0, -5, 0), (1, -7, -3, 3.14), (7, 2, -4, 153.94)],
)
def test_circle_area(r: int, x: int, y: int, expected: float) -> None:
    p = Point(x, y)
    c = Circle(r, p)
    assert round(c.area, 2) == expected


def test_circle_area_read_only() -> None:
    p = Point(0, 0)
    c = Circle(1, p)
    with raises(AttributeError) as error:
        # we add the end comment to the following line to tell pylance to not raise the corresponding warning
        c.area = 9 # type: ignore
    assert "can't set attribute 'area'" == error.value.args[0]


@mark.parametrize("r, x, y", [(4, 0, 0), (0, 0, -5), (1, -7, -3), (7, 2, -4)])
def test_circle_move_to(r: int, x: int, y: int) -> None:
    p = Point(random.randint(-10, 10), random.randint(-10, 10))
    c = Circle(r, p)
    c.move_to(x, y)
    assert p.x == x and p.y == y and c.radius == r and c.point == p


@mark.parametrize(
    "r1, x1, y1, r2, x2, y2, expected",
    [
        (4, 0, 0, 2, 0, 0, True),
        (3, 0, -5, 2, 0, 0, True),
        (1, -7, -3, 3, 4, -4, False),
        (4, 1, 2, 4, -6, -3, False),
    ],
)
def test_circle_is_touching(
    r1: int, x1: int, y1: int, r2: int, x2: int, y2: int, expected: bool
) -> None:
    c1 = Circle(r1, Point(x1, y1))
    c2 = Circle(r2, Point(x2, y2))
    assert c1.is_touching(c2) == expected
