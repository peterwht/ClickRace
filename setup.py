import cx_Freeze

executables = [cx_Freeze.Executable("clickRace.pyw")]

cx_Freeze.setup(
    name = "Click Race",
    options = {"build_exe":{"packages":["pygame"], "include_files":["BlueCar1.png", "RedCar.png", "beep2.wav", "beep4.wav", "checkered.png"]}},
    description = "Click Race",
    executables = executables
    

    )
