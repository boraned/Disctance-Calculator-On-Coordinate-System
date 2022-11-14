from CoordinateSystem import Coordinates2D, Coordinates3D

location1 = Coordinates2D(0, 0)

print(location1.goTo(4, 3))

location2 = Coordinates3D(0, 0, 0)

print(location2.goTo(2, 2, 1))
