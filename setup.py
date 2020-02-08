from cx_Freeze import setup, Executable

base = None

executables = [Executable("comparecsv.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="Compare Csv files",
    options=options,
    version="1.0",
    description='Compare 2 csv files and output the records that exist only in source file',
    executables=executables, requires=['pandas']
)
