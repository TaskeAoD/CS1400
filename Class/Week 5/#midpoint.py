#midpoint

def midpoint(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return (x1 + x2)/2, (y1 + y2)/2

point1 = float(input("Enter X1: ")), \
    float(input("Enter y1: "))
point2 = float(input("Enter X2: ")), \
    float(input("Enter y2: "))

mid = midpoint(point1, point2)
print(f"Midpoint of {point1} and {point2} is {mid}")