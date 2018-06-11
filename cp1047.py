""" Python Character Mapping Codec cp1047 generated from 'cp\cp1047.txt' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_table)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_table)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='cp1047',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Table

decoding_table = (
    u'\x00'     #  0x00 -> NULL
    u'\x01'     #  0x01 -> START OF HEADING
    u'\x02'     #  0x02 -> START OF TEXT
    u'\x03'     #  0x03 -> END OF TEXT
    u'\xdc'     #  0x04 -> LATIN CAPITAL LETTER U WITH DIAERESIS
    u'\t'       #  0x05 -> HORIZONTAL TABULATION
    u'\xc3'     #  0x06 -> LATIN CAPITAL LETTER A WITH TILDE
    u'\x1c'     #  0x07 -> FILE SEPARATOR
    u'\xca'     #  0x08 -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    u'\xb2'     #  0x09 -> SUPERSCRIPT TWO
    u'\xd5'     #  0x0A -> LATIN CAPITAL LETTER O WITH TILDE
    u'\x0b'     #  0x0B -> VERTICAL TABULATION
    u'\x0c'     #  0x0C -> FORM FEED
    u'\r'       #  0x0D -> CARRIAGE RETURN (CR)
    u'\x0e'     #  0x0E -> SHIFT OUT
    u'\x0f'     #  0x0F -> SHIFT IN
    u'\x10'     #  0x10 -> DATA LINK ESCAPE
    u'\x11'     #  0x11 -> DEVICE CONTROL ONE
    u'\x12'     #  0x12 -> DEVICE CONTROL TWO
    u'\x13'     #  0x13 -> DEVICE CONTROL THREE
    u'\xdb'     #  0x14 -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    u'\n'       #  0x15 -> LINE FEED (LF)
    u'\x08'     #  0x16 -> BACKSPACE
    u'\xc1'     #  0x17 -> LATIN CAPITAL LETTER A WITH ACUTE
    u'\x18'     #  0x18 -> CANCEL
    u'\x19'     #  0x19 -> END OF MEDIUM
    u'\xc8'     #  0x1A -> LATIN CAPITAL LETTER E WITH GRAVE
    u'\xf2'     #  0x1B -> LATIN SMALL LETTER O WITH GRAVE
    u'\x1a'     #  0x1C -> SUBSTITUTE
    u'\x1d'     #  0x1D -> GROUP SEPARATOR
    u'\x1e'     #  0x1E -> RECORD SEPARATOR
    u'\x1f'     #  0x1F -> UNIT SEPARATOR
    u'\xc4'     #  0x20 -> LATIN CAPITAL LETTER A WITH DIAERESIS
    u'\xb3'     #  0x21 -> SUPERSCRIPT THREE
    u'\xc0'     #  0x22 -> LATIN CAPITAL LETTER A WITH GRAVE
    u'\xd9'     #  0x23 -> LATIN CAPITAL LETTER U WITH GRAVE
    u'\xbf'     #  0x24 -> INVERTED QUESTION MARK
    u'\n'       #  0x25 -> NEXT LINE (NEL) WHY NOT 0XDA?
    u'\x17'     #  0x26 -> END OF TRANSMISSION BLOCK
    u'\x1b'     #  0x27 -> ESCAPE
    u'\xb4'     #  0x28 -> ACUTE ACCENT
    u'\xc2'     #  0x29 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    u'\xc5'     #  0x2A -> LATIN CAPITAL LETTER A WITH RING ABOVE
    u'\xb0'     #  0x2B -> DEGREE SIGN
    u'\xb1'     #  0x2C -> PLUS-MINUS SIGN
    u'\x05'     #  0x2D -> ENQUIRY
    u'\x06'     #  0x2E -> ACKNOWLEDGE
    u'\x07'     #  0x2F -> BELL
    u'\xcd'     #  0x30 -> LATIN CAPITAL LETTER I WITH ACUTE
    u'\xba'     #  0x31 -> MASCULINE ORDINAL INDICATOR
    u'\x16'     #  0x32 -> SYNCHRONOUS IDLE
    u'\xbc'     #  0x33 -> VULGAR FRACTION ONE QUARTER
    u'\xbb'     #  0x34 -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xc9'     #  0x35 -> LATIN CAPITAL LETTER E WITH ACUTE
    u'\xcc'     #  0x36 -> LATIN CAPITAL LETTER I WITH GRAVE
    u'\x04'     #  0x37 -> END OF TRANSMISSION
    u'\xb9'     #  0x38 -> SUPERSCRIPT ONE
    u'\xcb'     #  0x39 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    u'\xce'     #  0x3A -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    u'\xdf'     #  0x3B -> LATIN SMALL LETTER SHARP S (GERMAN)
    u'\x14'     #  0x3C -> DEVICE CONTROL FOUR
    u'\x15'     #  0x3D -> NEGATIVE ACKNOWLEDGE
    u'\xfe'     #  0x3E -> LATIN SMALL LETTER THORN (ICELANDIC)
    u'\x7f'     #  0x3F -> DELETE
    u' '        #  0x40 -> SPACE
    u'\xff'     #  0x41 -> LATIN SMALL LETTER Y WITH DIAERESIS
    u'\x83'     #  0x42 -> CONTROL
    u'\x84'     #  0x43 -> CONTROL
    u'\x85'     #  0x44 -> CONTROL
    u'\xa0'     #  0x45 -> NO-BREAK SPACE
    u'\xc6'     #  0x46 -> LATIN CAPITAL LIGATURE AE
    u'\x86'     #  0x47 -> CONTROL
    u'\x87'     #  0x48 -> CONTROL
    u'\xa4'     #  0x49 -> CURRENCY SIGN
    u'\xbd'     #  0x4A -> VULGAR FRACTION ONE HALF
    u'.'        #  0x4B -> FULL STOP
    u'<'        #  0x4C -> LESS-THAN SIGN
    u'('        #  0x4D -> LEFT PARENTHESIS
    u'+'        #  0x4E -> PLUS SIGN
    u'|'        #  0x4F -> VERTICAL LINE
    u'&'        #  0x50 -> AMPERSAND
    u'\x82'     #  0x51 -> CONTROL
    u'\x88'     #  0x52 -> CONTROL
    u'\x89'     #  0x53 -> CONTROL
    u'\x8a'     #  0x54 -> CONTROL
    u'\xa1'     #  0x55 -> INVERTED EXCLAMATION MARK
    u'\x8c'     #  0x56 -> CONTROL
    u'\x8b'     #  0x57 -> CONTROL
    u'\x8d'     #  0x58 -> CONTROL
    u'\xe1'     #  0x59 -> LATIN SMALL LETTER A WITH ACUTE
    u'!'        #  0x5A -> EXCLAMATION MARK
    u'$'        #  0x5B -> DOLLAR SIGN
    u'*'        #  0x5C -> ASTERISK
    u')'        #  0x5D -> RIGHT PARENTHESIS
    u';'        #  0x5E -> SEMICOLON
    u'^'        #  0x5F -> CIRCUMFLEX ACCENT
    u'-'        #  0x60 -> HYPHEN-MINUS
    u'/'        #  0x61 -> SOLIDUS
    u'\xb6'     #  0x62 -> PILCROW SIGN
    u'\x8e'     #  0x63 -> CONTROL
    u'\xb7'     #  0x64 -> MIDDLE DOT
    u'\xb5'     #  0x65 -> MICRO SIGN
    u'\xc7'     #  0x66 -> LATIN CAPITAL LETTER C WITH CEDILLA
    u'\x8f'     #  0x67 -> CONTROL
    u'\x80'     #  0x68 -> CONTROL
    u'\xa5'     #  0x69 -> YEN SIGN
    u'\xdd'     #  0x6A -> LATIN CAPITAL LETTER Y WITH ACUTE
    u','        #  0x6B -> COMMA
    u'%'        #  0x6C -> PERCENT SIGN
    u'_'        #  0x6D -> LOW LINE
    u'>'        #  0x6E -> GREATER-THAN SIGN
    u'?'        #  0x6F -> QUESTION MARK
    u'\x9b'     #  0x70 -> CONTROL
    u'\x90'     #  0x71 -> CONTROL
    u'\xd2'     #  0x72 -> LATIN CAPITAL LETTER O WITH GRAVE
    u'\xd3'     #  0x73 -> LATIN CAPITAL LETTER O WITH ACUTE
    u'\xd4'     #  0x74 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    u'\xd6'     #  0x75 -> LATIN CAPITAL LETTER O WITH DIAERESIS
    u'\xd7'     #  0x76 -> MULTIPLICATION SIGN
    u'\xd8'     #  0x77 -> LATIN CAPITAL LETTER O WITH STROKE
    u'\xde'     #  0x78 -> LATIN CAPITAL LETTER THORN (ICELANDIC)
    u'`'        #  0x79 -> GRAVE ACCENT
    u':'        #  0x7A -> COLON
    u'#'        #  0x7B -> NUMBER SIGN
    u'@'        #  0x7C -> COMMERCIAL AT
    u"'"        #  0x7D -> APOSTROPHE
    u'='        #  0x7E -> EQUALS SIGN
    u'"'        #  0x7F -> QUOTATION MARK
    u'\x9d'     #  0x80 -> CONTROL
    u'a'        #  0x81 -> LATIN SMALL LETTER A
    u'b'        #  0x82 -> LATIN SMALL LETTER B
    u'c'        #  0x83 -> LATIN SMALL LETTER C
    u'd'        #  0x84 -> LATIN SMALL LETTER D
    u'e'        #  0x85 -> LATIN SMALL LETTER E
    u'f'        #  0x86 -> LATIN SMALL LETTER F
    u'g'        #  0x87 -> LATIN SMALL LETTER G
    u'h'        #  0x88 -> LATIN SMALL LETTER H
    u'i'        #  0x89 -> LATIN SMALL LETTER I
    u'\xae'     #  0x8A -> REGISTERED SIGN
    u'\xaf'     #  0x8B -> MACRON
    u'\xd0'     #  0x8C -> LATIN CAPITAL LETTER ETH (ICELANDIC)
    u'\xec'     #  0x8D -> LATIN SMALL LETTER I WITH GRAVE
    u'\xe7'     #  0x8E -> LATIN SMALL LETTER C WITH CEDILLA
    u'\xf1'     #  0x8F -> LATIN SMALL LETTER N WITH TILDE
    u'\xf8'     #  0x90 -> LATIN SMALL LETTER O WITH STROKE
    u'j'        #  0x91 -> LATIN SMALL LETTER J
    u'k'        #  0x92 -> LATIN SMALL LETTER K
    u'l'        #  0x93 -> LATIN SMALL LETTER L
    u'm'        #  0x94 -> LATIN SMALL LETTER M
    u'n'        #  0x95 -> LATIN SMALL LETTER N
    u'o'        #  0x96 -> LATIN SMALL LETTER O
    u'p'        #  0x97 -> LATIN SMALL LETTER P
    u'q'        #  0x98 -> LATIN SMALL LETTER Q
    u'r'        #  0x99 -> LATIN SMALL LETTER R
    u'\xa6'     #  0x9A -> BROKEN BAR
    u'\xa7'     #  0x9B -> SECTION SIGN
    u'\x91'     #  0x9C -> CONTROL
    u'\xf7'     #  0x9D -> DIVISION SIGN
    u'\x92'     #  0x9E -> CONTROL
    u'\xcf'     #  0x9F -> LATIN CAPITAL LETTER I WITH DIAERESIS
    u'\xe6'     #  0xA0 -> LATIN SMALL LIGATURE AE
    u'~'        #  0xA1 -> TILDE
    u's'        #  0xA2 -> LATIN SMALL LETTER S
    u't'        #  0xA3 -> LATIN SMALL LETTER T
    u'u'        #  0xA4 -> LATIN SMALL LETTER U
    u'v'        #  0xA5 -> LATIN SMALL LETTER V
    u'w'        #  0xA6 -> LATIN SMALL LETTER W
    u'x'        #  0xA7 -> LATIN SMALL LETTER X
    u'y'        #  0xA8 -> LATIN SMALL LETTER Y
    u'z'        #  0xA9 -> LATIN SMALL LETTER Z
    u'\xad'     #  0xAA -> SOFT HYPHEN
    u'\xa8'     #  0xAB -> DIAERESIS
    u'\xd1'     #  0xAC -> LATIN CAPITAL LETTER N WITH TILDE
    u'['        #  0xAD -> LEFT SQUARE BRACKET
    u'\xe8'     #  0xAE -> LATIN SMALL LETTER E WITH GRAVE
    u'\xa9'     #  0xAF -> COPYRIGHT SIGN
    u'\xaa'     #  0xB0 -> FEMININE ORDINAL INDICATOR
    u'\x9c'     #  0xB1 -> CONTROL
    u'\xbe'     #  0xB2 -> VULGAR FRACTION THREE QUARTERS
    u'\xfa'     #  0xB3 -> LATIN SMALL LETTER U WITH ACUTE
    u'\xb8'     #  0xB4 -> CEDILLA
    u'\xf5'     #  0xB5 -> LATIN SMALL LETTER O WITH TILDE
    u'\xf4'     #  0xB6 -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    u'\xac'     #  0xB7 -> NOT SIGN
    u'\xab'     #  0xB8 -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xf3'     #  0xB9 -> LATIN SMALL LETTER O WITH ACUTE
    u'\xed'     #  0xBA -> LATIN SMALL LETTER I WITH ACUTE
    u'\xf9'     #  0xBB -> LATIN SMALL LETTER U WITH GRAVE
    u'\xee'     #  0xBC -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    u']'        #  0xBD -> RIGHT SQUARE BRACKET
    u'\xef'     #  0xBE -> LATIN SMALL LETTER I WITH DIAERESIS
    u'\x9e'     #  0xBF -> CONTROL
    u'{'        #  0xC0 -> LEFT CURLY BRACKET
    u'A'        #  0xC1 -> LATIN CAPITAL LETTER A
    u'B'        #  0xC2 -> LATIN CAPITAL LETTER B
    u'C'        #  0xC3 -> LATIN CAPITAL LETTER C
    u'D'        #  0xC4 -> LATIN CAPITAL LETTER D
    u'E'        #  0xC5 -> LATIN CAPITAL LETTER E
    u'F'        #  0xC6 -> LATIN CAPITAL LETTER F
    u'G'        #  0xC7 -> LATIN CAPITAL LETTER G
    u'H'        #  0xC8 -> LATIN CAPITAL LETTER H
    u'I'        #  0xC9 -> LATIN CAPITAL LETTER I
    u'\xf0'     #  0xCA -> LATIN SMALL LETTER ETH (ICELANDIC)
    u'\x93'     #  0xCB -> CONTROL
    u'\x94'     #  0xCC -> CONTROL
    u'\x95'     #  0xCD -> CONTROL
    u'\xa2'     #  0xCE -> CENT SIGN
    u'\xe4'     #  0xCF -> LATIN SMALL LETTER A WITH DIAERESIS
    u'}'        #  0xD0 -> RIGHT CURLY BRACKET
    u'J'        #  0xD1 -> LATIN CAPITAL LETTER J
    u'K'        #  0xD2 -> LATIN CAPITAL LETTER K
    u'L'        #  0xD3 -> LATIN CAPITAL LETTER L
    u'M'        #  0xD4 -> LATIN CAPITAL LETTER M
    u'N'        #  0xD5 -> LATIN CAPITAL LETTER N
    u'O'        #  0xD6 -> LATIN CAPITAL LETTER O
    u'P'        #  0xD7 -> LATIN CAPITAL LETTER P
    u'Q'        #  0xD8 -> LATIN CAPITAL LETTER Q
    u'R'        #  0xD9 -> LATIN CAPITAL LETTER R
    u'\xfb'     #  0xDA -> LATIN SMALL LETTER U WITH CIRCUMFLEX
    u'\x96'     #  0xDB -> CONTROL
    u'\x81'     #  0xDC -> CONTROL
    u'\x97'     #  0xDD -> CONTROL
    u'\xa3'     #  0xDE -> POUND SIGN
    u'\x98'     #  0xDF -> CONTROL
    u'\\'       #  0xE0 -> REVERSE SOLIDUS
    u'\xf6'     #  0xE1 -> LATIN SMALL LETTER O WITH DIAERESIS
    u'S'        #  0xE2 -> LATIN CAPITAL LETTER S
    u'T'        #  0xE3 -> LATIN CAPITAL LETTER T
    u'U'        #  0xE4 -> LATIN CAPITAL LETTER U
    u'V'        #  0xE5 -> LATIN CAPITAL LETTER V
    u'W'        #  0xE6 -> LATIN CAPITAL LETTER W
    u'X'        #  0xE7 -> LATIN CAPITAL LETTER X
    u'Y'        #  0xE8 -> LATIN CAPITAL LETTER Y
    u'Z'        #  0xE9 -> LATIN CAPITAL LETTER Z
    u'\xfd'     #  0xEA -> LATIN SMALL LETTER Y WITH ACUTE
    u'\xe2'     #  0xEB -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    u'\x99'     #  0xEC -> CONTROL
    u'\xe3'     #  0xED -> LATIN SMALL LETTER A WITH TILDE
    u'\xe0'     #  0xEE -> LATIN SMALL LETTER A WITH GRAVE
    u'\xe5'     #  0xEF -> LATIN SMALL LETTER A WITH RING ABOVE
    u'0'        #  0xF0 -> DIGIT ZERO
    u'1'        #  0xF1 -> DIGIT ONE
    u'2'        #  0xF2 -> DIGIT TWO
    u'3'        #  0xF3 -> DIGIT THREE
    u'4'        #  0xF4 -> DIGIT FOUR
    u'5'        #  0xF5 -> DIGIT FIVE
    u'6'        #  0xF6 -> DIGIT SIX
    u'7'        #  0xF7 -> DIGIT SEVEN
    u'8'        #  0xF8 -> DIGIT EIGHT
    u'9'        #  0xF9 -> DIGIT NINE
    u'\xfc'     #  0xFA -> LATIN SMALL LETTER U WITH DIAERESIS
    u'\xea'     #  0xFB -> LATIN SMALL LETTER E WITH CIRCUMFLEX
    u'\x9a'     #  0xFC -> CONTROL
    u'\xeb'     #  0xFD -> LATIN SMALL LETTER E WITH DIAERESIS
    u'\xe9'     #  0xFE -> LATIN SMALL LETTER E WITH ACUTE
    u'\x9f'     #  0xFF -> CONTROL
)

### Encoding table
encoding_table=codecs.charmap_build(decoding_table)

