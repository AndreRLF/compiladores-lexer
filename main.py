from lx import lexer

if __name__ == '__main__':
    # Test it out
    data = '''
     absb = 3 + 4 * 10
       + - 20.2 *2;
     '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

