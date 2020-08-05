import enum
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DockerConfig:
    def __init__(self, cmd, dest):
        tout = 10
        self.cmd = cmd
        self.dest = dest
        env = os.getenv("QUART_ENV", "production")
        if env == "development":
            tout = 10
        self.tout = tout

    @property
    def data(self):
        data = {
            "name": "CompilerDock",
            "volumes": {},
            "detach": True,
            "image": "pydock",
            "command": ["/bin/bash", "-c"],
            "auto_remove": True
            # "timeout": 0,
        }

        # data["timeout"] = self.timeout
        data["command"].append(self.cmd)
        # data["config"]["HostConfig"]["Binds"].append(f"{self.dest}:/compile")
        data["volumes"].update({self.dest: {"bind": "/compile", "mode": "rw"}})
        return data

    @property
    def timeout(self):
        return self.tout


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
