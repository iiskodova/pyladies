def display_hangman(tries):
    stages = ['''
    +
    |
    |
    |
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |
    |
    |
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |
    |
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    |
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    |   |
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    | --|
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    | --|--
    |
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    | --|--
    |  /
    |
    ~~~~~~~
    ''',
    '''
    +---.
    |   |
    |   O
    | --|--
    |  / \_
    |
    ~~~~~~~
    ''']
    return stages[tries]
