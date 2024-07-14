# https://www.codewars.com/kata/5886e082a836a691340000c3/train/python
import matplotlib.pyplot as plt
a = 30
b = 2
sq8 = 8**0.5
sq2 = 2**0.5
x = (a-b)/sq8
y = x + 2 * b/8**0.5

rectangle = [(x, y),(y, x),(-x,-y),(-y, -x)]

#print(rectangle)

int(a/sq2)
q = 2**0.5
da = int(a / q + 1) 
db = int(b / q + 1) 
zb = b / q
za = a / q
if int(za) % 2:
    za1, za2 = -1, 0
else:
    za1, za2 = 0 , -1
    
if int(zb) % 2:
    zb1, zb2 = -1, 0
else:
    zb1, zb2 = 0 , -1


print(f'{da=} {db=} {za=} {zb=}')

print( (da + zb1) * (db +za1) + ((da+zb2)*(db + za2) ) )


plt.plot(*zip(*(rectangle+rectangle[:1])))
plt.plot( [-a, a], [0,0] )
plt.plot( [0,0], [-a, a] )

plt.axis([-a, a, -a, a])
plt.xticks(range(-a,a+1))
plt.yticks(range(-a,a+1))
plt.grid( )
plt.gca().set_aspect("equal")
plt.show()

'''
a = 8  b = 6 
da=6 db=5 za=5.65685424949238 zb=4.242640687119285
6*4  + 5*5 = 49 

a = 6 b = 4
da=5 db=3 za=4.242640687119285 zb=2.82842712474619
5*3  + 4*2 = 23

rectangle = []
for x in range(-a,a+1):
    y = x + 2 * b/8**0.5
    rectangle.append((x,y))

plt.plot(*zip(*(rectangle+rectangle[:1])))

rectangle = []
for x in range(-a,a+1):
    y = -x + 2 * a/8**0.5
    rectangle.append((x,y))

plt.plot(*zip(*(rectangle+rectangle[:1])))
'''
'''
x + 2 * b/8**0.5 = -x + 2 * a/8**0.5
2x = 2 * a/8**0.5 - 2 * b/8**0.5
x = a/8**0.5 - b/8**0.5
'''