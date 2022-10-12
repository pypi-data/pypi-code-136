import argparse
import os
import subprocess

import botocore.exceptions
from aws import config, cluster, region, cfm, factsheet as aws_factsheet
from k9.cluster_init import create_cluster, delete_volumes, delete_logins_secret, create_cicd, delete_cicd, \
    configure_sonar_for_linking, configure_access_to_cluster, install_kibana_app_dashboards
from k9.helm import helm_exists, helm_uninstall
from k9.core import create_app_databases, run_command
from k9.templates import get_cfm_templates, create_project_template, generate_helm_values_files, \
    read_app_defaults, write_app_defaults, get_cfm_file, create_ecr_sync_values, create_prd_app_template
from k9.deploy import read_app_config, create_app_certs, deploy_service, \
    delete_all_service_deployments, delete_app_certs, deploy_ui, create_ecr, delete_ecr, \
    prepare_kubernetes_resources, delete_app_aws_secrets, delete_ui, \
    delete_service_application_databases, \
    create_promote_ui_stack, delete_promote_ui_stack, create_promote_service_stack, delete_promote_service_stack, \
    set_up_google_chat, create_ecr_sync_cron_job, delete_ecr_sync_cron_job, read_prd_app_config
from k9.jcasc import create_jenkins_pipeline, link_jenkins_sonarqube
from k9.factsheet import generate_application_factsheet

CLUSTER_CONFIG = 'cluster-config.yml'

def main():
    parser = argparse.ArgumentParser(prog='k9', description='k9-cli')

    parser.add_argument('command', type=str,
                        choices=['create', 'deploy', 'list', 'update', 'delete', 'link', 'get', 'configure'],
                        metavar='<command>',
                        help='the action you wish to take')

    parser.add_argument('resource', type=str,
                        choices=['project', 'templates', 'cluster', 'cicd',
                                 'eks-startstop', 'ui', 'service', 'monitoring',
                                 'cluster-factsheet', 'service-app-factsheet', 'ui-app-factsheet',
                                 'promote-ui', 'promote-service', 'ssm-template', 'access', 'ecr-sync',
                                 'prd-configs'],
                        metavar='<resource>',
                        help='the resource you wish to act on')

    parser.add_argument('-n', dest='clusterName',
                        help='cluster name to execute the command on')
    parser.add_argument('-kc', dest='keep_certs',
                        help='True or False to keep certificates when calling delete cluster')
    parser.add_argument('-env', dest='env_name',
                        help='environment name to execute the command on')
    parser.add_argument('-bd', dest='baseDomain',
                        help='base domain associated with the cluster')
    parser.add_argument('-cicd', dest='isCicd',
                        help='True or False whether the cluster is used for cicd purposes')
    parser.add_argument('-prd', dest='isPrd', action='store_true',
                        help='True or False whether the deployment is for the production environment')

    args = parser.parse_args()

    exe = CommandExecution()
    exe.solve_for(args.command, args.resource, clusterName=args.clusterName,
                  keep_certs=args.keep_certs, env_name=args.env_name, baseDomain=args.baseDomain,
                  isCicd=args.isCicd, isPrd=args.isPrd)


def alb_controller_cleanup(vpc_id: str):
    """
    Deletes the load balancer and target groups created by the ALB controller deployment.
    This is necessary because they are not part of the CloudFormation stacks and will prevent the VPC stack from
    being deleted.

    :param vpc_id: The id of the VPC to clean up in.
    """

    load_balancers = region.get_elbv2().describe_load_balancers()
    # search for load balancer in this cluster's vpc
    for lb in load_balancers['LoadBalancers']:
        if lb['VpcId'] == vpc_id:
            arn = lb['LoadBalancerArn']
            print('deleting load balancer: ', arn)
            region.get_elbv2().delete_load_balancer(
                LoadBalancerArn=arn
            )
            break

    # search for and delete target groups
    target_groups = region.get_elbv2().describe_target_groups()
    for tg in target_groups['TargetGroups']:
        if tg['VpcId'] == vpc_id:
            arn = tg['TargetGroupArn']
            try:
                region.get_elbv2().delete_target_group(
                    TargetGroupArn=arn
                )
            except botocore.exceptions.ClientError as e:
                # ignore failed delete, ALB controller may clean it up
                print(f'Failed to delete target group {arn}')
                print(e.response)


