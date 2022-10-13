import ec2_manager


class CustomManager(ec2_manager.EC2Manager):
    pass


if __name__ == '__main__':
    custom_manager = CustomManager()
    custom_manager.apply()
