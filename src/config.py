import enum
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DockerConfig:
    def __init__(self, cmd, dest):
        timeout = 20
        self.cmd = cmd
        self.dest = dest
        env = os.getenv("QUART_ENV", "production")
        if env == "development":
            timeout = 10
        self.timeout = timeout

    def data(self):
        data = {
            "config": {
                "Image": "compiler:v1",
                "Cmd": ["/bin/bash", "-c"],
                "HostConfig": {"Binds": []},
            },
            "name": "CompilerDock",
            "timeout": 0,
        }

        data["timeout"] = self.timeout
        data["config"]["Cmd"].append(self.cmd)
        data["config"]["HostConfig"]["Binds"].append(f"{self.dest}:/compile")
        return data


class FileNames(enum.Enum):
    error = "errors"
    completed = "completed"
    input = "input"
    output = "output"


exe = {"c": " ./a.out", "c++": " ./a.out", "rust": " ./file"}
lang_cmd = {
    "python3": "python3",
    "c": "gcc",
    "c++": "g++",
    "java": "java",
    "go": '"go run"',
    "R": "Rscript",
    "PHP": "php",
    "ruby": "ruby",
    "rust": "rustc",
}
filenames = {
    "python3": "file.py",
    "c": "file.c",
    "c++": "file.cpp",
    "java": "file.java",
    "go": "file.go",
    "R": "file.r",
    "PHP": "file.php",
    "ruby": "file.rb",
    "rust": "file.rs",
}
