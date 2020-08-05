import asyncio
import os
import tempfile

import docker
from quart.exceptions import HTTPException

from src.config import BASE_PATH, DockerConfig, FileNames, exe, filenames, lang_cmd
from src.utils.files import create_files, error_check, init_dir, read_ouput

try:
    os.mkdir(f"{BASE_PATH}/temp")
except FileExistsError:
    pass


async def run_container(dest, command):
    docker_config = DockerConfig(command, dest)
    client = docker.from_env()
    sleep_count = 0
    finish_run = None
    try:
        client.containers.run(**docker_config.data)
        while sleep_count != docker_config.timeout and not finish_run:
            if os.path.exists(f"{dest}/{FileNames.completed.value}"):
                finish_run = True
                break
            else:
                await asyncio.sleep(1)
                sleep_count += 1

    except Exception:
        raise HTTPException(status_code=500, description="Docker error", name=None)
    else:
        return finish_run


async def run_code(lang, code, stdin):
    output, error, fail, timeout_flag = "", "", False, False
    try:
        lang_cmd[lang]  # Check if language is supported
    except KeyError:
        raise HTTPException(
            status_code=400,
            description=f"Unknown or unsupported language {lang}",
            name=None,
        )

    with tempfile.TemporaryDirectory(dir=f"{BASE_PATH}/temp") as dest:
        init_dir(dest=dest, filenames=[FileNames.error.value, FileNames.output.value])
        create_files(code, filenames[lang], dest)
        create_files(stdin, FileNames.input.value, dest)
        command = "".join(
            [
                "/script/run.sh ",
                lang_cmd[lang],
                " ",
                filenames[lang],
                exe.get(lang, ""),
            ]
        )

        finish_run = await run_container(dest, command)
        error, fail = error_check(dest, FileNames.error.value)
        if finish_run:
            output = read_ouput(dest, FileNames.completed.value)
        else:
            output = read_ouput(dest, FileNames.output.value)
            timeout_flag = True

    return (output, error, fail, timeout_flag)
