from montypy.meaning.utils import sword

def test_mr_creosote():
    actual = sword()
    expected = "sword"
    assert actual == expected
    