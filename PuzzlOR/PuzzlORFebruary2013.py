import itertools

for value in itertools.permutations([1,2,3,4,5,6,7,8,9]):
    a,b,c,d,e,f,g,h,i=value
    if (2*a == b + 2*c) and (2*d + e == f) and (2*g + h == 3*i) and (3*(a+b+c) == 2*(d+e+f) + 3*(g+h+i)):
        print(value)
