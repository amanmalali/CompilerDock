import enum
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DockerConfig:
    def __init__(self, cmd: str, dest: str):
        tout = 20
        self.cmd = cmd
        self.dest = dest
        env = os.getenv("QUART_ENV", "production")
        if env == "development":
            tout = 10
        self.tout = tout

    def _image_name(self, name: str):
        name = name.lower()
        if "python" in name:
            return "python-compiler"
        if "c++" == name or "c" == name:
            return "gcc-compiler"

        return f"{name}-compiler"

    @property
    def data(self):
        data = {
            "name": None,
            "volumes": {},
            "detach": True,
            "image": None,
            "command": ["/bin/bash", "-c"],
            "auto_remove": True,
        }

        img_name = self._image_name(self.cmd.split()[1])
        data["image"] = img_name
        data["name"] = f"{img_name}-container"
        data["command"].append(self.cmd)
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


exe = {"c": " && ./a.out", "c++": " && ./a.out", "rust": " && ./file"}
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
