from yaml_config.configuration import cut_protocol

from .dataset import cutprotocol


def test_cutprotocol():
    """Тест проверяет работоспособность функции с различными входными аргументами."""
    for i, arg in enumerate(cutprotocol.ARGS):
        function_return = cut_protocol(arg)
        assert function_return == cutprotocol.RESULT[i], f'При подаче на вход функции {arg} неверный результат'
