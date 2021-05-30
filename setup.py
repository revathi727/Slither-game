import cx_Freeze

executables = [cx_Freeze.Executable("slither.py")]

cx_Freeze.setup(
    name = "Slither",
    options = {"build_exe":{"packages":["pygame"], "include_files":["apple30px.png", "snakehead20px.png"]}},
    
)