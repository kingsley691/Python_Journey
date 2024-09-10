# Chap2 - Variables
# Handling the precision of floating-point numbers
# S. Trowbridge/J. Sun

#PI = 3.14159265359
PI = 3.14

# use % operator
print('%.1f' % PI)
print('%.2f' % PI)
print('%.3f' % PI)
print()

# use format() method to format a specified value
print( "{:.6f} {:.2f} {:.3f}".format(0.123456789, 711, PI) )
print()

# f-string print with various levels of floating point precision
print(f"{PI:.1f}")
print(f"{PI:.2f}")
print(f"{PI:.3f}")
print(f"{PI:.4f}")
print(f"{PI:.5f}")
print()

# use round() for floating point precision
print(PI)
print(round(PI, 3))
print(round(PI))
print()
