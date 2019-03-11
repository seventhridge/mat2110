import os



def clean_line(line_in):
    if len(line_in) < 1:
        return None
    if not 'USGS' in line_in:
        return None


