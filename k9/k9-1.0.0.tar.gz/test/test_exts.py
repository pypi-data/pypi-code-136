from unittest import TestCase
from k9.exts import *
from k9.apps import *
from kubernetes import config
import os


class TestExts(TestCase):

    @classmethod
    def setUpClass(cls):
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    ###########################################################################
    # Ingress
    ###########################################################################
    def test_ingress(self):
        try:
            ##################
            # Arrange
            secret_name = "tomcat-dev"
            deploy_name = 'tomcat-dev'
            svc_name = 'tomcat-svc-dev'
            ing_name = 'tomcat-ing-dev'

            # create namespace
            set_default_namespace("ingress-unit-test")
            if not namespace_exists("ingress-unit-test"):
                create_namespace()

            # create secret
            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }
            create_secret(secret_name, secrets)

            # create deployment
            body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
            create_deployment(body)

            # create service
            body = read_yaml(abs_path('../test/tomcat-svc-dev.yml'))
            create_service(body)

            ##################
            # Act

            # create ingress
            body = read_yaml(abs_path('../test/tomcat-ing-dev.yml'))
            result = create_ingress(body)
            self.assertEqual(ing_name, result.metadata.name)

            ##################
            # Assert

            # test get_ingress()
            result = get_ingress(ing_name)
            self.assertEqual(ing_name, result.metadata.name)

            # test ingress_exists()
            self.assertTrue(ingress_exists(ing_name))

            # test list_ingress()
            found = [
                ing['name']
                for ing in list_ingress()
                if ing['name'] == ing_name
            ]
            self.assertEqual(1, len(found))

        finally:
            delete_ingress(ing_name)
            delete_service(svc_name)
            delete_deployment(deploy_name)
            delete_secret(secret_name)
            delete_namespace()

    def test_ingress_exists_fail(self):
        self.assertFalse(ingress_exists('bogus'))

    def test_delete_bogus_ingress(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_ingress('bogus'))

    def test_add_ingress_rule(self):
        secret_name = "tomcat-dev"
        deploy_name = 'tomcat-dev'
        svc_name = 'tomcat-svc-dev'
        ing_name = 'tomcat-ing-dev'
        try:
            # create namespace
            set_default_namespace("ingress-unit-test")
            if not namespace_exists("ingress-unit-test"):
                create_namespace()

            # create secret
            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }
            create_secret(secret_name, secrets)
            # create deployment
            body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
            create_deployment(body)
            # create service
            body = read_yaml(abs_path('../test/tomcat-svc-dev.yml'))
            create_service(body)
            # create ingress
            body = read_yaml(abs_path('../test/tomcat-ing-dev.yml'))
            result = create_ingress(body)

            add_ingress_rule(ing_name, svc_name, 8080, 'check.for.this', ['/this/path/too/'])

            final_ing = get_ingress(ing_name)

            found_new_rule = False
            for rules in final_ing.spec.rules:
                if rules.host == 'check.for.this' and rules.http.paths[0].path == '/this/path/too/':
                    found_new_rule = True
            self.assertTrue(found_new_rule)
        finally:
            delete_ingress(ing_name)
            delete_service(svc_name)
            delete_deployment(deploy_name)
            delete_secret(secret_name)
            delete_namespace()
        pass
