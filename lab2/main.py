import matplotlib.pyplot as plt
from math import sqrt, hypot


MIN = 1e-16


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'


class Section:
    def __init__(self, point1, point2):
        self.a = point1
        self.b = point2
        self.length = sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)


class Line:
    def __init__(self, point1 = None, point2 = None, a = None, b = None, c = None):
        if point1 and point2:
            self.p1 = point1
            self.p2 = point2
            self.a = point2.x - point1.x
            self.b = point2.y - point1.y
            self.c = point2.x * point1.y - point1.x * point2.y
        elif a and b and c:
            self.a = a
            self.b = b
            self.c = c
            self.p1 = Point(a, -((a + c) / b))
            self.p2 = Point(2 * a, -((2 * a + c) / b))


class Triangle:
    def __init__(self, vert1, vert2, vert3):
        self.vert1 = vert1
        self.vert2 = vert2
        self.vert3 = vert3
    
    def __repr__(self):
        return f'[{self.vert1} {self.vert2} {self.vert3}]'


class Circle:
    def __init__(self, center : Point, radius : int):
        self.center = center
        self.r = radius


##################################### ДОП ЗАДАЧИ ###################################################


def lines_intersect(line1, line2):
    # line1.a/line2.a = line1.b/line2.b перемножаем крест накрест и все влево
    if line1.a * line2.b - line1.b * line2.a < MIN:
        return None
    
    x = (line2.a * line1.c - line1.a * line2.c) / (line1.a * line2.b - line1.b * line2.a)
    y = -(line1.b * line2.c - line2.b * line1.c) / (line1.a * line2.b - line1.b * line2.a)

    return (x, y)


def line_section_intersect(line, section):
    # используем уже реализованную функцию пересечения двух прямых
    intsect = lines_intersect(line, Line(section.a, section.b))
    x1, x2 = min(section.a.x, section.b.x), max(section.a.x, section.b.x)
    y1, y2 = min(section.a.y, section.b.y), max(section.a.y, section.b.y)
    # если точка пересечения за отрезком
    if intsect and (x1 < intsect[0] < x2) and (y1 < intsect[1] < y2):
        return intsect
    return None


def sections_intersect(section1, section2):
    intsect = line_section_intersect(Line(section1.a, section1.b), section2)
    x1, x2 = min(section1.a.x, section1.b.x), max(section1.a.x, section1.b.x)
    y1, y2 = min(section1.a.y, section1.b.y), max(section1.a.y, section1.b.y)

    if intsect and (x1 < intsect[0] < x2) and (y1 < intsect[1] < y2):
        return intsect
    return None


def line_circle_intersect(line, circle):
    # вектор от точки на прямой (любой) до оцентра окружности 
    fx = line.p1.x - circle.center.x
    fy = line.p1.y - circle.center.y
    # квадратное уравнение для поиска точек пересечения
    a = line.a ** 2 + line.b ** 2
    b = 2 * (fx * line.a + fy * line.b)
    c = fx ** 2 + fy ** 2 - circle.r ** 2
    D = b**2 - 4*a*c
    
    if D < 0:
        return []
    # параметры уравнения
    t1 = (-b + sqrt(D)) / (2*a)
    t2 = (-b - sqrt(D)) / (2*a)
    points = list()
    if 0 <= t1 <= 1:
        points.append(Point(line.p1.x + t1 * line.a, line.p1.y + t1 * line.b))
    if D > 0 and 0 <= t2 <= 1:
        points.append(Point(line.p1.x + t2 * line.b, line.p1.y + t2 * line.b))

    return points


def section_circle_intersect(section, circle):
    points = line_circle_intersect(Line(section.a, section.b), circle)
    x1, x2 = min(section.a.x, section.b.x), max(section.a.x, section.b.x)
    y1, y2 = min(section.a.y, section.b.y), max(section.a.y, section.b.y)
    for point in points:
        if not(x1 < (point.x) < x2 and y1 < (point.y) < y2):
            points.remove(point)
    return points


