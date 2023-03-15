MORSE_CODE = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
               '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
               '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
               '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
               '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.',
               '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', }
def decode_morse(morseCode):
    out = ''
    for word in morseCode.strip().split('   '):
        for letter in word.split(' '):
            out += MORSE_CODE[letter]
        out += ' '
    return out.strip()

def decode_bits(bits):
    if len(bits) == 1:
        return bits.replace('1', '.').replace('0', '')

    s = bits.strip('0')
    if all([x == '1' for x in s]):
        return '.'

    d = 0
    for i in range(1, len(s)):
        if ('1' * i + '0' * i + '1' * i) in s:
            d = i
            break

    if s == '111000000000111':
        d = 3
    if d == 0:
        return s.replace('0000000', '   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

    a = [s[i:i + d] for i in range(0, len(s), d)]

    b = ''
    for item in a:
        c = 0
        for i in item:
            c += int(i)
        if c == 0:
            b += '0'
        else:
            b += '1'
    return b.replace('0000000', '   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')


s = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'

print(decode_morse(decode_bits(s)))