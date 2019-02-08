#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from typing import Dict, Any, List, Union, Optional

C_GREEN = "\033[92m"
C_BLUE = "\033[94m"
C_END = "\033[00m"


# def grouping(fileList: List[str]) -> Any:
#     for path in fileList:
#         items = path.split("/")
#         bottom = items[-1]
#         dirs = items[0:-1]


def grouping(fileList: List[str]) -> Any:
    root: Dict[str, Any] = {}
    for path in fileList:
        current = root
        for p in path.rstrip("\n").split("/"):
            current.setdefault(p, {})
            current = current[p]
    return root


def displayItems(items: Any, path: str, prefix: str, color: bool) -> Any:

    for index, item in enumerate(sorted(items.keys())):
        if index == len(items) - 1:
            print(prefix + "└── " + appendColor(path, item, color))
            nextPrefix = prefix + "    "
        else:
            print(prefix + "├── " + appendColor(path, item, color))
            nextPrefix = prefix + "│   "
        if len(items[item]) > 0:
            nextpath = os.path.join(path, item)
            displayItems(items[item], nextpath, nextPrefix, color)


def appendColor(path: str, item: str, color: bool = False) -> str:
    filepath = os.path.join(path, item)
    indicator = "/" if os.path.isdir(filepath) else ""

    if not color:
        return item + indicator

    return get_color(filepath) + item + C_END + indicator


def get_color(filepath: str) -> str:
    if os.path.isdir(filepath):
        return C_BLUE
    elif os.access(filepath, os.X_OK):
        return C_GREEN

    return C_END


def get_stdout() -> Optional[List[str]]:
    cmd = "git ls-files"
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    p.wait()
    stdout_data = p.stdout.readlines()
    stderr_data = p.stderr.read()
    if len(stderr_data) > 0:
        print(stderr_data)
        return None

    return [item.decode("utf-8") for item in stdout_data]


def main() -> None:
    color = True
    paths = get_stdout()

    if paths is None:
        return

    group = grouping(paths)
    displayItems(group, ".", "", color)


if __name__ == "__main__":
    main()
