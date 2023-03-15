def rot13(message):
    def crypt(c):
        if 65 <= ord(c) <= 90:
            if ord(c) + 13 > 90:
                return chr(ord(c)+13-26)
            else:
                return chr(ord(c) + 13)
        if 97 <= ord(c) <= 122:
            if ord(c) + 13 > 122:
                return chr(ord(c)+13-26)
            else:
                return chr(ord(c) + 13)
        return c

    res = ''
    for x in message:
        res += crypt(x)
    return res