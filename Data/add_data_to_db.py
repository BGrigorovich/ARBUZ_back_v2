from core.tileSystem import TileSystem
import random
import sqlite3

conn = sqlite3.connect('/media/global/HKSC/project/ARBUZ_back/db.sqlite3')
# 50.44187321507419 30.39968490600586 lat - y, long - x
# 50.3785320606136 30.62061309814453
# 13
x1 = 50.44187321507419
y1 = 40.39968490600586

# x2 = 70.3785320606136
# y2 = 70.62061309814453
x = -79.377807617187500
y = 43.653785705566406
z = 23

# lat = random.uniform(x1, x2)
# long = random.uniform(y1, y2)
print(TileSystem.lat_long_to_quadkey(y, x, z))

pY = TileSystem.latitude_to_pixel_y(y, z)
pX = TileSystem.longitude_to_pixel_x(x, z)
print(pY, pX)
tY = TileSystem.pixel_y_to_tile_y(pY)
tX = TileSystem.pixel_x_to_tile_x(pX)
print(tY, tX)
aa = TileSystem.tile_xy_to_quadkey(pX, pY, z)
# print(aa)
print(TileSystem.quadkey_to_tile_xy(aa , tX, tY, z))
# tileX = 3
# tileY = 5
# z1 = 3
#
# print(TileSystem.tile_xy_to_quadkey(tileX, tileY, z1))
# pixel_x = TileSystem.pixel_y_to_latitude()
# TileSystem.quadkey_to_tile_xy(quadkey=)
# print(type(TileSystem.lat_long_to_quadkey(x1, y1, z)))
#
# print(TileSystem.lat_long_to_quadkey_dec(x1, y1, z))
# print(type(TileSystem.lat_long_to_quadkey_dec(x1, y1, z)))
# lat1 = random.uniform(x1, x2)
# long1 = random.uniform(y1, y2)
# print(TileSystem.lat_long_to_quadkey_dec(lat1, long1, z))
row_data = []
for i in range(0, 3):
    lat = random.uniform(x1, x2)
    long = random.uniform(y1, y2)
    print(TileSystem.lat_long_to_quadkey(lat, long, z))
    row_data.append(('street '+[i+1], random.randint(1,100), lat, long))