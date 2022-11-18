def PrimeCheck(num: int):
    if num < 2:
        return False
    for n in range(2, num-1):
        if num % n == 0:
            return False
    return True

def NextPrime(num: int):
    temp = num+1
    while not PrimeCheck(temp):
        temp += 1
    return temp

def perfectSquare(num) -> list:
    outOfRoot = 1
    prime = 1

    while prime**2 < num:
        prime = NextPrime(prime)
        if num % prime**2 == 0:
            outOfRoot *= prime
            num /= prime**2
            prime = 1
    return [outOfRoot, int(num)]

class SquareRoot:
    def __init__(self, value) -> None:
        self.outOfRoot = perfectSquare(value)[0]
        self.inRoot = perfectSquare(value)[1]

    def __str__(self) -> str:
        representInRoot = self.inRoot
        if representInRoot == 1:
            return f"{self.outOfRoot}"
        elif self.outOfRoot == 1:
            return f"√{self.inRoot}"
        else:
            return f"{self.outOfRoot}√{self.inRoot}"
    
    def __repr__(self) -> str:
        representInRoot = self.inRoot
        if representInRoot == 1:
            return f"{self.outOfRoot}"
        elif self.outOfRoot == 1:
            return f"√{self.inRoot}"
        else:
            return f"{self.outOfRoot}√{self.inRoot}"
  
def Difference(num: int, num2: int):
    diff = num - num2
    if diff < 0:
        diff = -diff
    return diff

class Coordinates2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def goTo(self, x: int, y:int):
        xWay = Difference(x, self.x)
        yWay = Difference(y, self.y)
        wayTotal = SquareRoot(xWay**2 + yWay**2)
        return f"You have to move {wayTotal} units."


class Coordinates3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def goTo(self, x: int, y:int, z: int):
        xWay = Difference(x, self.x)
        yWay = Difference(y, self.y)
        zWay = Difference(z, self.z)
        wayTotal = SquareRoot(xWay**2 + yWay**2 + zWay**2)
        return f"You have to move {wayTotal} units."
