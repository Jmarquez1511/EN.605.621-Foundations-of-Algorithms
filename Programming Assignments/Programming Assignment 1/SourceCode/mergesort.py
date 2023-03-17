"""
This file contains two versions of merge sort, one version merge sorts a list of items.
The other version sorts a list of Points by either their x or y coordinates
"""


def mergesort(alist):
    """
    This implementation can be found in
    https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html.
    :param alist:
    :return:
    """
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


def mergesort_points(pointslist, sortby):
    """
    This implementation can be found in
    https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html. It corresponds to a classical
    implementation of merge sort which is O(nlgn). We make a simple adjustment by sorting by Point.x or Point.y by
    using the Point.get() method while passing the sortby parameter.
    :param pointslist:
    :return: a sorted list
    """

    if len(pointslist) > 1:
        mid = len(pointslist)//2
        lefthalf = pointslist[:mid]
        righthalf = pointslist[mid:]

        mergesort_points(lefthalf, sortby)
        mergesort_points(righthalf, sortby)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].get(sortby) <= righthalf[j].get(sortby):
                pointslist[k] = lefthalf[i]
                i = i+1
            else:
                pointslist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            pointslist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            pointslist[k] = righthalf[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    from SourceCode.point import Point
    pointslist = [Point(5, 12000), Point(1, 2), Point(-500, -8000)]
    mergesort_points(pointslist, 'y')
    print([point.y for point in pointslist])







