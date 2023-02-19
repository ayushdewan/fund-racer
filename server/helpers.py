from random import randrange

def stream_url(name):
    return f"https://viewer.millicast.com?streamId=Kb4XjT/{name}"

def generate_label(size=6):
    offsets = [randrange(0, 26) for _ in range(size)]
    chars = [chr(i + ord('a')) for i in offsets]
    return ''.join(chars)
