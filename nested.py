x = 2500

def scoper():
    x = 500
    return x

print x
print scoper()

# x is the global scope, so x is 2500 globally, ie: outside the scoper() function.
# within the context of scoper(), x is 500

# LEGB rule!

# x is local here.
f = lambda x:x ** 2


# nested functions
name = 'this is a global name'
print name
def greet():
    # enclosing function
    name = 'Sammy'

    def hello():
        print 'Hello ' + name

    hello()

greet()

# this is a global name
# Hello Sammy


x = 555
def func(x):
    print 'x is', x
    # ------ within this local scope x is 2
    x = 2
    print 'changed local x to ', x
    # ------ within this local scope x is 2

func(x)
print 'x is still ', x

# x is 555
# changed local x to  2
# x is still  555



z = 777
def funcTwo():
    global z
    print 'this function is now using the global z'
    print 'because the global z is: ', z
    z = 2
    print 'ran funcTwo(), changed global z to ', z

print 'before calling funcTwo(), z is: ', z
funcTwo()
print 'value of z (outside of funcTwo()) is: ', z

# before calling funcTwo(), z is:  777
# this function is now using the global z
# because the global z is:  777
# ran funcTwo(), changed global z to  2
# value of z (outside of funcTwo()) is:  2
