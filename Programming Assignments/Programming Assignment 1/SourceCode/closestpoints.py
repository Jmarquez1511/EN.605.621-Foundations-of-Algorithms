from SourceCode.mergesort import mergesort, mergesort_points
from SourceCode.point import Point
import math

operations = 0

def distance(a, b):
    """
    computes and returns the euclidean distance between points a and b
    :param a: Point()
    :param b: Point()
    :return: float value
    """
    global operations
    distance = math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    operations += 1
    return distance


def divide_and_conquer_m_closest_pairs(points, m, operations):
    xsorted = points.copy()
    mergesort_points(xsorted, 'x')
    ysorted = points.copy()
    mergesort_points(ysorted, 'y')
    result, operations = closest_m_pairs_helper(xsorted, ysorted, m, operations)
    return result, operations


def closest_m_pairs_helper(xsorted, ysorted, m, operations):
    if len(xsorted) <= m+3:
        return brute_force_closest_m_pairs(xsorted, m, operations)
    midx = len(xsorted)//2
    xl = xsorted[:midx]
    xr = xsorted[midx:]

    # Gather the midpoint coordinates
    xvalue = xsorted[midx].get('x')

    yl = []
    yr = []

    for point in ysorted:
        operations += 1
        if point.get('x') <= xvalue:
            yl.append(point)
        else:
            yr.append(point)

    # call recursively both arrays after split
    # find the m closest points in the left half
    result1, operations = closest_m_pairs_helper(xl, yl, m, operations)
    # find the m closest points in the right half
    result2, operations = closest_m_pairs_helper(xr, yr, m, operations)

    # deltas denote the max distance from each result
    delta1 = result1[len(result1)-1]['distance']
    #print(f'delta1:{delta1}')
    delta2 = result2[len(result2)-1]['distance']
    #print(f'delta2:{delta2}')
    delta = delta1 if delta1 <= delta2 else delta2

    ysorted_ = [point for point in ysorted if point.x - delta <= point.x <= point.x + delta]

    result3 = {}
    for i in range(len(ysorted_)):
        operations += 1
        for j in range(i+1, min(i+7, len(ysorted_))):
            operations += 1
            p, q = ysorted_[i], ysorted_[j]
            distance_ = distance(p, q)
            if distance_ < delta:
                result3[i] = {}
                result3[i]['distance'] = distance_
                #print(distance_)
                result3[i]['points'] = (p, q)
                delta = distance_

    overall_result = {}
    final_distances = []

    for result in [result1, result2, result3]:
        operations += 1
        for i in result:
            operations += 1
            if result[i]['distance'] not in overall_result:
                overall_result[result[i]['distance']] = {}
                overall_result[result[i]['distance']]['points'] = result[i]['points']
                final_distances.append(result[i]['distance'])

    mergesort(final_distances)
    final_result = {}

    for i in range(m):
        #operations += 1
        final_result[i] = {}
        final_result[i]['distance'] = final_distances[i]
        final_result[i]['points'] = overall_result[final_distances[i]]['points']

    return final_result, operations


def brute_force_closest_m_pairs(points, m, operations):
    """
    This method uses a nested for loop to compute and return the smallest distances and their corresponding points
    :param points:
    :param m: number of points
    :return:
    """

    distances = {}
    n = len(points)
    for i in range(n):
        operations += 1
        for j in range(i, n):
            operations += 1
            distances[distance(points[i], points[j])] = (points[i], points[j])

    sorted_distances = [key for key in distances]
    mergesort(sorted_distances)
    result = {}
    for i in range(m):
        operations += 1
        result[i] = {}
        result[i]['distance'] = sorted_distances[i]
        result[i]['points'] = distances[sorted_distances[i]]
    return result, operations


if __name__ == '__main__':
    from numpy.random import default_rng
    xrange = default_rng()
    yrange = default_rng()
    x_values = xrange.choice(2000, size=200, replace=False)
    y_values = yrange.choice(2000, size=200, replace=False)
    points = [Point(x_values[i], y_values[i]) for i in range(100)]
    m = 100
    final_result = brute_force_closest_m_pairs(points, m)
    for i in final_result:
        print(final_result[i]['distance'], final_result[i]['points'][0].__str__(), final_result[i]['points'][1].__str__())
    print()
    mergesort_points(points, 'y')
    dc_result = divide_and_conquer_m_closest_pairs(points, m)
    for i in final_result:
        print(dc_result[i]['distance'], dc_result[i]['points'][0].__str__(),
              dc_result[i]['points'][1].__str__())
    print()