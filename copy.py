import os

def parse_str(*args: str):
    join = ""
    for arg in args:
        join += arg + "\n"
    return join


with open(R".vscode\settings.json", "w") as file:
    command: str = (
        R"cd $dir & cd .. & python -u"
        R"config/console_script.py &"
        R"cd $dir && tsc $fileName && "
        R"node $fileNameWithoutExt.js && "
        R"del $fileNameWithoutExt.js & cd .. & "
        R"python -u config/cleanup.py & cd $dir & cd .. ||"
        R"(echo count.txt > config/count.txt)"
    )

    file.write(
        parse_str(
            "{",
            '    "workbench.editor.empty.hint": "text",',
            '    "code-runner.clearPreviousOutput": true,',
            '    "code-runner.runInTerminal": true,',
            '    "code-runner.executorMap": {',
            '        "javascript": "node",',
            f'       "typescript": "{command}"' "}",
            "}",
        )
    )

directories: dict[str, list[str]] = {".": os.listdir(".")}
FILE_EXTENSIONS: tuple = tuple(["js"])
CANNOTREMOVE: tuple[str] = tuple([None])


for name, folder in directories.items():
    for file in folder:
        if name == ".":
            file_path = Rf"{file}"
        else:
            file = Rf"{name}\{file}"

        if (
            os.path.isfile(file_path)
            and "." in file_path
            and file_path.split(".")[1] == next(i for i in FILE_EXTENSIONS)
        ):
            if not file_path in CANNOTREMOVE:
                os.remove(f"cleaned:{file_path}")

