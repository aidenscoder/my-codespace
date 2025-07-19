import os

def parse_str(*args:str):
    join = ""
    for arg in args:
        join += arg + "\n"
    return join

with open(RF'node project\.vscode\settings.json','w') as file:
    command = (
        RF"cls & cd $dir && tsc $fileName && "
        RF"node $fileNameWithoutExt.js && " 
        RF"del $fileNameWithoutExt.js & "
        RF"python -u configure\\cleanup.py"
    )
    
    file.write(
        parse_str(
            '{',
            '    "workbench.editor.empty.hint": "text",',
            '    "code-runner.clearPreviousOutput": true,',
            '    "code-runner.runInTerminal": true,',
            '    "code-runner.executorMap": {',
            '        "javascript": "node",',
            f'       "typescript": "{command}"'
                '}',
            '}'
        )
    )

directories: dict[str,list[str]] = {
    '.':os.listdir(".")
    #'modules':os.listdir('modules')
}

CANNOT_REMOVE:set = set()

for name,folder in directories.items():
    for file in folder:
        path = RF"{name}\{file}"
        if os.path.isfile(path) and '.' in path and path.split('.')[1] == 'js':
            if not path in CANNOT_REMOVE:
                os.remove(path)
