import palettable
from palettable.cubehelix import Cubehelix
from palettable import cubehelix

# cubehelix_palette = Cubehelix.make(start=0.3, rotation=-0.5, n=16)
# print(cubehelix_palette)


# print(cubehelix.print_maps())
# print(cubehelix.get_map('cubehelix1_16'))
# print(cubehelix.get_map('cubehelix1_16').__dict__)

my_cube = cubehelix.Cubehelix.make(gamma=1.0, start=2.0, rotation=1.0, sat=1.5, n=16)

print(my_cube.colors)
