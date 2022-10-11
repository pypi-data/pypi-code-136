from sympy import Symbol as symbol
from sympy import diff
from sympy import integrate as intg

import random as rn
import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import math as m

pie=22/7

def sgn(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return 0

def gif(n):
    return m.floor(n)


def factorial(n):
    if n==1:
        return n
    elif n==0:
        return n+1
    elif n<0:
        return "Factorial of a negative number does not exist"
    else:
        for i in range(1,n+1):
            factorial=n*(m.factorial(n-1))
            return factorial



def mod(real_number):
    if real_number>0:
        return real_number
    elif real_number<0:
        return -1*real_number
    else:
        return 0

def perarea(b,h):
    a=b*h
    print(f"Height of Parallelogram is: {h} units")
    print(f"Base of Parallelogram is: {b} units")
    print(f"Area of Parallelogram is: {a} units sq")

def traparea(ta,tb,th):
    tpa=(1/2)*(ta+tb)*th
    print(f"Length of first parallel side of Trapezium is: {ta} units")
    print(f"Length of second parallel side of Trapezium is: {tb} units")
    print(f"Height of Trapezium is: {th} units")
    print(f"Area of Trapezium is: {tpa} units sq")

def factors(integer):
    if integer>0:
        print("The factors of",integer,"are:")
        for i in range(1, integer + 1):
            if integer % i == 0:
                print(i)
    elif integer<0:
        print("The factors of",integer,"are:")
        a=-1*integer
        for i in range(integer, 0):
            if integer % i == 0:
                print(i)
        for z in range(1,a+1):
            if integer %z ==0:
                print(z)
    elif integer==0:
        print("Factors of zero does not exist")

def biodata(n):
    if n==0:
        print("Number is:", n)
        print("Number is even")
        print("It's Square is:0")
        print("It's Sruare root is:0")
        print("It's Cube is:0")
        print("It's Cube root is:0")
        print("It's Resiprocal is: infinity") 
        print("It's modulus is:", mod(n))
        factors(n)
        if n<0:
            print("Factorial of zerodoes not exist")
        else:
            a=factorial(n)
            print(f"It's factorial is {a}")
        print("It's greatest integer function is", gif(n))
        print("It's signum function is", sgn(n))
        print("Nether Prime nor Composite")    
    elif n>0 or n<0:
        A_IV=(-1)*n
        sq=n**2
        sq_root=n**(1/2)
        cube=n*n*n
        cb_root=n**(1/3)
        rp=1/n
        print("Number is:", n)
        if n%2==0:
            print("Number is even")
        else:
            print("Number is odd")

        print("It's Additive Inverse is:",  A_IV)
        print("It's Square is:",  sq)
        print("It's Sruare root is:",  sq_root)
        print("It's Cube is:",  cube)
        print("It's Cube root is:",  cb_root)
        print("It's Resiprocal is:",  rp) 
        print("It's modulus is:", mod(n))
        factors(n)
        factorial(n)
        print("It's greatest integer function is", gif(n))
        print("It's signum function is", sgn(n))
        if n>0:
            for i in range(2,n):
                if n%i==0:
                    print("Number is Composite")
                    break
                else:
                    print("Number is Prime")
        elif n<0:
            print("Number is Composite")
        elif n==0:
            print("Zero is neither a prime no a composite number")





def circle(r):
    pie=22/7
    a=pie*(r**2)
    d=2*r
    p=pie*r*2
    print(f"Radius of Circle is: {r} units")
    print(f"Diameter of Circle is: {d} units")
    print(f"Perimeter of Circle is: {p} units")
    print(f"Area of Circle is: {a} units sq")

def rccon(cor,coh):
    pie=22/7
    l=((cor**2)+(coh**2))**(1/2)
    axx=pie*(cor)*(l)
    axy=pie*(cor+l)*cor
    axv=(1/3)*pie*(cor**2)*(coh)
    b=pie*(cor**2)
    print(f"Radius of Circular Right Cone  is: {cor} units")
    print(f"Height of Circular Right Cone  is: {coh} units")
    print(f"Area of bottom of Circular Right Cone: {b} units sq")
    print(f"Curved Surface aera of Circular Right Cone: {axx} units sq")
    print(f"Total Surface aera of Circular Right Cone: {axy} units sq")
    print(f"Slant height of Circular Right Cone: {l} units")
    print(f"Volume of Circular Right Cone: {axv} units cb")

def cube(s):
    sa=s**2
    vc=s**3
    lcb=4*(s**2)
    tcb=6*(s**2)
    print(f"Length of each edge of cube is: {s} units")
    print(f"Surface area of each face of Cube is: {sa} units sq")
    print(f"Lateral Surface area of cube is: {lcb} units sq")
    print(f"Total Surface Area of cube is: {tcb} units sq")
    print(f"Voume of Cube is: {vc} units cb")

def cuboid(l,w,h):
    if l==w and l==h:
        print(f"Length of each edge of cube is: {h} units")
        print(f"Surface area of each face of Cube is: {h*h} units sq")
        print(f"Lateral Surface area of cube is: {4*h*h} units sq")
        print(f"Total Surface Area of cube is: {6*h*h} units sq")
        print(f"Voume of Cube is: {l*w*h} units cb")
    else:
        sa1=l*w
        sa2=w*h
        sa3=l*h
        v=l*w*h
        lv=2*h*(l+w)
        tv=(2*sa1)+(2*sa2)+(2*sa3)
        print(f"Length of cuboid is: {l} units")
        print(f"Width of cuboid is: {w} units")
        print(f"Height of cuboid is: {h} units")
        print(f"Surface area of first face (L*W) is: {sa1} units sq")
        print(f"Surface area of second face (W*H) is: {sa2} units sq")
        print(f"Surface area of third face (L*H) is: {sa3} units sq")
        print(f"Lateral Surface area of cuboid is: {lv} units sq")
        print(f"Total Surface area of cuboid is: {tv} units sq")
        print(f"Volume of Cuboid is: {v} units cb")

def cylinder(cr,ch):
    pie=22/7
    clv=pie*(cr**2)*ch
    cscl=2*pie*(cr)*(ch)
    tcl=(2*pie*cr*ch)+2*(pie*cr**2)
    e=2*pie*(cr**2)
    print(f"Radius of cylinder is: {cr} units")
    print(f"Height of cylinder is: {ch} units")
    print(f"Area of each face of cylinder is: {e} units sq")
    print(f"Curved Surface aera of cylinder is: {cscl} units sq")
    print(f"Total Surface aera of cylinder is: {tcl} units sq")
    print(f"Volume of cylinder is: {clv} units cb")

def eqtriangle(a):
    b=a**2
    h=(b-(b/4))**0.5
    A=((3**0.5)*b)/4
    p=3*a
    print(f"Length of each side of Equilateral Triangle is: {a} units")
    print(f"Height of Equilateral Triangle is: {h} units")
    print(f"Perimeter of Equilateral Triangle is: {p} units")
    print(f"Area of Equilateral Triangle is: {A} units sq")

def isotriangle(h,b):
    at=0.5*b*h
    s=(h**2+(b/2)**2)**0.5
    p=b+2*s
    print(f"Height of Isoceles Triangle is: {h} units")
    print(f"Base of Isoceles Triangle is: {b} units")
    print(f"Length of each equal sides of Isoceles Triangle is: {s} units")
    print(f"Perimeter of Isoceles Triangle is: {p} units")
    print(f"Area of Isoceles Triangle is: {at} units sq")

def rectangle(l,b):
    a=l*b
    p=2*(l+b)
    if l==b:
        print(f"Length of each side of Square is: {l} units")
        print(f"Perimeter of Square is: {4*l} units")
        print(f"Length of each diagonal of Square is: {(2**0.5)*l} units")
        print(f"Area of Square is: {l*b} units sq")
    else:
        print(f"Length of Rectangle is: {l} units")
        print(f"Breadth of Rectangle is: {b} units")
        print(f"Perimeter of Rectangle is: {p} units")
        print(f"Length of each diagonal of Rectangle is: {((l*l)+(b*b))**0.5} units")
        print(f"Area of Rectangle is: {a} units sq")

def polygon(n,l,a):
    aorp=(n*l*a)/2
    p=n*l
    print(f"Length of each side of Regular Polygon is: {l} units")
    print(f"Apothem of Regular Polygon is: {a} units")
    print(f"Number of Sides of Regular Polygon is: {n} ")
    if n==3:
        print(f"Area of  Equilateral Triangle is: {aorp} units sq")
        print(f"Perimeter of Equilateral Triangle is: {p} units")
    elif n==4:
        print(f"Area of Square is: {l*l} units sq")
        print(f"Perimeter of Square is: {p} units")
    elif n==5:
        print(f"Area of Regular Pentagon is: {aorp} units sq")
        print(f"Perimeter of Regular Pentagon is: {p} units")
    elif n==6:
        print(f"Area of Regular Hexagon is: {aorp} units sq")
        print(f"Perimeter of Regular Hexagon is: {p} units")
    elif n==7:
        print(f"Area of Regular Heptagon is: {aorp} units sq")
        print(f"Perimeter of Regular Heptagon is: {p} units")
    elif n==8:
        print(f"Area of Regular Octagon is: {aorp} units sq")
        print(f"Perimeter of Regular Octagon is: {p} units")
    elif n==9:
        print(f"Area of Regular Nonagon is: {aorp} units sq")
        print(f"Perimeter of Regular Nonagon is: {p} units")
    elif n==10:
        print(f"Area of Regular Decagon is: {aorp} units sq")
        print(f"Perimeter of Regular Decagon is: {p} units")
    elif n==11:
        print(f"Area of Regular Hendecagon is: {aorp} units sq")
        print(f"Perimeter of Regular Hendecagon is: {p} units")
    elif n==12:
        print(f"Area of Regular Dodecagon is: {aorp} units sq")
        print(f"Perimeter of Regular Dodecagon  is: {p} units")
    elif n==13:
        print(f"Area of Regular Tridecagon is: {aorp} units sq")
        print(f"Perimeter of Regular Tridecagon  is: {p} units")
    elif n==14:
        print(f"Area of Regular Tetradecagon is: {aorp} units sq")
        print(f"Perimeter of Regular Tetradecagon is: {p} units")
    elif n==15:
        print(f"Area of Regular Pentadecagon is: {aorp} units sq")
        print(f"Perimeter of Regular Pentadecagon  is: {p} units")
    elif n>15:
        print(f"Area of Regular Polygon is: {aorp} units sq")
        print(f"Perimeter of Regular Polygon is: {p} units")
    elif n<=2:
        print("Please Enter Correct Format")
        print("Your number of sides must be equal to 3 or greater then 3")
    elif n<=0:
        print("Please Enter Correct Format")
        print("Your number of sides must be equal to 3 or greater then 3")

def rtetrahedron(a):
    et=(3**0.5)*(a**2)/4
    ao1f=et
    lsat=3*et
    tsat=4*et
    htd=a*((2/3)**0.5)
    votd=(a**3)/(6*(2**0.5))
    print(f"Length of each edge of Regular Tetrahedron is: {a} units")
    print(f"Area of each face of Regular Tetrahedron is: {et} units sq")
    print(f"Lateral Surface area of Regular Tetrahedron is: {lsat} units sq")
    print(f"Total Surface area of  Regular Tetrahedron is: {tsat} units sq")
    print(f"Height of Regular Tetrahedron is: {htd} units")
    print(f"Volume of Regular Tetrahedron is: {votd} units cb")

def rhombus(ard,arb):
    if ard==arb:
        s=(2*((ard/2)**2))**0.5
        print(f"Length of each diagonal of Square is: {ard} units")
        print(f"Length of each side of Square is: {s} units")
        print(f"Perimeter of Square is: {4*s} units")
        print(f"Area of Square is: {s**2} units sq")
    else:
        arrh=(ard*arb)/2
        a=ard**2
        b=arb**2
        s=0.5*((a+b)**0.5)
        p=4*s
        print(f"Length of first diagonal of Rhombus is: {ard} units")
        print(f"Length of second diagonal of Rhombus is: {arb} units")
        print(f"Length of each side of Rhombus is: {s} units")
        print(f"Perimeter of Rhombus is: {p} units")
        print(f"Area of Rhombus is: {arrh} units sq")

def rcfrustum(fR,fr,fh):
    L=((fh**2)+(fR+fr)**2)**1/2
    lf_sq=(fh**2)+(fR-fr)**2
    lf=(lf_sq)**(0.5)
    csf=pie*(lf*(fR+fr))
    tcsf=(pie*L*(fR+fr))+(pie*(fR**2+fr**2))
    vfr=(22/7)*fh/3*((fR**2)+(fR*fr)+(fr**2))
    jx=pie*(fr**2)
    jxx=pie*(fR**2)
    print(f"Radius of bigger circle of Frustum of a Circular Right cone is: {fR} units")
    print(f"Radius of smaller circle of Frustum of a Circular Right cone is: {fr} units")
    print(f"Height of Frustum of a Circular Right cone is: {fh} units")
    print(f"Curved Surface area of Frustum of a Circular Right cone is: {csf} units sq")
    print(f"Total Surface area of Frustum of a Circular Right cone is: {tcsf} units sq")
    print(f"Surface area of top of Frustum of a Circular Right cone is: {jx} units sq")
    print(f"Surface area of bottom of Frustum of a Circular Right cone is: {jxx} units sq")
    print(f"Slant height of Frustum of a Circular Right cone is: {lf} units")
    print(f"Volume of Frustum of a Circular Right cone is: {vfr} units cb")

def rcfrustum(fR,fr,fh):
    L=((fh**2)+(fR+fr)**2)**1/2
    lf_sq=(fh**2)+(fR-fr)**2
    lf=(lf_sq)**(0.5)
    csf=pie*(lf*(fR+fr))
    tcsf=(pie*L*(fR+fr))+(pie*(fR**2+fr**2))
    vfr=(22/7)*fh/3*((fR**2)+(fR*fr)+(fr**2))
    jx=pie*(fr**2)
    jxx=pie*(fR**2)
    print(f"Radius of bigger circle of Frustum of a Circular Right cone is: {fR} units")
    print(f"Radius of smaller circle of Frustum of a Circular Right cone is: {fr} units")
    print(f"Height of Frustum of a Circular Right cone is: {fh} units")
    print(f"Curved Surface area of Frustum of a Circular Right cone is: {csf} units sq")
    print(f"Total Surface area of Frustum of a Circular Right cone is: {tcsf} units sq")
    print(f"Surface area of top of Frustum of a Circular Right cone is: {jx} units sq")
    print(f"Surface area of bottom of Frustum of a Circular Right cone is: {jxx} units sq")
    print(f"Slant height of Frustum of a Circular Right cone is: {lf} units")
    print(f"Volume of Frustum of a Circular Right cone is: {vfr} units cb")

def semicircle(r):
    pie=22/7
    a=pie*(r**2)
    b=a/2
    d=2*r
    p=d+(pie*r)
    print(f"Radius of Semicircle is: {r} units")
    print(f"Diameter of Semiircle is: {d} units")
    print(f"Perimeter of Semicircle is: {p} units")
    print(f"Area of Semicircle is: {b} units sq")

def sphere(r):
    v=(4/3)*pie*(r**3)
    s=4*pie*(r**2)
    print(f"Radius of Sphere is: {r} units")
    print(f"Diameter of Sphere is: {2*r} units")
    print(f"Volume of Sphere is: {v} units cb")
    print(f"Surface area of Sphere is: {s} units sq ")

def hemisphere(r):
    s=2*pie*(r**2)
    ts=3*pie*(r**2)
    v=(2/3)*pie*(r**3)
    b=pie*(r**2)
    print(f"Radius of Hemisphere is: {r} units")
    print(f"Diameter of Hemisphere is: {2*r} units")
    print(F"Area of base of Hemisphere is: {b} units sq")
    print(f"Curved Surface area of Hemisphere is: {s} units sq")
    print(f"Total Surface area of Hemisphere is: {ts} units sq")
    print(f"Volume of Hemisphere is: {v} units cb")

def square(s):
    x=s**2
    p=4*s
    d=s*(2**0.5)
    print(f"Side of Square is: {s} units")
    print(f"Perimeter of Square is: {p} units")
    print(f"Length of each diagona of Square is: {d} units")
    print(f"Area of Square is: {x} units sq")

def triangle(h,b):
    at=0.5*b*h
    print(f"Height of Triangle is: {h} units")
    print(f"Base of Triangle is: {b} units")
    print(f"Area of Triangle is: {at} units sq")

def nCr(n,r):
    x=factorial(n)
    y=factorial(r)
    return x/(y*factorial(n-r))

def sum_series(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

def sum_odd(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum

def sum_even(n):
    sum=0
    for i in range(2,n+1,2):
        sum=sum+i
    return sum

def table(a,x,y):
    for i in range(x,y+1):
        print(f"{a}*{i}={a*i}")

def series_square(n,m):
    for i in range(n,m+1):
        x=i**2
        print(x)

def simple_intrest(p,t,r):
    return p*(1+r*t)

def compound_intrest(P,r,t,n):
    return P*((1+(r/t))**(n*t))

def quad_eq(a,b,c):
    d=(b**2)-(4*a*c)
    a
    sol=((-1*b)+(d**0.5))/2*a
    sol_2=((-1*b)-(d**0.5))/2*a
    print(f"Your quadratic equation is {a}x^2+({b}x)+({c})=0")
    print(f"It's Discriminant is: {d} ")
    print(f"It's first root is: {sol} ")
    print(f"It's second root is: {sol_2} ")

def credits():
    print(" YASHRAJ BAILA of class 12th B")
    print("ROLL NUMBER=12227")
    print(" AYUSH THAKUR of class 12th B")
    print("ROLL NUMBER=12209")
    print(" BHUVAN THAKUR of class 12th B")
    print("ROLL NUMBER=12210")
    print(" STUDENTS OF DAV PUBLIC SCHOOL CHAMBA")
    print("BATCH : 2022-23")

def info():
    print("Pyfile use numpy,pandas,matplotlib,sympy,random and math as support libraries")

    print("numpy is imported as np,pandas is imported as pd,random imported as rn and and matplotlib.pyplot as mlt")

    print("math is imported as m, sympy is used as support library in pyfile but not whole sympy is imported. So,to access all functions of sympy user must import sympy apart from pyfile")
    
    print("perarea(base of parallelogram,height of perallelogram) is used to calulate area of parallelogram")
    
    print("traparea(length of first parallel side of trapezium,length of second parallel side of trapezium,height of trapezium) is used calculate area of trapezium")
    
    print("biodata(integer) shows the basic information of the given number, NOTE: integer can't be a float value")
    
    print("circle(radius o circle) is used to calculate all dimensions of circle")
    
    print("rccon(radius of Circular Right Cone,height of Circular Right Cone) is used to calculate all the dimensions of Circular Right Cone")
    
    print("cube(length of edfe of cube) is used to calculate all dimensions of cube")
    
    print("cuboid(length of cuboid,width of cuboid,height of cuboid) is used to calulate all dimensions of cuboid")
    
    print("cylinder(radius of cylinder,heifht of cylinder) is used to calulate all the dimensions of cylinder")
    
    print("eqtriangle(length of one side of equilateral triangle) is used to calculate all the dimensions of equilateral triangle")
    
    print("isotriangle(heigth of isoscles triangle,base of isoscles triangle) is used to calculate all the dimensions of isoscles triangle ")
    
    print("rectangle(length of rectangle,breadth of rectangle) is used to calculate all the dimensions of rectangle")

    print("polygon(number of sides,length of each side of regular polygon,apothem of regular polygon) is used to calculate all the dimensions of REGULAR polygon ,also gove the name of three sided regular polygon ot fifteen sided regular polygon")
    
    print("rtetrahedron(length of each edge of regular tetrahedron) is used to calculate all the dimensions of REGULAR tetrahedron")

    print("rhombus(length of first diagonal,length of second diagonal) is used to calculate all the dimensions od rhombus")

    print("rcfrustum(ridious of bigger circle of Frustum of a Circular Right cone,radius of smaller circle of Frustum of a Circular Right cone,height) is used to calculate all the dimensions of Frustum of a Circular Right cone")

    print("semicircle(radius) is used to find all the dimensions of semicircle")

    print("sphere(radius) is used to calculate all the dimensions of sphere ")

    print("hemisphere(radius) is used to calculate all the dimensions of hemisphere ")

    print("square(length of each side) is used to calculate all the dimension of square")

    print("triangle(height,base) is used to calculate area of any kind of triangle")

    print("factorial(whole number) as it is cleared from it's name it is used to calculate the factorial of a whole number")

    print("nCr(n,r) is used to calculate n choose r")

    print("sum_series(whole number) is used to claculate the sum of all the whole number up to given whole number")

    print("sum_even(whole number) is used to calculate the sum of all the even whole number up to given whole number")

    print("sum_odd(whole number) is used to calculate the sum of all the odd whole number up to given whole number")
    
    print("series_square(starting value,endind value) is use to calculate all square of all the integers between starting and ending value including them too NOTE:starting and ending value are integers ")

    print("table(integer,starting value,ending value) shows the mathematical table of ginven integer from starting value up to ending value including them too NOTE:starting and ending value are integers ")

    print("simple_intrest(initial principal balance,time period in years,annual intrest rate) is used to calculate final amount")

    print("compound_intrest(initial principle balance,intrest rate,numberof time period elapsed,number of time intrest applied per time period) is used to caluclate final amount")

    print("quad_eq(coefficient of x^2,coefficient of x,constant) is used to calculate the root and discriminant of quadratic equation")

    print("symbol('symbol') is used to give a variable with respect to user wants to differentiate or integrate a function, without it user can't use diff an intg function")

    print("diff(fx,symbol) is used to differentiate the given function fx with respect to given symbol/variable")

    print("intg(fx,symbol) is used to integrate(indefinate) the given function fx with respect to given symbol/variable")

    print("intg(fx,(symbol,lower limit,upper limit)) is used to integrate(definate) the given function fx with respect to given symbol/variable")
    
    




    





    

biodata(0)
print("done1")
biodata(4)
print("done2")
biodata(-4)
print("done3")
biodata(12345)
print("last")
biodata(-12345)


