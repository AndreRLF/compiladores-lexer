from ply_parser import parser

text = "3 + 5 * 2 + (5 + 3) / 2"

print(parser.parse(text))