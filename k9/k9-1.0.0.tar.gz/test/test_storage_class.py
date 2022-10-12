from unittest import TestCase
from kubernetes import config
from k9.storage import *
from k9.core import abs_path
import os
import subprocess


class TestStorage(TestCase):

    @classmethod
    def setUpClass(cls):
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    def test_create_storage_class(self):
        name = 'unit-storage-class'

        print("")
        print(create_storage_class(abs_path('../test/storage.yml')))

        self.assertTrue(storage_class_exists(name))

        delete_storage_class(name)

        self.assertFalse(storage_class_exists(name))

    def test_create_storage_class_fail(self):
        with self.assertRaisesRegex(subprocess.CalledProcessError, 'returned non-zero exit status 1.'):
            create_storage_class('bogus')

    def test_delete_storage_class_fail(self):
        with self.assertRaisesRegex(subprocess.CalledProcessError, 'returned non-zero exit status 1.'):
            delete_storage_class('bogus')
