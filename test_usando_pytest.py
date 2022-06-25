from unittest.mock import patch
from somando import somar

#### TESTING ABRIR ARQUIVO COM DADOS ###########
# f = open("6.in", "r")
# arquivo = f.read()
# arquivo = arquivo.split("\n")
# arquivo = map(lambda x: int(x), arquivo)
# arquivo = list(arquivo)
# print(arquivo)

ENTRADA = [1,2,3,4,5]

@patch('builtins.input', side_effect=ENTRADA)
def test_to_roman_numeral_simple(mock_input):
    ESPERADO = 15
    
    assert ESPERADO == somar()