def init_dir(dest, filenames):
    for name in filenames:
        with open(f"{dest}/{name}", "w") as _:
            pass


def create_files(data, filename, dest):
    with open(f"{dest}/{filename}", "w") as file:
        file.write(data)


def error_check(dest, filename):
    with open(f"{dest}/{filename}", "r") as error_file:
        errors = error_file.read()
        if errors == "":
            return (errors, False)
        return (errors, True)


def read_ouput(dest, filename):
    with open(f"{dest}/{filename}", "r") as file:
        output = file.read()
        return output
