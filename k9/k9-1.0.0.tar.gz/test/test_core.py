import base64
import io
import os.path
from datetime import timedelta
from unittest import TestCase, mock

from k9.apps import *

pp = pprint.PrettyPrinter(indent=2, width=120)


class TestCore(TestCase):

    @classmethod
    def setUpClass(cls):
        refresh_kubeconfig()

    ###########################################################################
    # Util
    ###########################################################################

    def test_run_command_success(self):
        set_run_output(True)
        result = run_command('ls', '-la')
        self.assertTrue('charts' in result.stdout)

    def test_run_command_fail(self):
        with self.assertRaisesRegex(FileNotFoundError, 'No such file or directory'):
            run_command('bogus -la')

    def test_last_word(self):
        self.assertEqual('my-pod', last_word('pods/my-pod'))

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_view_yaml(self, mock_stdout):
        view_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
        self.assertTrue('tomcat-dev' in mock_stdout.getvalue())

    def test_read_yaml(self):
        body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
        self.assertEqual('tomcat-dev', body['metadata']['name'])

    def test_age(self):
        now = datetime.now(timezone.utc)

        diff = timedelta(hours=14, minutes=4, seconds=22)
        then = now - diff
        self.assertEqual('14:04:22', get_age(then))

        diff = timedelta(hours=4, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('04:14:02', get_age(then))

        diff = timedelta(hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('23:14:02', get_age(then))

        diff = timedelta(days=1, hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('1d', get_age(then))

        diff = timedelta(days=25, hours=23, minutes=14, seconds=2)
        then = now - diff
        self.assertEqual('25d', get_age(then))

    def test_absolute_dir(self):
        result = abs_path('test')

        self.assertTrue(len(result) > 4)
        self.assertTrue('/' in result)
        self.assertEqual('test', last_word(result))

    ###########################################################################
    # Namespace
    ###########################################################################

    def test_list_namespaces(self):
        result = list_namespaces()
        self.assertTrue(len(result) > 0)

    def test_default_namespace(self):
        set_default_namespace("test")
        self.assertEqual("test", get_default_namespace())

    def test_default_namespace_exists(self):
        set_default_namespace("ononononon")
        self.assertFalse(default_namespace_exists())
        set_default_namespace("default")
        self.assertTrue(default_namespace_exists())

    def test_create_namespace(self):
        try:
            ns = "namespace-unit-test"
            set_default_namespace(ns)

            create_namespace()
            self.assertTrue(namespace_exists())

            result = get_namespace()
            self.assertEqual(ns, result.metadata.name)

        finally:
            delete_namespace()
            self.assertFalse(namespace_exists())

    def test_delete_bogus_namespace(self):
        self.assertEqual(None, delete_namespace('bogus'))

    def test_get_bogus_namespace(self):
        with self.assertRaisesRegex(Exception, 'You must call set_default_namespace()'):
            get_default_namespace()
            set_default_namespace('')
            get_default_namespace()

    ###########################################################################
    # Pods
    ###########################################################################

    def test_list_pods(self):
        try:
            result = list_pods("kube-system")
            self.assertIsNotNone(result)
            self.assertTrue(len(result) > 0)

            create_namespace('asdfjkl')
            set_default_namespace("asdfjkl")
            result = list_pods()
            self.assertTrue(len(result) == 0)
        finally:
            delete_namespace('asdfjkl')

    def test_wait_for_pod(self):
        try:
            set_default_namespace("wait-test")
            if not namespace_exists("wait-test"):
                create_namespace("wait-test")

            if not deployment_exists("tomcat"):
                secret_name = "tomcat-dev"
                secrets = {
                    'ds-url': 'https://some/url',
                    'password': 'My1SecretPassword',
                    'username': 'postgres'
                }
                create_secret(secret_name, secrets)
                body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
                create_deployment(body)
                time.sleep(1)

            pods = list_pods()
            print(pods)
            self.assertEqual(pods[0]['status'], 'Pending')
            wait_for_pod(pods[0]['name'])
            pods = list_pods()
            self.assertEqual(pods[0]['status'], 'Running')
        finally:
            delete_deployment('tomcat-dev')
            delete_secret('tomcat-dev')
            delete_namespace('wait-test')

    def test_get_pod_logs(self):
        try:
            set_default_namespace("log-test")
            if not namespace_exists("log-test"):
                create_namespace("log-test")

            if not deployment_exists("tomcat"):
                secret_name = "tomcat-dev"
                secrets = {
                    'ds-url': 'https://some/url',
                    'password': 'My1SecretPassword',
                    'username': 'postgres'
                }
                create_secret(secret_name, secrets)
                body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
                create_deployment(body)
                time.sleep(1)
            pods = list_pods()
            wait_for_pod(pods[0]['name'])
            logs = get_pod_logs(pods[0]['name'], 'tomcat')
            self.assertNotEqual(logs.find('VersionLoggerListener'), -1)
        finally:
            delete_deployment('tomcat-dev')
            delete_secret('tomcat-dev')
            delete_namespace('log-test')

    def test_get_pod_logs_except(self):
        try:
            get_pod_logs('THISPODDOESNOTEXIST', 'NOCONTAINER')
            self.fail()
        except:
            print('correctly excepted non-existsent pod')

    def test_copy_to_from_pod(self):
        try:
            # uses example-file.txt
            set_default_namespace("copy-test")
            if not namespace_exists("copy-test"):
                create_namespace("copy-test")
            if not deployment_exists("tomcat"):
                secret_name = "tomcat-dev"
                secrets = {
                    'ds-url': 'https://some/url',
                    'password': 'My1SecretPassword',
                    'username': 'postgres'
                }
                create_secret(secret_name, secrets)
                body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
                create_deployment(body)
                time.sleep(1)
            pods = list_pods()
            print(f'pods are {pods}')
            self.assertIsNotNone(pods)
            wait_for_pod(pods[0]['name'])
            copy_to_pod(pods[0]['name'], abs_path('../test/example-file.txt'), '/var/example-file.txt')
            copy_from_pod(pods[0]['name'], '/var/example-file.txt', abs_path('../test/newex.txt'))
            self.assertTrue(os.path.exists(abs_path('../test/newex.txt')))

        finally:
            delete_deployment('tomcat-dev')
            delete_secret('tomcat-dev')
            delete_namespace('copy-test')
            run_command('rm', '-f', abs_path('../test/newex.txt'))

    ###########################################################################
    # Secrets
    ###########################################################################

    def test_create_secret(self):
        try:
            set_default_namespace("default")

            secret_name = "tomcat-dev"
            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            # Test create_secret()
            result = create_secret(secret_name, secrets)
            self.assertEqual(secret_name, result.metadata.name)

            # Test get_secret()
            result = get_secret(secret_name)
            self.assertEqual(secret_name, result.metadata.name)

            # Check secret values
            for key, value in result.data.items():
                self.assertEqual(secrets[key], base64.b64decode(value).decode('utf8'))

            # Test secret_exists()
            self.assertTrue(secret_exists(secret_name))

            # Test list_secret()
            result = list_secrets()

            secret_list = [
                s['name']
                for s in result
                if s['name'] == secret_name
            ]

            self.assertEqual(1, len(secret_list))
            self.assertEqual(secret_name, secret_list[0])

        finally:
            delete_secret(secret_name)

    def test_secret_exists(self):
        set_default_namespace('default')
        self.assertFalse(secret_exists('bogus-secret'))

    def test_delete_bogus_secret(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_secret('bogus'))

    ###########################################################################
    # Services
    ###########################################################################
    def test_service(self):
        try:
            # Arrange
            svc_name = 'tomcat-svc-dev'
            secret_name = "tomcat-dev"
            deploy_name = 'tomcat-dev'

            set_default_namespace("service-unit-test")
            if not namespace_exists("service-unit-test"):
                create_namespace()

            secrets = {
                'ds-url': 'https://some/url',
                'password': 'My1SecretPassword',
                'username': 'postgres'
            }

            create_secret(secret_name, secrets)
            body = read_yaml(abs_path('../test/tomcat-deploy-dev.yml'))
            create_deployment(body)

            # Act
            body = read_yaml(abs_path('../test/tomcat-svc-dev.yml'))

            create_service(body)

            # Assert
            result = get_service(svc_name)
            self.assertEqual(svc_name, result.metadata.name)

            result = list_services()
            found = [
                svc['name']
                for svc in result
                if svc_name in svc['name']
            ]
            self.assertEqual(1, len(found))

        finally:
            if service_exists(svc_name):
                delete_service(svc_name)

            delete_deployment(deploy_name)

            delete_secret(secret_name)
            delete_namespace()

    def test_service_exists_fail(self):
        set_default_namespace('default')
        self.assertFalse(service_exists('bogus'))

    def test_delete_bogus_service(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_service('bogus'))

    ###########################################################################
    # Service Accounts
    ###########################################################################

    def test_service_accounts(self):
        try:
            ############
            # Arrange
            set_default_namespace('default')
            sa_name = "unit-test-tomcat-sa"

            ############
            # Act
            result = create_service_account(sa_name)

            ############
            # Assert

            self.assertEqual(sa_name, result.metadata.name)

            # test get_service_account()
            result = get_service_account(sa_name)
            self.assertEqual(sa_name, result.metadata.name)

            # test service_account_exists()
            self.assertTrue(service_account_exists(sa_name))

            # test_list_service_accounts()
            result = list_service_accounts()

            result = [
                sa['name']
                for sa in result
                if sa['name'] == sa_name
            ]
            self.assertEqual(1, len(result))

        finally:
            delete_service_account(sa_name)

    def test_service_account_exists_fail(self):
        set_default_namespace('default')
        self.assertFalse(service_account_exists('bogus'))
        self.assertTrue(service_account_exists('default'))

    def test_list_service_account_fail(self):
        self.assertEqual(0, len(list_service_accounts('bogus')))

    def test_delete_bogus_service_account(self):
        set_default_namespace('default')
        self.assertEqual(None, delete_service_account('bogus'))

    ###########################################################################
    # Config Maps
    ###########################################################################

    def test_create_delete_configmap(self):
        refresh_kubeconfig()
        if not namespace_exists('configmaptest'):
            create_namespace('configmaptest')
        set_default_namespace('configmaptest')

        body = {
            'apiVersion': 'v1',
            'data': {
                'hello': 'world'
            },
            'kind': 'ConfigMap',
            'metadata': {
                'name': 'testconfig'
            }
        }

        try:
            r = create_configmap(body)

            self.assertIsNotNone(r)
            self.assertEquals(r.kind, 'ConfigMap')
            self.assertEquals(r.data.get('hello', 'NO'), 'world')
        finally:
            d = delete_configmap('testconfig')
            self.assertTrue(d)

            delete_namespace('configmaptest')
            set_default_namespace('default')

    def test_get_bad_configmap(self):
        a = get_configmap('doesnotexist!!!')
        self.assertFalse(a)

    def test_delete_bad_configmap(self):
        a = delete_configmap('doesnotexist!!!!!')
        self.assertFalse(a)

    def test_update_configmap(self):
        if not namespace_exists('configmaptest'):
            create_namespace('configmaptest')
        set_default_namespace('configmaptest')

        body = {
            'apiVersion': 'v1',
            'data': {
                'hello': 'world',
                'delete': 'this'
            },
            'kind': 'ConfigMap',
            'metadata': {
                'name': 'testconfig'
            }
        }
        try:
            r = create_configmap(body)
            old = get_configmap('testconfig')

            self.assertIsNotNone(old)
            self.assertEquals(old.kind, 'ConfigMap')
            self.assertEquals(old.data.get('hello', 'NO'), 'world')

            new_data = {
                'hiya': 'planet',
                'delete': None
            }
            old.data = new_data

            nr = update_configmap('testconfig', old)
            self.assertIsNotNone(nr)
            self.assertEquals(nr.kind, 'ConfigMap')
            self.assertEquals(nr.data.get('hiya', 'NO'), 'planet')

            new = get_configmap('testconfig')
            self.assertIsNotNone(new)
            self.assertEquals(new.kind, 'ConfigMap')
            self.assertEquals(new.data.get('hiya', 'NO'), 'planet')
            self.assertEquals(new.data.get('delete', 'NOT'), 'NOT')
            self.assertEquals(new.data.get('hello', 'NO'), 'world')

        finally:
            d = delete_configmap('testconfig')

            delete_namespace('configmaptest')
            set_default_namespace('default')

    def test_list_configmap(self):
        if not namespace_exists('configmaptest'):
            create_namespace('configmaptest')
        set_default_namespace('configmaptest')
        body1 = {
            'apiVersion': 'v1',
            'data': {
                'hello': 'world'
            },
            'kind': 'ConfigMap',
            'metadata': {
                'name': 'testconfig1'
            }
        }

        body2 = {
            'apiVersion': 'v1',
            'data': {
                'hiya': 'planet'
            },
            'kind': 'ConfigMap',
            'metadata': {
                'name': 'testconfig2'
            }
        }
        try:
            create_configmap(body1)
            create_configmap(body2)

            maps = list_configmap()

            for m in maps:
                if m.metadata.name == 'testconfig1':
                    self.assertTrue(m.data.get('hello', 'NO'), 'world')
                elif m.metadata.name == 'testconfig2':
                    self.assertTrue(m.data.get('hiya', 'NO'), 'planet')
        finally:
            delete_configmap('testconfig1')
            delete_configmap('testconfig2')
            delete_namespace('configmaptest')
            set_default_namespace('default')

    ###########################################################################
    # AWS Auth
    ###########################################################################

    def test_aws_auth_user(self):
        iam = 'fake_arn'
        k8s = 'k8s_user'
        groups = ['test', 'another:group']

        a = add_aws_auth_user(iam, k8s, groups)

        new_user = get_aws_auth_user('fake_arn')
        self.assertEqual('fake_arn', new_user.get('userarn', 'BAD'))
        self.assertEqual('k8s_user', new_user.get('username', 'BAD'))
        self.assertEqual('test', new_user.get('groups', 'BAD')[0])
        self.assertEqual('another:group', new_user.get('groups', 'BAD')[1])

        n = update_aws_auth_user('fake_arn', 'different_k8s_user')
        upped_yaml = yaml.safe_load(n.data.get('mapUsers', '[]'))
        for m in upped_yaml:
            if m.get('userarn', 'BAD') == 'fake_arn':
                self.assertEqual('different_k8s_user', m.get('username', 'BAD'))

        d = delete_aws_auth_user('fake_arn')
        self.assertTrue(d)

    def test_get_bad_aws_users_roles(self):
        a = get_aws_auth_user('NOPETHISISNOTAUSER')
        self.assertFalse(a)
        b = get_aws_auth_user(kube_user='STILLNOTAUSER')
        self.assertFalse(b)
        c = get_aws_auth_role('NOPETHISISNOTAROLE')
        self.assertFalse(c)
        d = get_aws_auth_role(kube_user='STILLNOTAROLE')
        self.assertFalse(d)
        e = delete_aws_auth_user('NOTGETTINGIT?')
        self.assertFalse(e)
        f = delete_aws_auth_role('GUESSNOT!!')
        self.assertFalse(f)
        g = update_aws_auth_user('ALMOSTTHERE')
        self.assertFalse(g)
        h = update_aws_auth_role('STICKTHELANDING!!!')
        self.assertFalse(h)

    def test_aws_auth_role(self):
        iam = 'fake_arn'
        k8s = 'k8s_user'
        groups = ['test', 'another:group']

        a = add_aws_auth_role(iam, k8s, groups)

        new_role = get_aws_auth_role('fake_arn')
        self.assertEqual('fake_arn', new_role.get('rolearn', 'BAD'))
        self.assertEqual('k8s_user', new_role.get('username', 'BAD'))
        self.assertEqual('test', new_role.get('groups', 'BAD')[0])
        self.assertEqual('another:group', new_role.get('groups', 'BAD')[1])

        n = update_aws_auth_role('fake_arn', 'different_k8s_user')
        upped_yaml = yaml.safe_load(n.data.get('mapRoles', '[]'))
        for m in upped_yaml:
            if m.get('rolearn', 'BAD') == 'fake_arn':
                self.assertEqual('different_k8s_user', m.get('username', 'BAD'))

        d = delete_aws_auth_role('fake_arn')
        self.assertTrue(d)

    ###########################################################################
    # Application Databases
    ###########################################################################

    def test_create_app_databass_missing_config(self):
        with self.assertRaisesRegex(ValueError, "The application configuration is required."):
            create_app_databases(app_config={})

    def test_create_app_databases_missing_appName(self):
        conf = {
            'deployments': 'none'
        }
        with self.assertRaisesRegex(ValueError, "The appName is required."):
            create_app_databases(app_config=conf)

    def test_create_app_databases_no_env(self):
        cluster_name = os.getenv("CLUSTER_NAME")
        conf = {
            'appName': 'mockappmmm',
            'deployments': [
                {'clusterName': cluster_name, 'environments': [{'customers': ['uc', 'uva', 'vt']}, {'env': 'sat'}]}
            ]
        }
        with self.assertRaisesRegex(ValueError, "The env key is required for each deployment."):
            create_app_databases(app_config=conf)

    # commented out until fixed
    # def test_create_app_databases_and_delete_success(self):
    #     cluster_name = os.getenv("CLUSTER_NAME")
    #     conf = {
    #         'appName': 'mockappmmm',
    #         'deployments': [
    #             {'clusterName': cluster_name, 'environments': [{'env': 'dvl', 'customers': ['uc', 'uva', 'vt']}, {'env': 'sat'}]}
    #         ]
    #     }
    #     no_action, successful, failure = create_app_databases(app_config=conf)
    #     refresh_kubeconfig()
    #     if len(no_action) > 0 or len(failure) > 0 or len(successful) != 2:
    #         self.fail('Not all application databases have been created.')
    #     no_action, successful, failure = delete_app_database(cluster_name=cluster_name, app_name='mockappmmm', env='dvl')
    #     refresh_kubeconfig()
    #     if len(no_action) > 0 or len(successful) != 1 or len(failure) > 0:
    #         self.fail('Deletion of application database was unsuccessful.')
    #     if os.getenv('automated') == '1':
    #         kube_config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    def test_delete_app_database_missing_required(self):
        with self.assertRaisesRegex(ValueError, "All parameters except rds_instance are required"):
            delete_app_database(cluster_name='', app_name='', env='')

    def test_delete_app_database_secret_nonexistent(self):
        result = delete_app_database(cluster_name='qwerty', app_name='wertyu', env='ertyui')
        self.assertEqual(result, (None, None, None))
