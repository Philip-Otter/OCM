## Copyright 2023 Philip Otter


def cheat_line(line, architecture, isTargetSet):
    print("Cheat Line Function")


def mod_name(name):
    print("Mod Name Function")


def program_version(line):
    print("Program Version Function")


def target_module(line):
    print("Target Module Function")


def set_theme(theme):
    print("Set Theme Function")


def set_application(app):
    print("Set Application Function")


def gen_HTML(HTMLLine):
    print("Gen HTML Function")


def gen_JavaScript(JSLine):
    print("Gen JavaScript Function")


def gen_Python_3(PythonLine):
    print("Gen Python 3 Function")


def read_File(file):
    with open(file,'r') as oyster:

        modderName = None
        theme = None
        arch = None
        targetSet = False

        # First sweep to find {V}, {T}, {C}, {X} shellfish
        print("Checking for {V}, {T}, {C}, {X}")
        for line in oyster:
            if('{V}' in line):
                program_version(line.strip('{V}'))
            elif('{T}' in line):
                target_module(line.strip('{T}'))
                targetSet = True
            elif('{C}' in line):
                theme = line.strip('{C}')
            elif('{X}' in line):
                arch = line.strip('{X}')
            elif('{APP}' in line):
                set_application(line.strip('{APP}'))
            else:
                pass

            # Checks to see if default theme needs to be used.
            if(theme != None):
                set_theme(theme)
            else:
                set_theme("Default")

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
                cheat_line(line.strip('{}'),arch, targetSet)
            elif('{H5}' in line):
                gen_HTML(line.strip('{H5}'))
            elif('{JS}' in line):
                gen_JavaScript(line.strip('{JS}'))
            elif('{P3}' in line):
                gen_Python_3(line.strip('{P3}'))
            else:
                pass

        # Checks to see if the modder provided their name. 
        if(modderName != None):
                    mod_name(modderName)
        
        oyster.close()






                

