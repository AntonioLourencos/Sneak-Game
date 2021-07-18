class Convert:
    def hex_rgb(color: str):
        color.replace('#', "")
        r_hex = color[1:3]
        g_hex = color[3:5]
        b_hex = color[5:7]
        return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
