import re

def sanitise(filename):
    filename = filename.encode('ascii', 'ignore').decode('ascii')
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.strip().replace('  ', ' ')
    filename = filename.strip(" .")
    reserved_names = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"}
    if not filename or filename.upper() in reserved_names:
        filename = "filename"
    return filename