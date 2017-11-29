# -*- encoding: utf-8 -*-

class Proxy(object) :

    proxied = None

    def __init__(self, context) :
        self.context = context

        # if proxied is not provided, build identity proxy
        if self.proxied is None :
            self.proxied = tuple(
                filter(
                    lambda name : not name.startswith('_'),
                    dir(self.context)
                )
            )

    def __getattr__(self, name) :

        if name in self.proxied :
            return getattr(self.context, name)

        return super(Proxy, self).__getattribute__(name)

class Point(object) :

    def __init__(self, x, y ,z) :
        self._x, self._y, self._z = x, y, z

    def x(self) :
        return str(self._x)

    def y(self) :
        return str(self._y)

    def z(self) :
        return str(self._z)

def formatter(point) :

    return "({})".format(
            ', '.join([
                    point.x(),
                    point.y(),
                    point.z()
                    ])
            )


class Projection(Proxy) :

    def z(self) :
        return '0'

class Reduction(Proxy) :

    proxied = ('x', 'y', 'z')


if __name__ == '__main__' :
    p = Point(1, 2, 3)
    print('p=Point(1, 2, 3)\t:', formatter(p))
    print('Proxy(p)\t\t:', formatter(Proxy(p)))
    print('Projection(p)\t\t:', formatter(Projection(p)))
    print('Reduction(p)\t\t:', formatter(Reduction(p)))
