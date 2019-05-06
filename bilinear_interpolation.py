# Author: Jonathan Falwell
# Date: 05/06/2019
# Reference Documentation: https://en.wikipedia.org/wiki/Bilinear_interpolation            
# Explanation:
"""Bilinear Interpolation takes into account 4 points, with known "height" value, to approximate a 5th point's "height" value. The 5th point must be contained within the bounds formed by the 4 known points. Bilinear interpolation is done by performing linear interpolation in the x direction for the two point pairs, and then performing linear interpolation in the y direction for the values found from the first interpolation. The order of interpolation does not matter. i.e you can interpolate the y direction first, and then the x, or vice versa.""" 

# Bilinear Interpolation
def bilinear_interpolation(x1,x,x2,y1,y,y2,Q11,Q21,Q12,Q22):
  a = 1/(x2-x1)/(y2-y1)
  Qxy = a * (Q11*(x2-x)*(y2-y) + Q21*(x-x1)*(y2-y) + Q12*(x2-x)*(y-y1) + Q22*(x-x1)*(y-y1))
  return Qxy

# input names generalized to avoid confusion with bilinear method. ie can be used in the x or y
def linear_interpolation(n1,n,n2,Q1,Q2):
  return (n2-n)/(n2-n1)*Q1 + (n-n1)/(n2-n1)*Q2

if __name__ == '__main__':
  # input values taken from wiki example
  x1 = 14
  x2 = 15
  y1 = 20
  y2 = 21
  x = 14.5
  y = 20.2
  Q11 = 91
  Q21 = 210
  Q12 = 162
  Q22 = 95

  # bilinear interpolation all at once
  z = bilinear_interpolation(x1,x,x2,y1,y,y2,Q11,Q21,Q12,Q22)
  
  print("bilinear interpolation: {}".format(z))
  
  # x direction interpolation
  z1 = linear_interpolation(x1,x,x2,Q11,Q21)
  z2 = linear_interpolation(x1,x,x2,Q12,Q22)
  # y direction interpolation from x results
  z = linear_interpolation(y1,y,y2,z1,z2)

  print("bilinear interpolation of x then y result: {}".format(z))

  # y direction interpolation
  z1 = linear_interpolation(y1,y,y2,Q11,Q12)
  z2 = linear_interpolation(y1,y,y2,Q21,Q22)
  # x direction interpolation from y results
  z = linear_interpolation(x1,x,x2,z1,z2)

  print("bilinear interpolation of y then x result: {}".format(z))
