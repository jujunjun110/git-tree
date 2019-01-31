import unittest
import subprocess
from typing import Dict, Any
from gitTree.gitTree import grouping, displayItems, appendColor, get_stdout


class TestGitTree(unittest.TestCase):
    def test_grouping(self) -> None:
        case = ["a", "a/p", "a/p/x", "a/p/y", "a/q/z", "a/q/w"]
        actual = grouping(case)
        expected: Dict[str, Any] = {
            "a": {"p": {"x": {}, "y": {}}, "q": {"z": {}, "w": {}}}
        }
        self.assertEqual(actual, expected)

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
