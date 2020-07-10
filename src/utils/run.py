import os
import subprocess
import tempfile
import time
import asyncio

from src.config import BASE_PATH, comp, exe, filenames, inter, FileNames
from src.utils.files import create_files, error_check, init_dir, read_ouput

try:
    os.mkdir(f"{BASE_PATH}/temp")
except FileExistsError:
    pass

async def run_code(lang, code, stdin):
    output, error, fail, timeout_flag = None, None, None, None
    sleep_count=0
    timeout=20
    with tempfile.TemporaryDirectory(dir=f"{BASE_PATH}/temp") as dest:
        await init_dir(dest=dest, filenames=[FileNames.error.value, FileNames.output.value])
        await create_files(code, filenames[lang], dest)
        await create_files(stdin, FileNames.input.value, dest)
        if(lang in comp):
            param2 = '/scripts/run.sh ' + inter[lang] + ' ' + filenames[lang] + exe[lang]
        else:
            param2 = '/scripts/run.sh ' + inter[lang] + ' ' + filenames[lang]
        subprocess.call(['src/scripts/dockerRun.sh', dest, param2])

        finish_run=False
        while sleep_count!=timeout and not finish_run:
            if os.path.exists(f"{dest}/{FileNames.completed.value}"):
                finish_run=True
            else:
                asyncio.sleep(1)
                sleep_count+=1

        error, fail = await error_check(dest, FileNames.error.value)
        if finish_run:
            output = await read_ouput(dest, FileNames.completed.value)
            timeout_flag=0
        else:
            output = await read_ouput(dest, FileNames.output.value)
            timeout_flag=1

    return (output, error, fail, timeout_flag)
