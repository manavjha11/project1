import cx_Freeze

executables = [cx_Freeze.Executable("tanks.py")]

cx_Freeze.setup(
    name="tanks",
    option={"build_exe":{"packages":["pygame"],"incluade_files":["laser.wav","explosion.wav"]}},
    description = "hungry snake game",
    executables = executables
    )
