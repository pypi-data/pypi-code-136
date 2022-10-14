"""Systematization Strategy is tool for strategy systematization

"""
# Standard library imports
import sys
import threading
import glob
import os.path
import time




class myThread (threading.Thread):
    def __init__(self, threadID, name, repo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.repo = repo

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        pull_repo(self.name, self.repo)
        # Free lock to release next thread
        threadLock.release()

def pull_repo(threadName, repo):
    os.system('cd ' + repo + ' && git stash && git pull')

    # g = git.cmd.Git(repo)
    #
    # g.pull()


threadLock = threading.Lock()
threads = []


def main() -> None:

    directories = glob.glob('./*')
    repos = [x for x in directories if os.path.isdir(x) and os.path.isdir(x + "/.git")]

    print(repos)

    for i in range(len(repos)):
        while threading.activeCount() > 3:
            time.sleep(0.05)
        t = myThread(i, "Job " + str(i), repos[i])
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Done!")


if __name__ == "__main__":
    main()
