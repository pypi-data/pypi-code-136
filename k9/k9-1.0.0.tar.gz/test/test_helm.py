from unittest import TestCase
from kubernetes import config
import time
from k9.helm import *
from k9.core import set_default_namespace, delete_namespace, create_namespace


class TestHelm(TestCase):

    @classmethod
    def setUpClass(cls):
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    def test_helm_repo_add(self):
        if not namespace_exists('unittest'):
            create_namespace('unittest')
        set_default_namespace('unittest')
        helm_repo_add('simoncomputing', 'http://charts.simoncomputing.com')

        helm_repo_update()

        result = helm_repo_ls()

        found = [
            repo['name']
            for repo in result
            if repo['name'] == 'simoncomputing'
        ]

        self.assertEqual(1, len(found))

        result = helm_repo_remove('simoncomputing')
        self.assertTrue("has been removed" in result.stdout)

    def test_helm_repo_add_fail(self):
        with self.assertRaisesRegex(Exception, "non-zero exit status 1."):
            helm_repo_add('simoncomputing', 'http://bogus')

    def test_helm_repo_remove_fail(self):
        with self.assertRaisesRegex(Exception, "non-zero exit status 1."):
            helm_repo_remove('bogus')

    def test_helm_install(self):
        try:
            if not namespace_exists('unittest'):
                create_namespace('unittest')
            set_default_namespace('unittest')

            helm_repo_add('bitnami', 'https://charts.bitnami.com/bitnami')
            time.sleep(5)  # propagate changes

            # ensure repo added
            result = helm_repo_ls()
            found = [
                repo['name']
                for repo in result
                if repo['name'] == 'bitnami'
            ]
            self.assertEqual(1, len(found))

            release_name = 'tomcat'
            # Test helm_install()
            helm_install('bitnami/tomcat', {'domain': 'sandbox.simoncomputing.com'})

            # test helm_ls()
            result = helm_ls()
            found = [
                release
                for release in result
                if release['name'] == release_name
            ]
            self.assertIsNotNone(found)
            self.assertEqual(release_name, found[0]['name'])

            # test helm_exists()
            self.assertTrue(helm_exists(release_name))

        finally:
            # test helm_uninstall()
            result = helm_uninstall(release_name)
            print(f'result={result.stdout}')
            self.assertTrue('uninstalled' in result.stdout)
            self.assertFalse(helm_exists(release_name))

            helm_repo_remove('bitnami')
            delete_namespace('unittest')

    def test_helm_install_custom_vals(self):
        try:
            set_default_namespace('unittest')
            if not namespace_exists('unittest'):
                create_namespace('unittest')

            helm_repo_add('bitnami', 'https://charts.bitnami.com/bitnami')

            time.sleep(5)  # propagate changes
            release_name = 'tomcat'
            # Test helm_install()
            helm_install('bitnami/tomcat', {'domain': 'sandbox.simoncomputing.com'},
                         values_path='./charts/tomcat-values.yml')

            # test helm_ls()
            result = helm_ls()
            found = [
                release
                for release in result
                if release['name'] == release_name
            ]
            self.assertIsNotNone(found)
            self.assertEqual(release_name, found[0]['name'])

            # test helm_exists()
            self.assertTrue(helm_exists(release_name))

        finally:
            # test helm_uninstall()
            result = helm_uninstall(release_name)
            print(f'result={result.stdout}')
            self.assertTrue('uninstalled' in result.stdout)
            self.assertFalse(helm_exists(release_name))

            helm_repo_remove('bitnami')
            delete_namespace('unittest')

    def test_helm_uninstall_fail(self):
        with self.assertRaisesRegex(Exception, 'returned non-zero exit status'):
            helm_uninstall('bogus')
