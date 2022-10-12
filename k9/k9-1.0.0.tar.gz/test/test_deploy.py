from unittest import TestCase
from k9.core import *
from k9.deploy import *
from aws import cfm, secret
from aws.cert import generate_self_signed_cert, import_cert, get_certs
import os
import warnings


def exist_bucket(bucket_name: str):
    try:
        boto3.client('s3').list_objects(Bucket=bucket_name)
        return True
    except Exception:
        return False


def exist_cloudfront(distribution: str):
    try:
        boto3.client('cloudfront').get_distribution(Id=distribution)
        return True
    except Exception:
        return False


def exist_cert(domain_name: str):
    certs = get_certs()
    for c in certs:
        if c['DomainName'] == domain_name:
            return True

    return False


class TestDeploy(TestCase):

    @classmethod
    def setUpClass(cls):
        # Hide boto3 warnings. This is a known issue with boto3 + unittest.
        warnings.simplefilter('ignore', category=ResourceWarning)

        cluster_name = os.environ.get("CLUSTER_NAME")
        refresh_kubeconfig()
        cls.tag_dvl_uva = {
            "clusterName": cluster_name,
            "appName": "mockapp",
            "env": "dvl",
            "secretType": 'Application secret',
            "customer": "uva"
        }
        cls.tag_sat = {
            "clusterName": cluster_name,
            "appName": "mockapp",
            "env": "sat",
            "secretType": 'Application secret'
        }

        try:
            cls.DVL_MOCKAPP_UVA_SECRET = secret.create_secret(
                name='dvl-mockapp-uva-secret',
                description='Test secret for the mockapp application for the dvl environment',
                kvp={'testSecretKey': 'testSecretValue'},
                tags=cls.tag_dvl_uva)

            cls.SAT_MOCKAPP_SECRET = secret.create_secret(
                name='sat-mockapp-secret',
                description='Test secret for the mockapp application for the sat environment',
                kvp={'testSecretKeyTwo': 'testSecretValueTwo'},
                tags=cls.tag_sat)

        except Exception as e:
            if 'secret already exists' not in str(e):
                cls.tearDownClass()
                raise e

        warnings.simplefilter('ignore', category=ResourceWarning)

        root_dir = os.path.dirname(__file__)
        app_config_dir = os.path.join(root_dir, 'apps/testApp')
        cls.app_config = read_app_config(app_config_dir)

    @classmethod
    def tearDownClass(cls):
        secret.delete_secret('dvl-mockapp-uva-secret', perma_delete=True)
        secret.delete_secret('sat-mockapp-secret', perma_delete=True)

    ###########################################################################
    # Kubernetes Resources
    ###########################################################################

    def test_prepare_kubernetes_resources_cluster_nonexistent(self):
        app_config = {
            "appName": "mockapp",
            "appInstances": [
                {
                    "clusterName": "nonexistent",
                    "env": "dvl",
                    "customer": "na",
                    "appSecret": "dvl-mockapp-na-secret",
                    "namespace": "dvl-mockapp-na",
                }
            ]
        }
        with self.assertRaises(Exception):
            prepare_kubernetes_resources(app_config)
        self.assertFalse(namespace_exists(namespace='dvl-mockapp-na'))

    def test_prepare_kubernetes_resources_success(self):
        cluster_name = os.environ.get("CLUSTER_NAME")
        app_config = {
            "appName": "mockapp",
            "appInstances": [
                {
                    "clusterName": cluster_name,
                    "env": "dvl",
                    "customer": "uva",
                    "appSecret": "dvl-mockapp-uva-secret",
                    "generatedAppSecret": "dvl-mockapp-uva-secret",
                    "namespace": "dvl-mockapp-uva",
                    "dbName": "dvl_mockapp",
                    "dbSchema": "dvl_mockapp_uva"
                }, {
                    "clusterName": cluster_name,
                    "env": "sat",
                    "customer": "None",
                    "appSecret": "sat-mockapp-secret",
                    "generatedAppSecret": "sat-mockapp-secret",
                    "namespace": "sat-mockapp",
                    "dbName": "sat_mockapp",
                    "dbSchema": "sat_mockapp"
                }
            ]
        }
        prepare_kubernetes_resources(app_config)
        try:
            self.assertTrue(namespace_exists(namespace='dvl-mockapp-uva'))
            self.assertTrue(secret_exists(name='dvl-mockapp-uva-secret', namespace='dvl-mockapp-uva'))
            result = get_secret(name='dvl-mockapp-uva-secret', namespace='dvl-mockapp-uva')
            self.assertNotEqual(result, None)
            delete_namespace(namespace='dvl-mockapp-scc')
            self.assertFalse(namespace_exists(namespace='dvl-mockapp-scc'))
            delete_secret(name='dvl-mockapp-uva-secret', namespace='dvl-mockapp-uva')
            self.assertFalse(secret_exists(name='dvl-mockapp-uva-secret', namespace='dvl-mockapp-uva'))

            self.assertTrue(namespace_exists(namespace='sat-mockapp'))
            self.assertTrue(secret_exists(name='sat-mockapp-secret', namespace='sat-mockapp'))
            result = get_secret(name='sat-mockapp-secret', namespace='sat-mockapp')
            self.assertNotEqual(result, None)
            delete_namespace(namespace='sat-mockapp')
            self.assertFalse(namespace_exists(namespace='sat-mockapp'))
            delete_secret(name='sat-mockapp-secret', namespace='sat-mockapp')
            self.assertFalse(secret_exists(name='sat-mockapp-secret', namespace='sat-mockapp'))
        except Exception as e:
            print(e)
            self.fail('An unexpected exception was raised.')

    ###########################################################################
    # Deploy UI
    ###########################################################################

    def test_delete_ui_cert(self):
        # manually create a cert for deletion
        testing_cert_name = 'unittestdeleteuicert.atomictests.com'
        c = generate_self_signed_cert(testing_cert_name, 'US', 'Virginia', 'Alexandria',
                                      'SimonComputing', 2)
        import_cert(testing_cert_name, c.get('public', 'N/A'), c.get('private', 'N/A'))
        time.sleep(10)
        self.assertTrue(exist_cert(testing_cert_name))

        delete_ui_cert('unittest', 'k9-unit', testing_cert_name, False)
        time.sleep(10)
        self.assertFalse(exist_cert(testing_cert_name))

    def test_delete_ui_with_env_not_valid(self):
        app_config = {
            "appName": "mockapp",
            "appInstances": [
                {
                    "clusterName": "nonexistent",
                    "env": "dvl",
                    "customer": "na",
                    "appSecret": "dvl-mockapp-na-secret",
                    "namespace": "dvl-mockapp-na",
                }
            ]
        }

        try:
            delete_ui(app_config, 'bogus-env', True)
        except Exception as exc:
            assert False, f"'delete_ui' raised an exception {exc}"

    def test_delete_ui_with_env_valid(self):
        app_config = {
            "appName": "mockapp",
            "appInstances": [
                {
                    "clusterName": "nonexistent",
                    "env": "dvl",
                    "customer": "na",
                    "appSecret": "dvl-mockapp-na-secret",
                    "namespace": "dvl-mockapp-na",
                    "uiCertUrl": "*.mockapp.dvl.atomictests.com"
                },
                {
                    "clusterName": "nonexistent",
                    "env": "sat",
                    "uiCertUrl": "*.mockapp.sat.atomictests.com"
                }
            ]
        }
        try:
            delete_ui(app_config, 'dvl', True)
        except Exception as exc:
            assert False, f"'delete_ui' raised an exception {exc}"

    def test_create_and_delete_s3(self):
        cluster_name = os.environ.get("CLUSTER_NAME")
        test_bucket_name = f'{cluster_name.lower()}.unique.atomictests.com-builds'
        create_s3_if_not_exist(test_bucket_name)
        self.assertTrue(s3_exists(test_bucket_name))

        # call it again and not expect exception
        create_s3_if_not_exist(test_bucket_name)

        # delete it
        empty_and_delete_bucket(test_bucket_name)
        self.assertFalse(s3_exists(test_bucket_name))

    ###########################################################################
    # Promotion Jobs
    ###########################################################################

    def test_create_promote_ui_stack(self):
        test_dir = os.path.dirname(__file__)
        test_app_dir = os.path.join(test_dir, 'apps/testApp')
        stack = create_promote_ui_stack(test_app_dir)

        self.assertIsNotNone(stack)
        app_config = read_app_config(test_app_dir)
        app_name = app_config['appName']
        delete_promote_ui_stack(app_name)
        stack = cfm.find_stack(StackType='promote-ui', appName=app_name.lower())
        self.assertIsNone(stack)

    def test_create_promote_service_stack(self):
        test_dir = os.path.dirname(__file__)
        test_app_dir = os.path.join(test_dir, 'apps/testApp')
        stack = create_promote_service_stack(test_app_dir)

        self.assertIsNotNone(stack)
        app_config = read_app_config(test_app_dir)
        app_name = app_config['appName']
        delete_promote_service_stack(app_name)
        stack = cfm.find_stack(StackType='promote-service', appName=app_name.lower())
        self.assertIsNone(stack)

    ###########################################################################
    # App Config
    ###########################################################################

    def test_read_app_config(self):
        test_dir = os.path.dirname(__file__)
        test_app_dir = os.path.join(test_dir, 'apps/website-test')
        app_config = read_app_config(test_app_dir)
        self.assertIsNotNone(app_config)
        app_instances = app_config['appInstances']
        self.assertTrue(len(app_instances) == 3)
        for app_instance in app_instances:
            ui_url = app_instance['uiUrl']
            ui_cert_url = app_instance['uiCertUrl']
            alt_ui_cert_url = app_instance['altUiCertUrl']
            self.assertTrue('www' in ui_url)
            self.assertTrue('www' in ui_cert_url)
            self.assertTrue('www' in alt_ui_cert_url)
