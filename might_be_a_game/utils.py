import constants as c

def limit_trait(value):
    value = max(value, c.trait_val_lower_limit)
    value = min(value, c.trait_val_upper_limit)
    return value

def limit_map(pos_x, pos_y):
    pos_x = max(0, pos_x)
    pos_y = max(0, pos_y)

    pos_x = min(c.map_x-1, pos_x)
    pos_y = min(c.map_y-1, pos_y)

    return pos_x,pos_y