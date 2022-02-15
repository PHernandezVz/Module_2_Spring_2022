geek_points = 1
portals = 2.0

# uses string modulo operator
print("Geeks: %2d, Portal: %5.2f" % (1, 05.33))

# uses string modulo operator
print("Geeks: %2d, Portal: %5.2f" % (geek_points, portals))

# f-string formatting
print(f'Geeks: {geek_points}, Portals: {portals}')

# f-string formatting
print(f'Geeks: {geek_points}, Portals: {portals: 5.2f}')

# string format() method
print('Geeks: {}, Portals: {}'.format(geek_points, portals))

# string format() method
print('Geeks: {}, Portals: {:5.2f}'.format(geek_points, portals))
