import matplotlib.pyplot as plt
import numpy as np
from itertools import pairwise
import pdb

def get_unit_normal(p0, p1, direction):

    line = p1 - p0

    n_v_1 = np.array([-line[1], line[0]])
    n_v_2 = np.array([line[1], -line[0]])

    normal_vector = n_v_1 if np.dot(direction, n_v_1) >= 0 else n_v_2
    unit_normal = normal_vector / np.linalg.norm(normal_vector)

    return unit_normal

def pattern(o1, o2, scaling_factor, n, direction):


   # distance to cover
    line = o2 - o1
    distance = np.linalg.norm((line))
    
    # get triange info
    side_distance = scaling_factor * distance / (2 * n)
    base_distance = distance / n
    height_distance = np.sqrt((side_distance ** 2 - (base_distance / 2) ** 2))

    # get heights of triangles
    n_v_1 = np.array([-line[1], line[0]])
    n_v_2 = np.array([line[1], -line[0]])

    normal_vector = n_v_1 if np.dot(direction, n_v_1) >= 0 else n_v_2
    unit_normal = normal_vector / np.linalg.norm(normal_vector)
    heights = []
    triangles = []
    for i in range(n):
        base = o1 + line * (1 + 2 * i) / (2 * n)
        
        triangles.append([o1 + line * i / n, o1 + line * (1 + 2 * i) / (2 * n) + unit_normal * height_distance, o1 + line * (i + 1)/ (n)])
        # heights.append(o1 + np.array([base_distance / 2 + base_distance * i, height_distance])) 
    
    # get bases of triangles
    # bases = [ np.array([o1[0] + i * base_distance, o1[1]]) for i in range(n + 1) ]

    # triangles
    # list of 3 points
    return triangles
    # return [ (bases[i], heights[i], bases[i + 1]) for i in range(len(heights))  ]

def recursive(s1, s2, direction, depth, n, scaling_factor):

    level_points = [(s1, s2, direction)]
    triangles = []
    for d in range(depth):
        
        level = []
        level_triangles = []
        # iterate over level
        while level_points:

            p1, p2, direction = level_points.pop(0)  # get points 

            one_triangle_set = pattern(p1, p2, scaling_factor, n, direction)
            
            level_triangles.extend(one_triangle_set)  # save for answer

            base_points = [[(p[0], p[1], get_unit_normal(p[0], p[1], direction)), (p[1], p[2], get_unit_normal(p[1], p[2], direction))] for p in one_triangle_set]
            level.extend([points for sublist in base_points for points in sublist])  # save for next iteration

            # simple_plot_triangles(level_triangles)
        level_points = level
        triangles.append(level_triangles)


    return triangles


def triangle_center(p1, p2, p3):
    return (p1[0] + p2[0] + p3[0]) / 3 , (p1[1] + p2[1] + p3[1]) / 3

def plot_triangles(triangles):
    
    plt.figure()
    plt.xlim(min(o1[0], o2[0]) - 0.01, max(o1[0], o2[0]) + 0.01)
    plt.ylim(min(o1[1], o2[1])- 0.01, max(o1[1], o2[1]) + 0.01)

    for i in range(len(triangles)):
        plt.gca().add_patch(plt.Polygon(triangles[i], color = 'red')) 


    plt.axis('equal')
    plt.xlim()
    plt.show()

def simple_plot_triangles(triangles):

    xx = [
        p[0] for triangle in triangles
        for p in triangle
    ]

    yy = [
        p[1] for triangle in triangles
        for p in triangle
    ]


    plt.plot(xx, yy,'b-o')
    plt.show()

if __name__ == "__main__":
    o1 = np.array([0,0])
    o2 = np.array([1,0])
    direction = np.array([0, 1])

    num_triangles = 10
    scale = 1.5
    depth = 3

    # triangles = pattern(o1, o2, scaling_factor=scale, n=num_triangles)
    triangles = recursive(o1, o2, direction, depth, num_triangles, scale)


    # plt.figure()
    # plt.xlim(min(o1[0], o2[0]) - 0.01, max(o1[0], o2[0]) + 0.01)
    # plt.ylim(min(o1[1], o2[1])- 0.01, max(o1[1], o2[1]) + 0.01)

    # for i in range(len(triangles[-1])):
    #     plt.gca().add_patch(plt.Polygon(triangles[-1][i], color = 'red')) 


    


    # plt.axis('equal')
    # plt.xlim()
    # plt.show()

    # sorted_triangles = sorted(triangles[-1], key = lambda x: np.linalg.norm(triangle_center(*x)))
    # sorted_triangles = sorted_triangles[8: 17]

    xx = [
        p[0] for triangle in triangles[-1]
        for p in triangle
    ]

    yy = [
        p[1] for triangle in triangles[-1]
        for p in triangle
    ]

    # print(sorted_triangles)
    # print("++++++++++++++++++++++++++++")
    # print(xx)
    # print(yy)
    print("++++++++++++++++++++")
    plt.plot(xx, yy, 'b-o')
    plt.show()
