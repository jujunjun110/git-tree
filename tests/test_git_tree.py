import unittest
import subprocess
from gitTree.gitTree import grouping, displayItems, appendColor, get_stdout


class TestGitTree(unittest.TestCase):
    def test_grouping(self) -> None:
        res = get_stdout()
        print(res)

    def test_main(self) -> None:
        cmd = "git ls-files"
        p = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        p.wait()
        stdout_data = p.stdout.readlines()
        stderr_data = p.stderr.read()
        print(stdout_data)
        print(stderr_data)


if __name__ == "__main__":
    unittest.main()
