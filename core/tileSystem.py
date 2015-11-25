import math


class TileSystem:

    EARTH_RADIUS = 6378137
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    # latitude - y
    # longitude - x
    # geo coordinates (lat, long)

    @staticmethod
    def clip(n, min_value, max_value): return min(max(n, min_value), max_value)

    @staticmethod
    def map_size(zoom): return 256 << zoom

    @classmethod
    def ground_resolution(cls, latitude, zoom):
       latitude = cls.clip(latitude, cls.MIN_LATITUDE, cls.MAX_LATITUDE)
       return math.cos(latitude * math.pi / 180) * 2 * math.pi * cls.EARTH_RADIUS / cls.map_size(zoom)

    @classmethod
    def map_scale(cls, latitude, zoom, screen_dpi=96):
        return cls.ground_resolution(latitude, zoom) * screen_dpi / 0.0254

    @classmethod
    def latitude_to_pixel_y(cls, latitude, zoom):
        latitude = cls.clip(latitude, cls.MIN_LATITUDE, cls.MAX_LATITUDE)
        sin_latitude = math.sin(latitude * math.pi / 180)
        y = 0.5 - math.log((1 + sin_latitude) / (1 - sin_latitude)) / (4 * math.pi)
        map_size = cls.map_size(zoom)
        pixel_y = int(cls.clip(y * map_size + 0.5, 0, map_size - 1))
        return pixel_y

    @classmethod
    def longitude_to_pixel_x(cls, longitude, zoom):
        longitude = cls.clip(longitude, cls.MIN_LONGITUDE, cls.MAX_LONGITUDE)
        x = (longitude + 180) / 360
        map_size = cls.map_size(zoom)
        pixel_x = int(cls.clip(x * map_size + 0.5, 0, map_size - 1))
        return pixel_x

    @classmethod
    def pixel_y_to_latitude(cls, pixel_y, zoom):
        map_size = cls.map_size(zoom)
        y = 0.5 - (cls.clip(pixel_y, 0, map_size - 1) / map_size)
        latitude = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
        return latitude

    @classmethod
    def pixel_x_to_longitude(cls, pixel_x, zoom):
        map_size = cls.map_size(zoom)
        x = (cls.clip(pixel_x, 0, map_size - 1) / map_size) - 0.5
        longitude = 360 * x
        return longitude

    @staticmethod
    def pixel_y_to_tile_y(pixel_y): return pixel_y / 256

    @staticmethod
    def pixel_x_to_tile_x(pixel_x): return pixel_x / 256

    @staticmethod
    def tile_y_to_pixel_y(tile_y): return tile_y * 256

    @staticmethod
    def tile_x_to_pixel_x(tile_x): return tile_x * 256

    @staticmethod
    def quadkey_4_to_dec(quadkey): return int(quadkey, base=4)

    @staticmethod
    def tile_xy_to_quadkey(tile_x, tile_y, zoom):
        """
        :param tile_x:
        :param tile_y:
        :param zoom:
        :return: string quadkey
        """
        if zoom == 0:
            return '0'

        quadkey = ''
        for i in range(zoom, 0, -1):
            digit = 0
            mask = 1 << (i - 1)
            if(int(tile_x) & mask) != 0:
                digit += 1
            if(int(tile_y) & mask) != 0:
                digit += 1
                digit += 1
            quadkey += str(digit)
        return quadkey

    @classmethod
    def lat_long_to_quadkey(cls, lat, long, zoom):
        pixel_x = cls.longitude_to_pixel_x(long, zoom)
        pixel_y = cls.latitude_to_pixel_y(lat, zoom)
        tile_x = cls.pixel_x_to_tile_x(pixel_x)
        tile_y = cls.pixel_y_to_tile_y(pixel_y)
        return cls.tile_xy_to_quadkey(tile_x, tile_y, zoom)

    @classmethod
    def lat_long_to_quadkey_dec(cls, lat, long, zoom):
        return cls.quadkey_4_to_dec(cls.lat_long_to_quadkey(lat, long, zoom))

    @classmethod
    def pixel_xy_to_quadkey(cls, pixel_x, pixel_y, zoom):
        tile_x = cls.pixel_x_to_tile_x(pixel_x)
        tile_y = cls.pixel_y_to_tile_y(pixel_y)
        return cls.tile_xy_to_quadkey(tile_x, tile_y, zoom)

    @classmethod
    def pixel_xy_to_quadkey_dec(cls, pixel_x, pixel_y, zoom):
        return cls.quadkey_4_to_dec(cls.pixel_xy_to_quadkey(pixel_x, pixel_y, zoom))

    @classmethod
    def tile_xy_to_quadkey_dec(cls, tile_x, tile_y, zoom):
        return cls.quadkey_4_to_dec(cls.tile_xy_to_quadkey(tile_x, tile_y, zoom))

    #todo: refactor if-else by dict
    @classmethod
    def quadkey_to_tile_xy(cls, quadkey, tile_x, tile_y, zoom):
        tile_x = tile_y = 0
        zoom = len(quadkey)
        for i in range(zoom, 0, -1):
            mask = 1 << (i - 1)
            if quadkey[zoom - i] == '0':
                continue
            elif quadkey[zoom - i] == '1':
                tile_x |= mask
                continue
            elif quadkey[zoom - i] == '2':
                tile_y |= mask
                continue
            elif quadkey[zoom - i] == '3':
                tile_x |= mask
                tile_y |= mask
                continue
        return tile_x, tile_y