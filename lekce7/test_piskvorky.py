from pisk import vyhodnot, tah, tah_pocitace

def test_vyhodnot():
    assert vyhodnot('--xxx---------------') == 'x'
    assert vyhodnot('--xooo--------------') == 'o'
    assert vyhodnot('xxooxxooxxooxxooxxoo') == '!'
    assert vyhodnot('') == '!'
    assert vyhodnot('1234') == '!'
    assert vyhodnot('xxxooooooooo--oo--oo') == 'x'

def test_tah():
    assert tah('--xooo--------------', 0, 'x') == 'x-xooo--------------'
    assert tah('--xooo--------------', 19, 'x') == '--xooo-------------x'
    assert tah('--xooo--------------', 1, 'o') == '-oxooo--------------'

def test_tah_pocitace():
    #chci otestovat že když je pole plné, funkce se ukončí
    assert tah_pocitace('xxooxxooxxooxxooxxoo') == break