def get_cluster_config(cluster_dir: str):
    """
    Reads cluster-config.yml in the directory provided.

    :param cluster_dir: directory containing cluster-config.yml

    :returns: dictionary version of cluster-config using atomic-cloud create_config method
    """
    conf_path = os.path.join(cluster_dir, CLUSTER_CONFIG)
    if not os.path.exists(conf_path):
        print('The cluster-config.yml is not found. '
              'Run "k9 create templates" to get default cloudformation templates.')
        exit(0)

    return config.create_config(conf_path)


def read_keep_certs(kc):
    """
    Returns boolean True or False if certificates should be deleted.

    :param kc: Value passed in from command line after -kc flag, or None

    :returns: Boolean value whether to keep certificates.
    """
    if kc is None:
        # no value provided, prompt user
        keep_certs = 'deletecerts' != input(
            'Input "deletecerts" to delete certificates. Enter anything else to keep. '
            'If deleted, these must be manually approved when re-making the stack\n')
    elif type(kc) == bool:
        keep_certs = kc
    else:
        # true only if True/true given
        keep_certs = kc.lower() == 'true'

    print("Keeping certs" if keep_certs else "Deleting certs")
    return keep_certs


class CommandExecution:
    """
    Class that holds cli commands. Takes commands in the form 'k9 command resource'
    and calls function name command_resource()
    """

    def solve_for(self, command: str, resource: str, **kwargs):
        # turn command-name into command_name
        resource = resource.replace('-', '_')
        do = f'{command}_{resource}'

        if hasattr(self, do) and callable(getattr(self, do)):
            func = getattr(self, do)
            func(**kwargs)
        else:
            print(f'Not supported: {do}')

    def create_project(*args, **kwargs):
        """
        The first command that is run when using k9. Creates the k9 directory and subdirectory structures.
        """
        cwd = os.getcwd()
        print('Creating project...')
        create_project_template(cwd)
        print('Project created.')

    def create_templates(*args, **kwargs):
        """
        Copies default config and CloudFormation files from atomic-cloud into the current directory,
        skipping files that already exist.
        """
        cwd = os.getcwd()
        print('Creating templates...')
        get_cfm_templates(cwd)
        print('Templates created.')

    def create_cluster(*args, **kwargs):
        """
        Creates a cluster based on the k9-config and CloudFormation files in the current directory.
        If k9-config.yml is not present, it will prompt the user to run "k9 create templates"

        If there is an error when creating stacks, you must call delete cluster to clean up all stacks.
        """
        cwd = os.getcwd()
        # create config object from cluster-config.yml
        conf = get_cluster_config(cwd)
        get_cfm_templates(cwd)

        print('Creating cluster. This may take around an hour.')
        print('Warning: Running k9 create cluster for multiple clusters concurrently may cause issues when configuring'
              ' kubernetes resources after AWS stacks have been created. Any issues can likely be resolved by running'
              'create cluster again, independently.')
        create_cluster(conf, cwd)
        base_domain = conf['baseDomain']
        is_cicd = conf['isCicd']
        aws_factsheet.generate_cluster_factsheet(f'{conf["clusterName"]}-cluster', base_domain, is_cicd)
        print('Cluster creation process complete.')

    def deploy_service(*args, **kwargs):
        """
        Deploys the service application using the information in app-config.yml from the current directory, and helm
        values.yml files found in values/ in the current directory. Creates a values.yml file in values/ directory then
        reads it when calling helm install.
        """
        # Flag to determine if deployment is strictly for production
        is_prd = kwargs.get('isPrd', None)

        cwd = os.getcwd()
        app_config = read_prd_app_config(cwd) if is_prd else read_app_config(cwd)

        # create certs if needed
        print('Creating application certificates...')
        create_app_certs(app_config, False, True)
        print('Application certificates created. Creating ECR...')
        create_ecr(app_config['appName'])
        print('ECR created. Creating application databases...')
        create_app_databases(app_config)
        print('Application databases created. Preparing kubernetes resources...')
        prepare_kubernetes_resources(app_config)
        print('Kubernetes resources created. Generating helm values files...')
        defaults = read_app_defaults(os.path.dirname(cwd))
        generate_helm_values_files(app_dir=cwd, defaults=defaults)
        print('Helm values files generated. Deploying service...')
        deploy_service(app_config, cwd)

        # Do not want to create a Google Chat credential or Jenkins pipeline if the deployment is strictly for production
        if is_prd:
            print('Deploying service')
            print('Creating application production factsheet...')
            generate_application_factsheet(app_config=app_config, is_service=True, is_prd=True)
        else:
            print('Deploying service. Setting up Google Chat credential...')
            result = set_up_google_chat(app_config=app_config, defaults=defaults)

            if not result:
                print(
                    'Google Chat credential was not created in Jenkins. This will need to be done manually if applicable.')

            print('Creating service Jenkins pipeline...')
            create_jenkins_pipeline(app_config, defaults, is_service=True)
            print('Service Jenkins pipeline successfully created. Creating service promotion stack...')
            create_promote_service_stack(cwd)
            print('Service promotion stack successfully created. Creating application factsheet...')
            generate_application_factsheet(app_config=app_config, is_service=True, is_prd=False)

        print('Application factsheet created. Installing kibana dashboards...')
        install_kibana_app_dashboards(cwd)
        print('Service deployment completed.')

    def deploy_ui(*args, **kwargs):
        """
        Deploys the ui application using the information in app-config.yml from the current directory.
        """
        # Flag to determine if deployment is strictly for production
        is_prd = kwargs.get('isPrd', None)

        cwd = os.getcwd()
        app_config = read_prd_app_config(cwd) if is_prd else read_app_config(cwd)

        # Not request to create certificate here because without approval, deploy ui cannot continue
        # deploy_ui includes certificate request and wait to be approved
        print('Deploying UI...')
        deploy_ui(app_config=app_config, app_dir=cwd)
        print('UI deployed.')
        defaults = read_app_defaults(os.path.dirname(cwd))

        # Do not want to create a Google Chat credential orJenkins pipeline if the deployment is strictly for production
        if is_prd:
            print('Deploying UI')
            print('Creating application production factsheet...')
            generate_application_factsheet(app_config=app_config, is_service=False, is_prd=True)
        else:
            print('Deploying UI. Setting up Google Chat credential...')
            result = set_up_google_chat(app_config=app_config, defaults=defaults)
            if not result:
                print(
                    'Google Chat credential was not created in Jenkins. This will need to be done manually if applicable.')
            print('Creating UI Jenkins pipeline...')
            create_jenkins_pipeline(app_config, defaults, is_service=False)
            print('UI Jenkins pipeline successfully created. Creating ui promotion stack...')
            create_promote_ui_stack(cwd)
            print('UI promotion stack successfully created. Creating application factsheet...')
            generate_application_factsheet(app_config=app_config, is_service=False, is_prd=False)

        print('Application factsheet created. UI deployment completed.')

    def list_cluster(*args, **kwargs):
        print('TODO: list_cluster coming soon')

    def delete_cluster(*args, **kwargs):
        """
        Deletes a cluster with the given clusterName. Prompts user to delete certificates.

        Usage:
        'k9 delete cluster -n clusterName'

        'k9 delete cluster -n clusterName -kc true'
        """
        assert kwargs['clusterName'], 'delete_cluster() requires clusterName (-n clusterName)'
        cluster_name = kwargs['clusterName']

        kc = kwargs.get('keep_certs', None)
        keep_certs = read_keep_certs(kc)

        # delete standard apps and load balancer controller
        print('Deleting standard apps...')
        try:
            run_command("aws", "eks", "update-kubeconfig", "--name", f"{cluster_name}-cluster")
            CommandExecution().delete_monitoring()
        except subprocess.CalledProcessError as e:
            if '(ResourceNotFoundException) when calling the DescribeCluster operation' not in str(e.stderr):
                raise e
            else:
                print('EKS Cluster not found, continuing with AWS cleanup.')

        # delete AWS resources
        print('Deleting AWS resources...')
        delete_logins_secret(cluster_name)
        delete_volumes(cluster_name)
        try:
            vpc_id = cfm.get_output(cluster_name + '-01-vpc', 'VPC')
        except TypeError:
            vpc_id = None
        alb_controller_cleanup(vpc_id)

        # delete cluster stacks
        print('AWS resources deleted. Deleting cluster stacks...')
        try:
            cluster.delete_cluster(cluster_name, keep_certs=keep_certs)
        except TypeError:
            # delete_cluster fails if VPC already deleted, so try again to delete certs if needed
            if not keep_certs:
                cluster.delete_certificates(cluster_name)

        print('Cluster stacks deleted')

        # try ALB cleanup again
        alb_controller_cleanup(vpc_id)

    def delete_monitoring(*args, **kwargs):
        """
        Deletes EFK, Prometheus, Grafana default deployments from the cluster.
        Useful if you wish to use different helm charts for these apps.
        """
        if helm_exists('efk', 'logging'):
            helm_uninstall('efk', 'logging')
        if helm_exists('prometheus', 'monitoring'):
            helm_uninstall('prometheus', 'monitoring')
        if helm_exists('grafana', 'monitoring'):
            helm_uninstall('grafana', 'monitoring')

        print('\nAll standard apps deleted successfully.\n')

    def create_cicd(*args, **kwargs):
        """
        Installs Jenkins and SonarQube for the cluster defined by the cluster-config.yml in the path.
        Useful for setting up the cicd process for deployment.
        """
        cwd = os.getcwd()
        conf = get_cluster_config(cwd)

        # find apps dir with defaults.yml
        k9_dir = os.path.dirname(cwd)
        apps_dir = os.path.join(k9_dir, 'apps')
        # edit defaults.yml
        defaults = read_app_defaults(apps_dir)
        defaults['jenkins']['jenkinsUrl'] = f'https://jenkins.{conf["baseDomain"]}'
        defaults['jenkins']['clusterName'] = conf['clusterName']
        write_app_defaults(apps_dir, defaults)

        print('Creating cicd...')
        create_cicd(conf)
        print('Cicd created.')

    def delete_cicd(*args, **kwargs):
        cwd = os.getcwd()
        conf = get_cluster_config(cwd)
        print('Deleting cicd...')
        delete_cicd(conf)
        print('Cicd deleted.')

    def create_cluster_factsheet(*args, **kwargs):
        """
        Creates a cluster factsheet based on either the cluster-config file in the current directory or the user input

        Usage:
        'k9 create cluster-factsheet -n clusterName -bd base_domain -cicd is_cicd'
        """
        cwd = os.getcwd()
        conf = None
        conf_path = os.path.join(cwd, CLUSTER_CONFIG)
        if not os.path.exists(conf_path):
            print(
                'The cluster-config.yml file does not exist in the current directory. Relying solely on user input...')
        else:
            conf = config.create_config(conf_path)
        assert kwargs.get('clusterName', None) or conf.get('clusterName',
                                                           None), 'create_cluster_factsheet() requires clusterName (-n clusterName)'
        assert kwargs.get('baseDomain', None) or conf.get('baseDomain',
                                                          None), 'create_cluster_factsheet() requires baseDomain (-bd baseDomain)'
        assert kwargs.get('isCicd', None) or conf.get('isCicd',
                                                      None), 'create_cluster_factsheet() requires whether the cluster is used for cicd (-cicd isCicd)'
        cluster_name = kwargs.get('clusterName', None) or conf.get('clusterName')
        base_domain = kwargs.get('baseDomain', None) or conf.get('baseDomain')
        is_cicd = kwargs.get('isCicd', None) or conf.get('isCicd')
        if type(is_cicd) != bool:
            is_cicd = is_cicd.lower() == 'true'
        print('Generating factsheet...')
        aws_factsheet.generate_cluster_factsheet(f'{cluster_name}-cluster', base_domain, is_cicd)
        print('Factsheet generated.')

    def create_service_app_factsheet(*args, **kwargs):
        """
        Creates a service application factsheet based on the app-config file in the current directory

        Usage:
        'k9 create service-app-factsheet'
        """
        # Flag to determine if factsheet is strictly for production
        is_prd = kwargs.get('isPrd', None)

        cwd = os.getcwd()

        print('Generating service application factsheet...')
        if is_prd:
            generate_application_factsheet(app_config=read_prd_app_config(cwd), is_service=True, is_prd=True)
        else:
            generate_application_factsheet(app_config=read_app_config(cwd), is_service=True, is_prd=False)
        print('Service application factsheet generated.')

    def create_ui_app_factsheet(*args, **kwargs):
        """
        Creates a ui application factsheet based on the app-config file in the current directory

        Usage:
        'k9 create ui-app-factsheet'
        """
        # Flag to determine if factsheet is strictly for production
        is_prd = kwargs.get('isPrd', None)

        cwd = os.getcwd()

        print('Generating ui application factsheet...')
        if is_prd:
            generate_application_factsheet(app_config=read_prd_app_config(cwd), is_service=False, is_prd=True)
        else:
            generate_application_factsheet(app_config=read_app_config(cwd), is_service=False, is_prd=False)
        print('Ui application factsheet generated.')

    def link_cicd(*args, **kwargs):
        cwd = os.getcwd()
        conf_path = os.path.join(cwd, CLUSTER_CONFIG)
        if not os.path.exists(conf_path):
            print(
                'The cluster-config.yml is not found. Run "k9 create templates" to get default cloudformation templates.')
            return

        conf = config.create_config(conf_path)
        cluster_name = conf.get('clusterName')
        base_domain = conf.get('baseDomain')
        user_token = configure_sonar_for_linking(conf)
        print('Linking SonarQube and Jenkins...')
        result = link_jenkins_sonarqube(cluster_name=cluster_name, base_domain=base_domain,
                                        secret_name='jenkins-sonarqube-access-token', secret=user_token)
        if not result:
            raise ValueError(
                "ERROR: SonarQube and Jenkins were not able to be linked. This will need to be done manually.")
        else:
            print('Successfully linked SonarQube and Jenkins.')

    def delete_service(*args, **kwargs):
        # Flag to determine if deletion is strictly for production
        is_prd = kwargs.get('isPrd', None)

        cwd = os.getcwd()

        kc = kwargs.get('keep_certs', None)
        keep_certs = read_keep_certs(kc)

        if is_prd:
            print('Deleting service deployments...')
            delete_all_service_deployments(cwd, is_prd=True)
            print('Service deployments deleted. Deleting ECR...')
            delete_ecr(read_prd_app_config(cwd)['appName'])
            print('ECR deleted.')
            if not keep_certs:
                print('Deleting service certificates')
                delete_app_certs(cwd, False, True, is_prd=True)
            print('Deleting application secrets in AWS...')
            delete_app_aws_secrets(read_prd_app_config(cwd, True))
            print('Application secrets deleted. Deleting application databases...')
            delete_service_application_databases(read_prd_app_config(cwd))
            print('Application databases deleted. Deleting service promotion stack...')
            delete_promote_service_stack(read_prd_app_config(cwd, True)['appName'])
            print('Service promotion stack deleted.')
        else:
            print('Deleting service deployments...')
            delete_all_service_deployments(cwd, is_prd=False)
            print('Service deployments deleted. Deleting ECR...')
            delete_ecr(read_app_config(cwd)['appName'])
            print('ECR deleted.')
            if not keep_certs:
                print('Deleting service certificates')
                delete_app_certs(cwd, False, True, is_prd=False)
            print('Deleting application secrets in AWS...')
            delete_app_aws_secrets(read_app_config(cwd, True))
            print('Application secrets deleted. Deleting application databases...')
            delete_service_application_databases(read_app_config(cwd))
            print('Application databases deleted. Deleting service promotion stack...')
            delete_promote_service_stack(read_app_config(cwd, True)['appName'])
            print('Service promotion stack deleted.')

    def delete_ui(*args, **kwargs):
        """
        Deletes UI hosting per environment if specified. Otherwise deleting all environments.

        Usage:
        'k9 delete ui [-env envName]'
        """
        # Flag to determine if deletion is strictly for production
        is_prd = kwargs.get('isPrd', None)

        kc = kwargs.get('keep_certs', None)
        keep_certs = read_keep_certs(kc)

        env_name = kwargs.get('env_name', None)

        cwd = os.getcwd()
        app_config = read_prd_app_config(cwd, True) if is_prd else read_app_config(cwd, True)

        # ask user to confirm the app name to be deleted
        deleting_env = 'ALL environments' if env_name is None else f'{env_name} environment'
        entered_app_name = input(f'Enter application name to confirm the UI hosting deletion for {deleting_env}:')

        # if entered app name does not match to the appName on appConfig, exit
        if entered_app_name != app_config['appName']:
            print('Application name you entered does not match with appName in the appConfig')
            exit()

        print(f'Deleting UI for application {entered_app_name} for {deleting_env} and keep_certs={keep_certs}...')
        delete_ui(app_config, env_name, keep_certs)
        print(
            f'UI deleted for application {entered_app_name} for {deleting_env} and keep_certs={keep_certs}. Deleting UI promotion stack...')
        delete_promote_ui_stack(app_config['appName'])
        print('UI promotion stack deleted.')

    def create_eks_startstop(*args, **kwargs):
        print('Creating eks-startstop automation.')
        cluster.create_eks_startstop()
        print('Automation created. Tag clusters with "eks-autostart" and "eks-autostop" and the desired values to scale'
              'the clusters to. Stop values may go to 0 to turn clusters off.')

    def delete_eks_startstop(*args, **kwargs):
        print('Deleting eks-startstop automation.')
        cluster.delete_eks_startstop()
        print('Automation deleted')

    def create_promote_ui(*args, **kwargs):
        print('Creating promote-ui stack')
        create_promote_ui_stack(os.getcwd())
        print('promote-ui stack created')

    def delete_promote_ui(*args, **kwargs):
        print('deleting promote-ui stack')
        cwd = os.getcwd()
        app_config = read_app_config(cwd)
        delete_promote_ui_stack(app_config['appName'])
        print('promote-ui stack deleted')

    def create_promote_service(*args, **kwargs):
        print('Creating promote-service stack')
        create_promote_service_stack(os.getcwd())
        print('promote-service service created')

    def delete_promote_service(*args, **kwargs):
        print('deleting promote-service stack')
        cwd = os.getcwd()
        app_config = read_app_config(cwd)
        delete_promote_service_stack(app_config['appName'])
        print('promote-service stack deleted')

    def get_ssm_template(*args, **kwargs):
        cwd = os.getcwd()
        get_cfm_file('ssm-access.yml', cwd)
        print(f'Copied ssm-access.yml to f{cwd}. Use this template to create a SSM instance to run k9 on without '
              f'needing to generate aws cli long-term access keys.')
        print('Check https://k9.docs.simoncomputing.com/ssm_access.html for more information.')

    def configure_access(*args, **kwargs):
        assert kwargs['clusterName'], 'configure_access() requires clusterName (-n clusterName)'
        cluster_name = kwargs.get('clusterName', None)
        return configure_access_to_cluster(cluster_name)

    def create_ecr_sync(*args, **kwargs):
        cwd = os.getcwd()
        sync_values_path = os.path.join(cwd, 'ecr-sync-values.yml')
        if not os.path.exists(sync_values_path):
            create_ecr_sync_values(cwd, cluster_name=kwargs.get('clusterName'))
            print('Created ecr-sync-values.yml. Edit then re-run "k9 create ecr-sync"')
            return
        create_ecr_sync_cron_job(cwd)

    def create_prd_configs(*args, **kwargs):
        cwd = os.getcwd()

        # Create prd_app_config file
        create_prd_app_template(cwd)
        print('Created prd-app-config.yml.')

        # Create ecr_sync_values
        create_ecr_sync_values(cwd, cluster_name=kwargs.get('clusterName'))
        print('Created ecr-sync-values.yml.')

    def delete_ecr_sync(*args, **kwargs):
        cwd = os.getcwd()
        delete_ecr_sync_cron_job(cwd)


if __name__ == '__main__':
    main()
