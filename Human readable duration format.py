def format_duration(seconds):
    if seconds == 0:
        return 'now'

    s = seconds % 60
    m = seconds % 3600 // 60
    h = seconds % 86400 // 3600
    d = seconds % 31536000 // 86400
    y = seconds // 31536000

    A = [y, d, h, m, s]
    b = ['year', 'day', 'hour', 'minute', 'second']
    out = []

    for x, y in zip(A, b):
        if x == 1:
            out.append(f'{x} {y}')
        elif x > 1:
            out.append(f'{x} {y}s')

    if len(out) > 1:
        return ', '.join(out[:-1]) + ' and ' + out[-1]
    return ''.join(out)

print(format_duration(3662))