from hello import hello, goodbye

def test_hello():
    assert 'Hello!' == hello()

def test_goodbye():
    assert 'Goodbye!' == goodbye()