from .validations import BadiValidators


def test_validate_username(value):
    print("test_validate_username(`", value, "`):", BadiValidators.username(value))


if __name__ == '__main__':
    test_validate_username("1234")
    test_validate_username("mohammad")
    test_validate_username("mo")
    test_validate_username("mohammad.shekari")
    test_validate_username("mohammad_shekari")
    test_validate_username("mohammad-shekari")
