from unittest import TestCase
from kubernetes import config
from k9.apps import *
import os


class TestApps(TestCase):

    @classmethod
    def setUpClass(cls):
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    ###########################################################################
    # Deployments
    ###########################################################################

    def test_deployments(self):
        try:
            secret_name = "tomcat-dev"
            deploy_name = 'tomcat-dev'

            set_default_namespace("deployment-unit-test")
            if not namespace_exists("deployment-unit-test"):
                create_namespace()

            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            # Test create_secret()
            create_secret(secret_name, secrets)

            body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
            create_deployment(body)
            self.assertTrue(deployment_exists(deploy_name))

            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)

            result = [
                d
                for d in list_deployments()
                if d['name'] == deploy_name
            ]
            self.assertEqual(1, len(result))
            self.assertFalse(deployment_exists('bogus'))

            # Update deployment
            update_deployment_image(deploy_name, 'tomcat', 'tomcat:8')

            # Confirm that deployment image has been updated.
            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)
            found = [
                container.image
                for container in result.spec.template.spec.containers
                if container.name == 'tomcat'
            ]
            self.assertEqual('tomcat:8', found[0])

            # Scale deployment
            spec = {
                'replicas': 3
            }
            scale_deployment(deploy_name, spec)
            result = get_deployment(deploy_name)
            self.assertEqual(deploy_name, result.metadata.name)
            self.assertEqual(3, result.spec.replicas)

        finally:

            delete_deployment(deploy_name)
            delete_secret(secret_name)
            delete_namespace()

    def test_delete_bogus_deployment(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_deployment('bogus'))
