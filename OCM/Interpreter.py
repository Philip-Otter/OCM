## Copyright 2023 Philip Otter


def cheat_line(line, architecture, isTargetSet: bool, path):
    print("Cheat Line Function")

    # Split our line values
    lineFace = line.split('|')[0]  # InteractionType:CheatName
    lineBody = (line.split('|')[1]).split('>')[0]  # BaseOffset:PointerOffsets
    lineTail = (line.split('|')[1]).split('>')[1]  # if isTargetSet=False:  ModValue<TargetModule  # If isTargetSet=True:  ModValue
    # Further break down of our values
    interactionType = lineFace.split(":")[0]
    cheatName = lineFace.split(":")[1]
    baseOffset = lineBody.split(":")[0]
    pointerOffset = lineBody.split(":")[1]

    if(isTargetSet):
        ModValue = lineTail
    else:
        ModValue = lineTail.split("<")[0]
        targetModule =  lineTail.split("<")[1]
    

    def python_64():
        print("Python 64bit function")


    def python_32():
        print("Python 32bit function")


    # Evaluate our architecture
    if(architecture == 64 or architecture ==32):
        if(architecture ==64):
            python_64()
        else:
            python_32()
    else:
        print("Unexpected Architecture type! Aborting!")
        exit()
    


def mod_name(name, path):
    print("Mod Name Function")


def program_version(line, path):
    print("Program Version Function")


def target_module(line, path):
    print("Target Module Function")


def set_theme(theme, path):
    print("Set Theme Function")


def set_application(app, path):
    print("Set Application Function")

    


def gen_HTML(HTMLLine, path):
    print("Gen HTML Function")


def gen_JavaScript(JSLine, path):
    print("Gen JavaScript Function")


def gen_Python_3(PythonLine, path):
    print("Gen Python 3 Function")


def read_File(file, path):
    with open(file,'r') as oyster:

        modderName = None
        theme = None
        arch = None
        targetSet = False

        # First sweep to find {V}, {T}, {C}, {X}, {APP} shellfish
        print("Checking for {V}, {T}, {C}, {X}")
        for line in oyster:
            if('{V}' in line):
                program_version(line.strip('{V}'), path)
            elif('{T}' in line):
                target_module(line.strip('{T}'), path)
                targetSet = True
            elif('{C}' in line):
                theme = line.strip('{C}')
            elif('{X}' in line):
                arch = line.strip('{X}')
            elif('{APP}' in line):
                set_application(line.strip('{APP}'), path)
            else:
                pass

            # Checks to see if default theme needs to be used.
            if(theme != None):
                set_theme(theme, path)
            else:
                set_theme("Default", path)

            # Checks to make sure that the modder provided the architecture
            if(arch != None):
                pass
            else:
                print("No architecture provided. Aborting!")
                exit()
            
        oyster.seek(0)  # Move back to the start of the oyster

        # Second sweep for the rest of our shellfish
        for line in oyster:
            if('{@}' in line):
                modderName = line.strip('{@}')
            elif('{}' in line):
                cheat_line(line.strip('{}'),arch, targetSet, path)
            elif('{H5}' in line):
                gen_HTML(line.strip('{H5}'), path)
            elif('{JS}' in line):
                gen_JavaScript(line.strip('{JS}'), path)
            elif('{P3}' in line):
                gen_Python_3(line.strip('{P3}'), path)
            else:
                pass

        # Checks to see if the modder provided their name. 
        if(modderName != None):
                    mod_name(modderName, path)
        
        oyster.close()