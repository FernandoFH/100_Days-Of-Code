import pytest
from main import escribir, suma

def test_suma():
    assert suma(2, 3) == 5

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2, 3, 5),
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (3, 2, 5), 
        (suma(2,2), 4, 8),
        (suma(3,2), 5, 10),
    ]
)
def test_suma_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected

def test_temp_dir(tmpdir):
    data_in = "Hola mundo"
    fpath = f"{tmpdir}/test.txt"
    escribir(fpath, data_in)

    with open(fpath, 'r') as file_out:
        data_out = file_out.read()

    assert data_in == data_out
