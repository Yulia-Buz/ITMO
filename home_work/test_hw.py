def test_hw():
    assert ('home','work') == ('home','work')

def test_hw1():
    assert 'QA' != 'QC'

def test_hw2():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
