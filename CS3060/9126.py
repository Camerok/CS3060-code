
def calculate_circle_properties():
    radius = 4.15
    pi = 22/7
    circle_area = pi * (radius ** 2)
    circle_circumference = 2 * pi * radius

    print("The area of the circle is:", circle_area)
    print("The circumference of the circle is:", circle_circumference)


def string_examples():
    s1 = "hello"
    s2 = 'world'
    s3 = """multi-line"""
    print(s1, s2, s3)
    s1 = str(123) # '123'
    s1 = "hello" + "world"
    print(s1)
    s1 = "no"
    s2 = s1*3 #'nonono'
    print(s1, s2)
    s = "Python"
    s[0] #"P"
    s[-1] #"n"
    print(s, s[0], s[-1])


def string_examples2():
    x = "+"
    c = "/"
    s1 = "s" + x + 2*c
    y = "a"
    z = "b"
    x = "2"
    s2 = (y+z)*int(x)
    print(s1, s2)

def length_string():
    len("Rossum") # 6
    a = len("Rossum") # 6
    print(a)

def string_slicing():
    s1 = "Rossum"
    s1[2:4] # 'ss'

    s1[2:5:1] # 'ssu'
    s1[2:5:2] # 'su'
    s1[2:5:1] # is same as s1[2:5]
    print(s1[2:4], s1[2:5:1], s1[2:5:2], s1[2:5:1])
    print(s1[2:3])
    print(s1[3:5])
    print(s1[4:5])
    print(s1[1:5:2])
    print(s1[:])
    print(s1[:-2])
    print(s1[::-1])
    print(s1[1::-2])
    print(s1[0:len(s1):1])


def main():
    calculate_circle_properties()
    string_examples()
    string_examples2()
    length_string()
    string_slicing()


main()
