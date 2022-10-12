from install_dependencies import install_dependencies

def test_install_dependencies():
    install_dependencies('get_repository_path', 'repo_utils')
    install_dependencies(__file__, 'repo_utils')
