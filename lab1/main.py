# ПЕРЕДЕЛАТЬ ПОДСЧЕТ УГЛА ОТНОСИТЕЛЬНО ВЕКТОРА 


from math import atan, pi
from tkinter import *


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y
    
    def __str__(self):
        return f'({self._x}, {self._y})'


class Vector:
    def __init__(self, point1, point2):
        x_delta = point2.x - point1.x
        y_delta = point2.y - point1.y
        if x_delta == 0 and y_delta > 0:
            self._angle = 90
        elif x_delta == 0 and y_delta <= 0:
            self._angle = -90
        else:
            self._angle = atan(y_delta / x_delta) * 180 / pi
            match x_delta > 0, y_delta > 0:
                case False, True:
                    self._angle += 180
                case False, False:
                    self._angle -= 180

    
    @property
    def angle(self):
        return self._angle
    

def jarvis_algorithm(points_list):
    points_count = len(points_list)
    curr_point = points_list[0]
    perimeter = [curr_point]
    count = 0
    while True:
        ind = points_list.index(curr_point)
        print(curr_point)
        [print(i, end='') for i in points_list[:ind] + points_list[ind+1:]]
        #print(points_list[:ind] + points_list[ind+1:])
        print('\n', list(map(lambda x: Vector(curr_point, x).angle, points_list[:ind] + points_list[ind+1:])))
        next_point = min(points_list[:ind] + points_list[ind+1:], key=lambda x: Vector(curr_point, x).angle)

        perimeter.append(next_point)
        curr_point = next_point
        
        if next_point == perimeter[0]:
            return perimeter

        count += 1
        if count > 1000:
            return '>'



if __name__ == '__main__':
    point1 = Point(200, 100)
    point2 = Point(300, 200)
    point3 = Point(100, 200)
    point4 = Point(200, 200)
    point5 = Point(200, 300)

    points = [point1, point2, point3, point4, point5]
    points.sort(key=lambda item: item.x)
    ans = jarvis_algorithm(points)

    window = Tk()
    window.title('My App')
    canv = Canvas(bg="white", width=1000,height=1000)  
    canv.pack()

    for dot in points:
        canv.create_oval(dot.x - 2, dot.y - 2, dot.x + 2, dot.y + 2)
    if ans != '>':
        for i in range(1, len(ans)):
            canv.create_line(ans[i-1].x, ans[i-1].y, ans[i].x, ans[i].y)
    window.mainloop()
    #[print(i) for i in jarvis_algorithm(points)]
    