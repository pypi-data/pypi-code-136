from sparrow.string.color_string import rgb_string, color_const
from git import Repo, RemoteProgress
import os
from sparrow.utils.cursor import Cursor

cursor = Cursor()


class CloneProgress(RemoteProgress):
    MESSAGE = ''

    def update(self, op_code, cur_count, max_count=None, message=""):
        percent = cur_count / (max_count or 100.0) * 100
        self.MESSAGE = message if message != "" else self.MESSAGE
        print(f"\r{int(cur_count)}|{int(max_count)} {self.MESSAGE} PERCENT:{percent:.0f}% {cursor.EraseLine(0)} ",
              end='', flush=True)


def clone(url: str, repo_name=None, branch=None):
    url = url.strip()
    if repo_name is None:
        repo_name = url.split('/')[-1][:-len('.git')]
    if url.startswith('git'):
        git_proxy_dir = url
    else:
        git_proxy_dir = f"https://ghproxy.com/{url.strip()}"
    print(rgb_string(f"Cloning into '{repo_name}' ...", color=color_const.green))
    Repo.clone_from(git_proxy_dir, to_path=repo_name, branch=branch, progress=CloneProgress())


def clone_cmd(url: str):
    os.system(f"git clone https://ghproxy.com/{url.strip()}")


if __name__ == "__main__":
    clone("https://github.com/beidongjiedeguang/beidongjiedeguang.git")
    # clone_cmd("https://github.com/beidongjiedeguang/beidongjiedeguang.git")
