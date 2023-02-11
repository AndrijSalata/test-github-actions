from src.app import app_func


def test_app_func():
    assert app_func() == 'app_func_result'
