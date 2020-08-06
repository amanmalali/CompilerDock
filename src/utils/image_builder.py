import docker
from docker.errors import APIError, BuildError, ImageNotFound
from halo import Halo


class Colorize:
    _colours = {
        "PURPLE": "\033[95m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "ORANGE": "\033[93m",
        "RED": "\033[91m",
        "ENDC": "\033[0m",
    }

    @classmethod
    def colorize(cls, text: str, colour: str) -> str:
        clr = cls._colours.get(colour.upper(), "")
        end = cls._colours.get("ENDC")
        return "".join([clr, text, end])


class ImageBuilder:
    def __init__(self):
        self.client = docker.from_env()
        self.spinner = Halo(spinner="dots")
        self.colorize = Colorize.colorize

    def __del__(self):
        if self.spinner:
            self.spinner.stop()

    def image_exists(self, img: str) -> bool:
        try:
            self.client.images.get(img)
            return True
        except ImageNotFound:
            return False

    def build_images(self, languages):
        failed, built = 0, 0
        for lang in languages:
            try:
                text_build = f"Building image for {lang}"
                img_name = f"{lang}-compiler"
                self.spinner.start(self.colorize(text=text_build, colour="orange"))
                if self.image_exists(img_name):
                    self.spinner.succeed(
                        self.colorize(
                            text=f"Image {img_name} already exists, skipping build...",
                            colour="green",
                        )
                    )
                else:
                    _, _ = self.client.images.build(
                        path="docker/",
                        dockerfile=f"{lang}/Dockerfile",
                        tag=img_name,
                        forcerm=True,
                    )
                    self.spinner.succeed(self.colorize(text=text_build, colour="green"))
                    built += 1

            except APIError as apierr:
                failed += 1
                self.spinner.fail(self.colorize(text=apierr.explanation, colour="red"))
            except BuildError as be:
                failed += 1
                self.spinner.fail(self.colorize(text=be.msg, colour="red"))

        print(f"Built: {built}")
        print(f"Failed {failed}")

    def rebuild_images(self, languages):
        rebuilt, failed = 0, 0
        for lang in languages:
            try:
                text_build = f"Reuilding image for {lang}"
                img_name = f"{lang}-compiler"
                self.spinner.start(self.colorize(text=text_build, colour="orange"))
                if self.image_exists(img_name):
                    self.client.images.remove(image=img_name, force=True)

                _, _ = self.client.images.build(
                    path="docker/",
                    dockerfile=f"{lang}/Dockerfile",
                    tag=img_name,
                    forcerm=True,
                )
                self.spinner.succeed(self.colorize(text=text_build, colour="green"))
                rebuilt += 1
            except APIError as apierr:
                failed += 1
                self.spinner.fail(self.colorize(text=apierr.explanation, colour="red"))
            except BuildError as be:
                failed += 1
                self.spinner.fail(self.colorize(text=be.msg, colour="red"))

        print(f"Reuilt: {rebuilt}")
        print(f"Failed {failed}")

    def create_images(self, languages: list, rebuild: bool = False):
        if rebuild:
            self.rebuild_images(languages)
        else:
            self.build_images(languages)
