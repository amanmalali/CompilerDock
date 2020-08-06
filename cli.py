import os

import inquirer
from inquirer.themes import GreenPassion

from src.utils.image_builder import Colorize, ImageBuilder


def get_languages() -> list:
    """Return a list a list of buildable languages
    Assumes the following directory structure
        docker/
            lang1/
                Dockerfile
            lang2/
                Dockerfile
            lang3/
                Dockerfile
    """
    x = next(os.walk("docker/"))[1]  # get only directories
    x.remove("script")  # remove script directory
    return x


def ignore(answer: dict) -> bool:
    if "all" in answer.get("action"):
        return True
    return False


def main(questions: list, languages: list):
    option = inquirer.prompt(questions, theme=GreenPassion())
    build_type = option.get("action")  # Build type: all or selected
    build_option = "rebuild" in build_type  # build or rebuild
    ib = ImageBuilder()
    if "all" in build_type:
        ib.create_images(languages, build_option)
    else:
        ib.create_images(option.get("partial_build"), build_option)


if __name__ == "__main__":
    txt = (
        "This script can build or rebuild the docker images specified in the docker folder."
        "It will also generate the language_list file in src/ folder."
    )
    summary = Colorize.colorize(text=txt, colour="purple",)
    print(summary)
    languages = get_languages()
    questions = [
        inquirer.List(
            name="action",
            message="Select the appropriate action",
            choices=[
                "build all images",
                "build selected images",
                "rebuild all images",
                "rebuild selected images",
            ],
        ),
        inquirer.Checkbox(
            name="partial_build",
            message=(
                "Select the language you want to install:"
                "(press <space> to select, <enter> to finalize)"
            ),
            choices=languages,
            ignore=ignore,
        ),
    ]
    main(questions, languages)