def circles_intersect(circle1, circle2):
    d = hypot(circle2.center.x - circle1.center.x, circle2.center.y - circle1.center.y)
    # расстояние между центрами больше суммы радиусов => не пересекаются
    if d > circle1.r + circle2.r or d < abs(circle1.r - circle2.r):
        return []
    # окружности совпадают
    if abs(d) < MIN and abs(circle1.r - circle2.r) < MIN:
        return None
        
    a = (circle1.r ** 2 - circle2.r ** 2 + d ** 2) / (2 * d)
    h0 = circle1.center.x + (circle2.center.x - circle1.center.x) * a / d
    k0 = circle1.center.y + (circle2.center.y - circle1.center.y) * a / d
    # расстояние от точки на соеднинении центроы до точек пересечения
    h = sqrt(max(circle1.r ** 2 - a ** 2, 0))
    # если = 0, то одна точка пересечения
    if abs(h) < MIN:
        return [(h0, k0)]
    else:
        # Перпендикулярный вектор к направлению между центрами
        rx = -(circle2.center.y - circle1.center.y) * (h / d)
        ry = (circle2.center.x - circle1.center.x) * (h / d)
        p1 = (h0 + rx, k0 + ry)
        p2 = (h0 - rx, k0 - ry)
        return [p1, p2]


################################ ВЛОЖЕННЫЙ ТРЕУГОЛЬНИК #############################################


# находятся ли обе точки по одну сторону от прямой
def on_same_side(line, point1, point2):
    # ориентированная площадь треугольника из стороны и точки
    sq1 = (point1.x - line.p1.x) * (line.p2.y - line.p1.y) - (point1.y - line.p1.y) * (line.p2.x - line.p1.x)
    sq2 = (point2.x - line.p1.x) * (line.p2.y - line.p1.y) - (point2.y - line.p1.y) * (line.p2.x - line.p1.x)
    if abs(sq1) < MIN or abs(sq2) < MIN:
        return False
    # если однозначны => лежат по одну сторону от прямой
    return (sq1 * sq2) > 0


# находится ли точка внутри треугольника
def point_into_triangle(point, triangle):
    center = Point(
        (triangle.vert1.x + triangle.vert2.x + triangle.vert3.x) / 3,
        (triangle.vert1.y + triangle.vert2.y + triangle.vert3.y) / 3
    )
    for i, j in ((triangle.vert1, triangle.vert2), (triangle.vert2, triangle.vert3), (triangle.vert3, triangle.vert1)):
        side = Line(i, j)
        if not on_same_side(side, point, center):
            return False
        return True


# находится ли один треугольник (все его точки) внутри другого
def is_inner(big_tr, small_tr):
    for vert in (small_tr.vert1, small_tr.vert2, small_tr.vert3):
        if not point_into_triangle(vert, big_tr):
            return False
    return True


def any_nested_triangles(points):
    triangles = list()
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                vert1 = Point(points[i][0], points[i][1])
                vert2 = Point(points[j][0], points[j][1])
                vert3 = Point(points[k][0], points[k][1])
                if lines_intersect(Line(vert1, vert2), Line(vert1, vert3)):
                    triangles.append(Triangle(vert1, vert2, vert3))

    n = len(triangles)
    for i in range(n):
        for j in range(i + 1, n):
            if is_inner(triangles[i], triangles[j]):
                return f'треугольник: {triangles[j]} вложен в {triangles[i]}'
            elif is_inner(triangles[j], triangles[i]):
                return f'треугольник: {triangles[i]} вложен в {triangles[j]}'
    return 'вложенных треугольников нет'


if __name__ == '__main__':
    line1 = Line(Point(8, -2), Point(2, 10))
    line2 = Line(Point(0, 0), Point(4, 4))
    section1 = Section(Point(3, -6), Point(-1, -1))
    section2 = Section(Point(4, 4), Point(0, -4))
    circle1 = Circle(Point(-1, 3), 6)
    circle2 = Circle(Point(2, -4), 10)

    print(lines_intersect(line1, line2))
    print(line_section_intersect(line1, section1))
    print(sections_intersect(section1, section2))
    print(line_circle_intersect(line1, circle1))
    print(section_circle_intersect(section1, circle1))
    print(circles_intersect(circle1, circle2))

    points = [
        (0, 6), (0, 0), (4, 0),
        (1, 1), (1, 2), (2, 1)
    ]
    
    print(any_nested_triangles(points))
