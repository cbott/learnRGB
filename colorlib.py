# colorlib.py
# define helper functions for use in numberlearn and colorlearn
def to_hex(rgb):
    """Change an (r, g, b) tuple to a tkinter-compatible hex string"""
    return '#%02x%02x%02x' % rgb

def clamp_rgb(num):
    """Limit inputs to between 0 and 255"""
    return int(max(0, min(num, 255)))

def color_score(actual_rgb, guess_rgb):
    """ 
        compute a score as the sum of differences between the actual rgb and input rgb
        squared, then scaled to a 0-100 range
    """
    actual_rgb = tuple(actual_rgb)
    guess_rgb = tuple(guess_rgb)

    diffsum = abs(actual_rgb[0] - guess_rgb[0]) + \
              abs(actual_rgb[1] - guess_rgb[1]) + \
              abs(actual_rgb[2] - guess_rgb[2])

    return int(((765 - diffsum)/765.0)**2 * 100)
