from service import health


def test_is_active():
    assert health.is_active() is True
