from math import atan2, pi
from tkinter import *


def angle(dot1, dot2, dot3):
   vec1 = (dot2[0] - dot1[0], dot2[1] - dot1[1])
   vec2 = (dot3[0] - dot2[0], dot3[1] - dot2[1])
   angle = atan2(vec2[1], vec2[0]) - atan2(vec1[1], vec1[0])
   if angle < 0:
       return 360 + angle * 180 / pi
   return angle * 180 / pi

def jarvis_algorithm(points):
    perimeter = [points[0]]
    prev_point = (points[0][0], points[0][1] + 10)
    count = 0
    while count < len(points)*2:
        angles_list = list(angle(prev_point, perimeter[-1], dot) for dot in points)
        next_point = points[angles_list.index(min(angles_list))]
        print(min(angles_list), '\t', *list(map(int, angles_list)))
        prev_point = perimeter[-1]
        perimeter.append(next_point)
        points.remove(next_point)
        if next_point == perimeter[0]:
            return perimeter
    return '!'



if __name__ == '__main__':
    window = Tk()
    window.title('My App')
    canv = Canvas(bg="white", width=1000,height=1000)  
    canv.pack()

    points = [
        (200, 110),
        (330, 200),
        (200, 660),
        (770, 350),
        (350, 500),
        (110, 200),
        (200, 330),
        (731, 314),
        (148, 800),
        ]
    
    min_id = points.index(min(points, key=lambda item : item[0]))
    points[min_id], points[0] = points[0], points[min_id]

    if len(points) < 3:
        print('NO')

    for dot in points:
        canv.create_oval(dot[0] - 2, dot[1] - 2, dot[0] + 2, dot[1] + 2)
    
    ans = jarvis_algorithm(points)

    if ans != '!':
        print('YES')
        for i in range(1, len(ans)):
            canv.create_line(ans[i-1][0], ans[i-1][1], ans[i][0], ans[i][1])
    else:
        print('NO')
    window.mainloop()
    
