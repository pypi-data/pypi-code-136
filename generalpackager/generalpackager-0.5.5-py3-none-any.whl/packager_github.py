from git import Git

from github import Github

from generalpackager import PACKAGER_GITHUB_API


class _PackagerGitHub:
    """ Sync metadata. """
    def __init__(self):
        self.commit_sha = "master"

    def sync_github_metadata(self):
        """ Sync GitHub with local metadata.

            :param generalpackager.Packager self: """
        assert self.github.set_website(self.pypi.url).ok
        assert self.github.set_description(self.localrepo.metadata.description).ok
        assert self.github.set_topics(*self.get_topics()).ok

    # These methods below should maybe be in LocalRepo

    def commit_and_push(self, message=None, tag=False):
        """ Commit and push this local repo to GitHub.
            Return short sha1 of pushed commit.

            :param generalpackager.Packager self:
            :param message:
            :param tag: """
        repo = self.localrepo.gitpython_repo
        repo.git.add(A=True)
        # Todo: commit-hook failed for auto commit "not a valid Win32 application"
        repo.index.commit(message=str(message) or "Automatic commit.")
        remote = repo.remote()
        remote.set_url(f"https://Mandera:{PACKAGER_GITHUB_API}@github.com/{self.github.owner}/{self.name}.git")

        if tag:
            tag_ref = repo.create_tag(f"v{self.localrepo.metadata.version}", force=True)
            remote.push(refspec=tag_ref)
        try:
            """ Todo: Fetch commit sha locally before pushing, possibly generate sha before commit.
                
                import git
                repo = git.Repo(search_parent_directories=True)
                sha = repo.head.object.hexsha """
            self.commit_sha = remote.push()[0].summary.split("..")[1].rstrip()
            # self.commit_sha = remote.push("head")[0].summary.split("..")[1].rstrip()
        except OSError:  # Just suppressing weird invalid handle error
            pass
        return self.commit_sha

    def enable_vcs_operations(self):
        """ :param generalpackager.Packager self: """
        Git(str(self.path)).init()
        # self.localrepo.get_repo().git.add(A=True)
        # repo = self.localrepo.get_repo()

    def create_github_repo(self):
        """ :param generalpackager.Packager self: """
        g = Github(PACKAGER_GITHUB_API.value)

        manderageneral = g.get_organization("ManderaGeneral")

        repo = manderageneral.create_repo(
            name=self.name,
            private=self.localrepo.metadata.private,
        )
        repo = manderageneral.get_repo(self.name)
        # repo.create_git_ref()
        # print(repo.master_branch)
        # print(list(repo.get_branches()))

    def create_master_branch(self):
        """ :param generalpackager.Packager self: """
        repo = self.localrepo.gitpython_repo
        # Create remote somehow first
        print(repo.remote().push("head"))

    # Todo: Setup env vars for project.






