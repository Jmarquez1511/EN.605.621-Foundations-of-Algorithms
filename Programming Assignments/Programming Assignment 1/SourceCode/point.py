class Point:
    """
    We use the Point class to define a point with x and y coordinates. This class only has an __init__ method.
    """
    def __init__(self, x, y):
        """
        Initiate a Point(x,y)
        :param x: x-coordinate
        :param y: y-coordinate
        """
        self.x = x
        self.y = y

    def get(self, toget):
        """
        Helper function to get the x or y values by passing a string
        :param toget:
        :return:
        """
        if toget == 'x':
            return self.x
        else:
            return self.y

    def __str__(self):
        return f'({self.x},{self.y})'


