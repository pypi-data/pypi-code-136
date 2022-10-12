from unittest import TestCase

from kubernetes import config

from k9.apps import delete_deployment
from k9.cluster_init import *
from k9.core import delete_namespace

SIMON_CHARTS = 'https://charts.simoncomputing.com'

HELM_PARAMS = {
    'vpcName': 'k9-unit-test',
    'domain': 'k9.simoncomputing.com',
    'certArn': 'fake-bad-whatever',
    'jenkinsPass': 'jpass'  # changed in config step
}

DEFAULT_SC = 'yaml/default-sc.yml'


class TestClusterInit(TestCase):

    @classmethod
    def setUpClass(cls):
        refresh_kubeconfig()

    def test_jenkins_ready(self):
        set_run_output(False)
        helm_repo_add('simoncomputing', SIMON_CHARTS)
        helm_repo_update()
        set_run_output(True)
        set_default_namespace('unit-cluster-tools')
        if not namespace_exists():
            create_namespace('unit-cluster-tools')
        if not storage_class_exists('standard'):
            result = run_command('kubectl', 'apply', '-f', abs_path(DEFAULT_SC))
            errors = result.stderr
            if errors:
                self.fail('Error in creating standard storage class: ' + errors)
            helm_install('simoncomputing/aws-storage', {}, release_name='aws-storage',
                         values_path=abs_path('yaml/aws-storage-values.yml'))

        try:
            install_jenkins(HELM_PARAMS, 'unit-cluster-tools')
            install_jenkins(HELM_PARAMS, 'unit-cluster-tools')
            helm_uninstall('jenkins', 'unit-cluster-tools')
        except Exception as e:
            print(e)
        finally:
            if helm_exists('jenkins', 'unit-cluster-tools'):
                helm_uninstall('jenkins', 'unit-cluster-tools')
            delete_namespace('unit-cluster-tools')

    def test_efk_ready(self):
        set_run_output(False)
        helm_repo_add('simoncomputing', SIMON_CHARTS)
        helm_repo_update()
        set_run_output(True)
        set_default_namespace('unit-cluster-tools')
        if not namespace_exists():
            create_namespace('unit-cluster-tools')
        if not storage_class_exists('standard'):
            result = run_command('kubectl', 'apply', '-f', abs_path(DEFAULT_SC))
            errors = result.stderr
            if errors:
                self.fail('Error in creating standard storage class: ' + errors)
            helm_install('simoncomputing/aws-storage', {}, release_name='aws-storage',
                         values_path=abs_path('yaml/aws-storage-values.yml'))

        try:
            install_efk(HELM_PARAMS, 'unit-cluster-tools')
            install_efk(HELM_PARAMS, 'unit-cluster-tools')
            helm_uninstall('efk', 'unit-cluster-tools')
        except Exception as e:
            print(e)
        finally:
            if helm_exists('efk', 'unit-cluster-tools'):
                helm_uninstall('efk', 'unit-cluster-tools')
            delete_namespace('unit-cluster-tools')

    # def test_sonarqube_ready(self):
    #    set_run_output(False)
    #    helm_repo_add('simoncomputing', SIMON_CHARTS)
    #    helm_repo_update()
    #    set_run_output(True)
    #    set_default_namespace('unit-cluster-tools')
    #    if not namespace_exists():
    #        create_namespace('unit-cluster-tools')
    #    if not storage_class_exists('standard'):
    #        helm_install('simoncomputing/aws-storage', {}, release_name = 'aws-storage', values_path = abs_path('yaml/aws-storage-values.yml'))
    #
    #    # sonar url/pw
    #    rds = get_db_instance('k9-unit-test-rds')[0]
    #    sonar_values = HELM_PARAMS
    #    sonar_values['sonarServerHost'] = rds.get('Endpoint', {}).get('Address', 'bad_rds_host')
    #    
    #    sonar_secret = {
    #      'postgresql-password': 'password'
    #    }
    #    create_secret('sonar-password', sonar_secret)
    #
    #    try:
    #        s = install_sonarqube(sonar_values, 'unit-cluster-tools')
    #        self.assertTrue(install_sonarqube(sonar_values, 'unit-cluster-tools'))
    #        helm_uninstall('sonarqube', 'unit-cluster-tools')
    #        self.assertTrue(s)
    #    except Exception as e:
    #        print(e)
    #    finally:
    #        if helm_exists('sonarqube', 'unit-cluster-tools'):
    #            helm_uninstall('sonarqube', 'unit-cluster-tools')
    #        if secret_exists('sonar-password'):
    #            delete_secret('sonar-password')
    #        delete_namespace('unit-cluster-tools')
    #        refresh_kubeconfig()

    def test_prometheus_ready(self):
        set_run_output(False)
        helm_repo_add('simoncomputing', SIMON_CHARTS)
        helm_repo_update()
        set_run_output(True)
        set_default_namespace('unit-cluster-tools')
        if not namespace_exists():
            create_namespace('unit-cluster-tools')
        if not storage_class_exists('standard'):
            result = run_command('kubectl', 'apply', '-f', abs_path(DEFAULT_SC))
            errors = result.stderr
            if errors:
                self.fail('Error in creating standard storage class: ' + errors)
            helm_install('simoncomputing/aws-storage', {}, release_name='aws-storage',
                         values_path=abs_path('yaml/aws-storage-values.yml'))
        try:
            install_prometheus(HELM_PARAMS, 'unit-cluster-tools')
            install_prometheus(HELM_PARAMS, 'unit-cluster-tools')
            helm_uninstall('prometheus', 'unit-cluster-tools')
        except Exception as e:
            print(e)
        finally:
            if helm_exists('prometheus', 'unit-cluster-tools'):
                helm_uninstall('prometheus', 'unit-cluster-tools')
            delete_namespace('unit-cluster-tools')

    def test_grafana_ready(self):
        set_run_output(False)
        helm_repo_add('simoncomputing', SIMON_CHARTS)
        helm_repo_update()
        set_run_output(True)
        set_default_namespace('unit-cluster-tools')
        if not namespace_exists():
            create_namespace('unit-cluster-tools')
        if not storage_class_exists('standard'):
            result = run_command('kubectl', 'apply', '-f', abs_path(DEFAULT_SC))
            errors = result.stderr
            if errors:
                self.fail('Error in creating standard storage class: ' + errors)
            helm_install('simoncomputing/aws-storage', {}, release_name='aws-storage',
                         values_path=abs_path('yaml/aws-storage-values.yml'))
        try:
            install_grafana(HELM_PARAMS, 'unit-cluster-tools')
            install_grafana(HELM_PARAMS, 'unit-cluster-tools')
            helm_uninstall('grafana', 'unit-cluster-tools')
        except Exception as e:
            print(e)
        finally:
            if helm_exists('grafana', 'unit-cluster-tools'):
                helm_uninstall('grafana', 'unit-cluster-tools')
            delete_namespace('unit-cluster-tools')

    def test_install_aws_tools(self):
        set_default_namespace('unit-cluster-tools')
        if not namespace_exists():
            create_namespace('unit-cluster-tools')

        try:
            a = install_aws_tools(HELM_PARAMS)
            self.assertTrue(install_aws_tools(HELM_PARAMS))
            delete_deployment('cluster-autoscaler', 'kube-system')
            run_command('kubectl', 'delete', '-f', abs_path('yaml/autoscaler/infra.yml'))
            self.assertTrue(a)
        except Exception as e:
            print(e)
        finally:
            delete_namespace('unit-cluster-tools')

    #
    # def test_cluster_init_full_dev(self):
    #    if not namespace_exists('unit-cluster-tools'):
    #        create_namespace('unit-cluster-tools')
    #    set_default_namespace('unit-cluster-tools')
    #
    #    pars = {
    #      'loadBalancerUrl': 'unimportant',
    #      'jenkinsPass': 'placeholder',
    #      'sonarServerHost': 'notrelevant',
    #      'vpctype': 'k9-unit',
    #      'domain': 'k9.simoncomputing.com'
    #    }
    #    pars = HELM_PARAMS
    #    pars['sonarServerHost'] = rds.get('Endpoint', {}).get('Address', 'bad_rds_host')
    #
    #    try:
    #        ct = install_cluster_tools(pars, 'unit-cluster-tools')
    #        helm_uninstall('efk', 'unit-cluster-tools')
    #        helm_uninstall('grafana', 'unit-cluster-tools')
    #        helm_uninstall('prometheus', 'unit-cluster-tools')
    #        helm_uninstall('aws-load-balancer-controller', 'unit-cluster-tools')
    #        helm_uninstall('aws-storage', 'default')
    #        delete_deployment('cluster-autoscaler', 'kube-system')
    #        run_command('kubectl', 'delete', '-f', abs_path('yaml/autoscaler/infra.yml'))
    #        self.assertTrue(ct)
    #    except Exception as e:
    #        print(e)
    #    finally:
    #        delete_namespace('unit-cluster-tools')
    #        refresh_kubeconfig()
    #
    def test_jinja_xml(self):
        env = Environment(loader=FileSystemLoader(abs_path('../test/')))
        filename = write_templated_config('test-config.txt', env, {'replaceMe': 'hello!'})
        with open(filename) as f:
            out = f.readline()
            self.assertNotEqual(out.find('hello!'), -1)
        os.remove(filename)

    #
    #

    def test_create_cicd_no_clustername(self):
        cluster_conf = {
            'baseDomain': 'bogus'
        }
        with self.assertRaisesRegex(ValueError, 'The cluster-config.yml does not contain a clusterName.'):
            create_cicd(cluster_conf)

    def test_create_cicd_bogus_clustername(self):
        cluster_conf = {
            'clusterName': 'b0ogu5',
            'baseDomain': 'bogus'
        }
        with self.assertRaises(Exception):
            create_cicd(cluster_conf)
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    def test_create_cicd_no_base_domain(self):
        cluster_name = os.getenv('CLUSTER_NAME')
        cluster_conf = {
            'clusterName': cluster_name,
        }
        with self.assertRaisesRegex(ValueError, 'The cluster-config.yml does not contain a baseDomain.'):
            create_cicd(cluster_conf)
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))

    def test_create_cicd_bogus_base_domain(self):
        cluster_name = os.getenv('CLUSTER_NAME')
        cluster_conf = {
            'clusterName': cluster_name,
            'baseDomain': 'yes.bogus.domain.name'
        }
        with self.assertRaises(ValueError):
            create_cicd(cluster_conf)
        if os.getenv('automated') == '1':
            config.load_kube_config(config_file=os.environ.get("KUBECONFIG"))
