import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List
from typing import Optional

import pygit2
from pathvalidate import sanitize_filepath
from pygit2 import RemoteCallbacks

from ..Exceptions import ChangesNotCommitedError
from ..Exceptions import MergeConflict
from ..Exceptions import NoChangesToCommitError
from ..Exceptions import NoRemoteDefined
from ..Exceptions import ProjectValidationError
from ..migration import getLatestRevision
from ..tuples.git_commit_tuple import GitCommitTuple


logger = logging.getLogger(__name__)

ATTUNE_WORKING_BRANCH = "__working__"

_gitignore = """
# Ignore files in directories named unversioned
**/unversioned/**
**/.DS_Store
"""


def makeRef(branch: str) -> str:
    return "refs/heads/%s" % branch


class PathNameInvalidException(Exception):
    pass


class GitLibMixin:
    defaultCommitter = pygit2.Signature(
        "ServerTribe Attune", "attune@servertribe.com"
    )

    def __init__(self, projectPath: Path):
        self.projectPath = projectPath
        self.__committer = self.defaultCommitter
        self._repo = None
        self.__indexInitialised = False
        # TODO: What if the class was loaded before a raw commit was made?
        self.__isIndexDirty = False

        # Information required by the on-error context manager
        self._workingId: Optional[str] = None

        try:
            self.loadGitRepo()
        except pygit2.GitError:
            self.initGitRepo()
            self.loadGitRepo()

    @property
    def _repoPath(self) -> Path:
        return self.projectPath / "git_storage"

    @property
    def _checkedOutBranchRef(self) -> str:
        return self._repo.head.raw_name

    def loadGitRepo(self):
        self._repo = pygit2.Repository(self._repoPath.as_posix())
        if self._repo.is_bare:
            raise ValueError(f"{self._repoPath} points to a Git Bare Repo")

    def initGitRepo(self):
        # Create target repo
        self._repo = pygit2.init_repository(self._repoPath.as_posix())
        self.__indexInitialised = True
        logger.info(f"Create Git repository at {self._repoPath}")
        self.__createInitialCommit()

    def __createInitialCommit(self):
        # We cannot use the public `writeMetadata` method here because the
        # branches and references to have not been set up yet
        self.__writeProjectMetadata()
        self.__writeGitIgnore()
        self.__createCommit(
            "HEAD", "Create default metadata.json", [], self.__index
        )

    def __writeProjectMetadata(self):
        # Create default metadata.json
        name = self.project.name
        data = json.dumps(
            {"revision": getLatestRevision(), "name": name},
            indent=4,
            sort_keys=True,
            separators=(", ", ": "),
        ).encode()
        path = "metadata.json"
        # Write the file, *without* preparing the working branch
        self.__index.add(
            pygit2.IndexEntry(
                path, self._repo.create_blob(data), pygit2.GIT_FILEMODE_BLOB
            )
        )
        self.__isIndexDirty = True

    def __writeGitIgnore(self):
        data = _gitignore.encode()
        path = ".gitignore"
        # Write the file, with out preparing the working branch
        self.__index.add(
            pygit2.IndexEntry(
                path, self._repo.create_blob(data), pygit2.GIT_FILEMODE_BLOB
            )
        )
        self.__isIndexDirty = True

    @property
    def metadata(self):
        tree = self.__workingTree
        data = (tree / "metadata.json").data
        metadataStr = data.decode()
        metadata = json.loads(metadataStr)
        return metadata

    def writeMetadata(self, metadata):
        oid = self._repo.create_blob(
            json.dumps(
                metadata,
                indent=4,
                sort_keys=True,
                separators=(", ", ": "),
            ).encode()
        )
        self.prepareWorkingBranch()
        self.__index.add(
            pygit2.IndexEntry("metadata.json", oid, pygit2.GIT_FILEMODE_BLOB)
        )
        self.__isIndexDirty = True

    @classmethod
    def cloneGitRepo(
        cls,
        projectPath: Path,
        url: str,
        username: str = None,
        password: str = None,
    ):
        class RemoteCallback(RemoteCallbacks):
            def credentials(self, url, username_from_url, allowed_types):
                if username is None and password is None:
                    return super().credentials(
                        url, username_from_url, allowed_types
                    )
                elif password is None:
                    cred = pygit2.Username(username)
                else:
                    cred = pygit2.UserPass(username, password)
                return cred

            def certificate_check(self, certificate, valid, host):
                # Return whatever the TLS/SSH library thinks about the cert
                return True

        pygit2.clone_repository(
            url,
            projectPath.as_posix(),
            bare=False,
            callbacks=RemoteCallback(),
        )

    def _writeFile(self, path: str, data: bytes, mode=pygit2.GIT_FILEMODE_BLOB):
        if path != sanitize_filepath(path):
            raise PathNameInvalidException(
                "Path %s is not valid, please " "sanitize it first" % path
            )

        oid = self._repo.create_blob(data)
        self.prepareWorkingBranch()
        self.__index.add(pygit2.IndexEntry(Path(path).as_posix(), oid, mode))
        self.__isIndexDirty = True

    def _moveDirectory(self, fromPath: Path, toPath: Path):
        if fromPath == toPath:
            raise Exception("The source and destination paths are the same")

        fromTree = self._getTree(fromPath)

        self.prepareWorkingBranch()

        def recurse(fromParentPath, toParentPath, tree):
            for item in tree:
                fromItemPath = fromParentPath / item.name
                toItemPath = toParentPath / item.name
                # A child tree is a directory
                if isinstance(item, pygit2.Tree):
                    recurse(fromItemPath, toItemPath, item)
                    continue

                # Otherwise it's a blob, move it
                assert isinstance(
                    item, pygit2.Object
                ), "item is not a pygit2.Object"
                self.__index.add(
                    pygit2.IndexEntry(
                        toItemPath.as_posix(), item.oid, item.filemode
                    )
                )
                self.__index.remove(fromItemPath.as_posix())

        recurse(fromPath, toPath, fromTree)
        self.__isIndexDirty = True

    def _moveFile(self, fromPath: Path, toPath: Path):
        if fromPath == toPath:
            raise Exception("The source and destination paths are the same")

        fromTree = self._getTree(fromPath.parent)

        self.prepareWorkingBranch()

        blob = fromTree / fromPath.name
        assert isinstance(blob, pygit2.Object), "blob is not a pygit2.Object"

        self.__index.add(
            pygit2.IndexEntry(toPath.as_posix(), blob.oid, blob.filemode)
        )
        self.__index.remove(fromPath.as_posix())
        self.__isIndexDirty = True

    def _deleteDirectory(self, path: Path):
        try:
            startTree = self._getTree(path)
        except FileNotFoundError:
            # It's already done.
            return

        self.prepareWorkingBranch()

        def recurse(parentPath, tree):
            for item in tree:
                itemPath = parentPath / item.name
                # A child tree is a directory
                if isinstance(item, pygit2.Tree):
                    recurse(itemPath, item)
                    continue

                # Otherwise, it's a blob, move it
                assert isinstance(
                    item, pygit2.Object
                ), "item is not a pygit2.Object"
                self.__index.remove(itemPath.as_posix())

        recurse(path, startTree)
        self.__isIndexDirty = True

    def _deleteFile(self, path: Path):
        tree = self._getTree(path.parent)
        self.prepareWorkingBranch()

        blob = tree / path.name
        assert isinstance(blob, pygit2.Object), "blob is not a pygit2.Object"

        self.__index.remove(path.as_posix())
        self.__isIndexDirty = True

    def _readFile(self, path: Path) -> bytes:
        tree = self._getTree(path.parent)

        if path.name in tree:
            fileObject = tree / path.name
            return fileObject.data
        else:
            raise FileNotFoundError()

    @property
    def isDirty(self) -> bool:
        return self.__isIndexDirty

    def commit(self, msg: str):
        descendentCommit = next(
            self._repo.walk(self.__workingBranch.target), None
        )
        if descendentCommit is not None:
            descendents = [descendentCommit.id]
        else:
            descendents = []
        self.__createCommit(
            self.__workingBranch.name, msg, descendents, self.__index
        )

    def __createCommit(
        self, targetName: str, msg: str, descendents: list[str], index
    ) -> str:

        tree = index.write_tree()
        author = self.__committer if self.__committer else self.defaultCommitter

        self.__isIndexDirty = False

        return self._repo.create_commit(
            targetName,
            author,
            author,
            msg,
            tree,
            descendents,
        )

    @property
    def __index(self) -> pygit2.Index:
        if self.__indexInitialised:
            return self._repo.index

        # Else, initialise the index
        if ATTUNE_WORKING_BRANCH in list(self._repo.branches):
            self._repo.index.read_tree(
                tree=self._repo.revparse_single(
                    makeRef(ATTUNE_WORKING_BRANCH)
                ).tree
            )
        else:
            self._repo.index.read_tree(
                tree=self._repo.revparse_single(self._checkedOutBranchRef).tree
            )
        self.__indexInitialised = True

        return self._repo.index

    def prepareWorkingBranch(self):
        if ATTUNE_WORKING_BRANCH not in list(self._repo.branches):
            commit = next(self._repo.walk(self.__checkedOutBranch.target), None)
            self._repo.create_branch(ATTUNE_WORKING_BRANCH, commit)
            self.__indexInitialised = False

    @property
    def __workingBranch(self) -> pygit2.Branch:
        """Working Branch

        Accessing the working branch causes creation of __working__ branch if
        it does not already exist.

        """
        self.prepareWorkingBranch()
        return self._repo.references[makeRef(ATTUNE_WORKING_BRANCH)]

    @property
    def __checkedOutBranch(self) -> pygit2.Branch:
        return self._repo.references[self._checkedOutBranchRef]

    @property
    def __workingTree(self):
        branch = self._checkedOutBranchRef
        if ATTUNE_WORKING_BRANCH in list(self._repo.branches):
            branch = makeRef(ATTUNE_WORKING_BRANCH)

        return self._repo.revparse_single(branch).tree

    def _getTree(self, path: Path) -> pygit2.Tree:
        # We will read objects as they are at the working branch
        tree = self.__workingTree
        climbedPath = ""
        for pathComponent in path.as_posix().split("/"):
            climbedPath += f"/{pathComponent}"
            if pathComponent in tree:
                tree = tree / pathComponent
            else:
                raise FileNotFoundError(f"Path {pathComponent} does not exist")
        return tree

    def setCommitterSignature(self, name: str, email: str) -> None:
        self.__committer = pygit2.Signature(name, email)

    def allLocalBranches(self) -> List[str]:
        return [
            str(branch)
            for branch in self._repo.branches.local
            if not str(branch) == ATTUNE_WORKING_BRANCH
        ]

    def allRemoteBranches(self) -> List[str]:
        return [str(branch) for branch in self._repo.branches.remote]

    def allBranches(self) -> List[str]:
        return [str(branch) for branch in self._repo.branches]

    def allRemotes(self) -> List[tuple[str, str]]:
        return [(remote.name, remote.url) for remote in self._repo.remotes]

    def checkoutBranch(self, branchName: str) -> None:
        if branchName == ATTUNE_WORKING_BRANCH:
            raise ValueError(
                "Cannot checkout the reserved Attune branch %s"
                % ATTUNE_WORKING_BRANCH
            )

        if self.isDirty:
            raise ChangesNotCommitedError()

        # Check if there are changes waiting to be squashed and merged
        if ATTUNE_WORKING_BRANCH in list(self._repo.branches):
            workingBranch = self.__workingBranch
            checkedOutBranch = self.__checkedOutBranch
            if workingBranch.target != checkedOutBranch.target:
                raise ChangesNotCommitedError()

            # Delete the working branch
            workingBranch.delete()

        if branchName in self.allLocalBranches():
            # Checkout existing branch
            self._repo.checkout(makeRef(branchName))
        else:
            # Create and checkout new branch
            checkedBranch = self.__checkedOutBranch
            commit = next(self._repo.walk(checkedBranch.target), None)
            self._repo.create_branch(branchName, commit)
            self._repo.checkout(makeRef(branchName))

    def squashAndMergeWorking(self, mergeCommitMessage: str) -> None:
        if self._workingId is not None:
            raise Exception(
                "Cannot squash and commit when modifying the working branch"
            )

        working = self.__workingBranch
        checkedOut = self.__checkedOutBranch
        checkedOutBranchRef = checkedOut.name

        if self.isDirty:
            raise ChangesNotCommitedError()

        if working.target == checkedOut.target:
            raise NoChangesToCommitError("There are no changes to commit")

        checkedLastCommit = next(self._repo.walk(checkedOut.target), None)

        # Walk the commits till we find the previous common point
        commitsOnWorking = 0
        for c in self._repo.walk(working.target):
            if c.id == checkedLastCommit.id:
                break
            commitsOnWorking += 1

        self._repo.checkout(makeRef(ATTUNE_WORKING_BRANCH))
        # Create squash commit
        # Do a soft reset to the beginning of working branch
        self._repo.reset(checkedLastCommit.id, pygit2.GIT_RESET_SOFT)
        # Create a commit. This will squash the previous `commitsOnChecked`
        # into one

        squashCommitOid = self.__createCommit(
            makeRef(ATTUNE_WORKING_BRANCH),
            mergeCommitMessage,
            [checkedLastCommit.id],
            self.__index,
        )

        """
        Because we write files directly to the Git object database and
        never to the working directory, running a git status at this point
        will show that the files were deleted because they are not present
        in the working directory. This does not allow us to merge later as
        the repo is in a dirty state. Doing a hard reset, resets the index
        and restores the state of the working directory (in our case,
        it recreates the files that it things were deleted). This is done
        in C code and should be faster than writing files to the working
        directory in Python and then `add commit`ing them.
        """
        self._repo.reset(squashCommitOid, pygit2.GIT_RESET_HARD)

        # Reload the reference to the working branch
        working = self.__workingBranch

        self._repo.checkout(checkedOutBranchRef)
        checkedOut.set_target(working.target)
        self._repo.reset(checkedOut.target, pygit2.GIT_RESET_HARD)

        # Delete the working branch. It will be recreated if there is a new
        # commit
        working.delete()

    def getCommits(self) -> list[GitCommitTuple]:
        for commit in self._repo.walk(self.__checkedOutBranch.target):
            gitCommit = GitCommitTuple()
            gitCommit.authorName = commit.author.name
            gitCommit.authorEmail = commit.author.email
            gitCommit.message = commit.message
            gitCommit.timestamp = datetime.fromtimestamp(
                commit.commit_time
            ).strftime("%Y-%m-%d %H:%M:%S")
            gitCommit.hash = commit.short_id

            yield gitCommit

    def addRemote(self, remote: str, url: str) -> None:
        if remote in [r[0] for r in self.allRemotes()]:
            self._repo.remotes.set_url(remote, url)
        else:
            self._repo.remotes.create(remote, url)

    def deleteRemote(self, remote: str) -> None:
        if remote in [r[0] for r in self.allRemotes()]:
            self._repo.remotes.delete(remote)
        else:
            raise ValueError(f"Remote {remote} does not exist")

    def pushToRemote(
        self, remote: str, username: str, password: str = None
    ) -> None:
        if remote not in [r[0] for r in self.allRemotes()]:
            raise NoRemoteDefined(f"Remote {remote} not set for project")

        if password is None:
            cred = pygit2.Username(username)
        else:
            cred = pygit2.UserPass(username, password)

        remote = self._repo.remotes[remote]

        class RemoteCallback(RemoteCallbacks):
            def credentials(self, url, username_from_url, allowed_types):
                return cred

            def certificate_check(self, certificate, valid, host):
                # Return whatever the TLS/SSH library thinks about the cert
                return True

        remote.push(
            [self.__checkedOutBranch.name],
            callbacks=RemoteCallback(),
        )

    def pullFromRemote(
        self, remoteName: str, username: str, password: str = None
    ) -> None:
        if remoteName not in [r[0] for r in self.allRemotes()]:
            raise NoRemoteDefined(f"Remote {remoteName} not set for project")

        if password is None:
            cred = pygit2.Username(username)
        else:
            cred = pygit2.UserPass(username, password)

        remote = self._repo.remotes[remoteName]

        class RemoteCallback(RemoteCallbacks):
            def credentials(self, url, username_from_url, allowed_types):
                return cred

            def certificate_check(self, certificate, valid, host):
                # Return whatever the TLS/SSH library thinks about the cert
                return True

        remote.fetch(callbacks=RemoteCallback())

        checkedOutBranch = self.__checkedOutBranch
        remoteBranchName = f"{remoteName}/{checkedOutBranch.shorthand}"
        # Try to merge remote equivalent into current checked out
        self.mergeBranches(remoteBranchName)

    def mergeBranches(self, sourceBranch: str) -> None:
        if sourceBranch not in self.allBranches():
            raise ValueError(f"Branch {sourceBranch} does not exist")

        checked = self.__checkedOutBranch
        if ATTUNE_WORKING_BRANCH in self._repo.branches:
            working = self.__workingBranch

            logger.debug(f"Merging branches {sourceBranch} to {checked.name}")

            if working.target != checked.target:
                raise RuntimeError(
                    "There are changes pending to be committed. Please commit "
                    "them before trying again"
                )

        sourceBranchId = self._repo.branches[sourceBranch].target
        checkedBranchId = checked.target

        mergeAnalysis, _ = self._repo.merge_analysis(sourceBranchId)
        if mergeAnalysis & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
            logger.debug("Both branches are up-to-date. Nothing to merge")
            return

        if mergeAnalysis & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
            logger.debug("Branch can be fast-forwarded")
            # Fast-forward checked branch to source branch
            checked.set_target(sourceBranchId)

        elif mergeAnalysis & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
            """
            IMPORTANT!!
            The `merge` method on the `Repository` object and the merging
            procedure below is dependent on the state of the index and the
            working tree. We cannot use self.__index or any other methods
            that mutate the index or working tree here. self.__index
            reloads the index if there is no working branch which causes
            the merged index to be lost and the merged changes won't be
            committed.
            """

            logger.debug("Merging branches")
            self._repo.merge(sourceBranchId)
            # Check for merge conflicts and reverse merge if there are any
            if self._repo.index.conflicts:
                self._repo.reset(checkedBranchId, pygit2.GIT_RESET_HARD)
                raise MergeConflict("Cannot complete merge due to conflicts")

            logger.debug("Branches merged. Creating merge commit")
            self.__createCommit(
                "HEAD",
                "Merged pulled changes",
                [self._repo.head.target, sourceBranchId],
                self._repo.index,
            )

            # This is so Git CLI does not show status as MERGING
            self._repo.state_cleanup()

        else:
            raise RuntimeError("Unknown Git merge analysis result")

        checked = self.__checkedOutBranch
        if ATTUNE_WORKING_BRANCH in self._repo.branches:
            # Fast-forward the working branch on top of the merged branch
            # We need to reload the branch references here
            working = self.__workingBranch
            working.set_target(checked.target)
        # The checked branch status will show the modified files from the pull
        # here as staged because they were not created on disk. This will create
        # those files
        self._repo.reset(checked.target, pygit2.GIT_RESET_HARD)

        # Check for project validation errors after merge
        try:
            # This is the load method from GitObjectStorageContext
            self.load()
        except ProjectValidationError:
            logger.debug(
                "Merged project failed validation. Resetting to "
                "previous state"
            )
            self._repo.reset(checkedBranchId, pygit2.GIT_RESET_HARD)
            logger.debug("Project reset")
            raise Exception("Merging failed due to project validation errors")

        logger.debug("No validation errors after merge")

    def _getGitRevisionForBranch(self, name: str) -> str:
        assert name in self._repo.branches, "Branch does not exist in project"
        commit: pygit2.Commit = self._repo.revparse_single(name)
        return commit.id

    def __enter__(self):
        # Ensure that the working branch exists
        self.prepareWorkingBranch()
        self._workingId = self._getGitRevisionForBranch(ATTUNE_WORKING_BRANCH)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            # There was no error and this is a clean exit
            self._workingId = None
        else:
            logger.debug(
                f"Something went wrong. Resetting __working__ to"
                f" {self._workingId} in {self.project.name}"
            )
            checkedBranchName = self._checkedOutBranchRef
            self._repo.checkout(makeRef(ATTUNE_WORKING_BRANCH))
            self._repo.reset(self._workingId, pygit2.GIT_RESET_HARD)
            self._repo.checkout(checkedBranchName)
            self._workingId = None

            # Reset the index state so it is reinitialized
            self.__isIndexDirty = False
            self.__indexInitialised = False

            # Reload all items
            self.reloadProject()

    def renameProject(self, newName: str):
        """
        The user should not be able to rename when there is a __working__
        branch present. This is because we want the user to be able to revert
        and discard the changes on the __working__ branch. If rename is
        reverted, the Attune DB and the project name committed to
        `metadata.json` in the project will be out-of-sync
        """
        if ATTUNE_WORKING_BRANCH in self._repo.branches:
            raise RuntimeError(
                "There are changes pending to be committed. Please commit "
                "them before trying again"
            )

        metadata = self.metadata
        metadata["name"] = newName

        self.writeMetadata(metadata)
        self.commit("Write metadata with new name")
        self.squashAndMergeWorking(f"Renamed project to {newName}")
