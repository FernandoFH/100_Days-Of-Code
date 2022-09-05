from main import calculadora

def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora, 'sumar', lambda x: 5)
    clac = calculadora()
    assert clac.sumar() == 5
