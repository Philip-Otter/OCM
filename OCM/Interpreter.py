## Copyright 2023 Philip Otter


def cheat_line(line, architecture, isTargetSet: bool, path, app, referenceNumber: int, globalTarget):
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
    
    def python_gen():
        # Determine the path for our Python cheat file
        filePath = path+"/"+str(referenceNumber)+".py"  # Example:  ~/Documents/OCM_Files/Ocean/1.py
        # Make our Python file for the cheat
        set_application(app, filePath)


        cheatFile = open(filePath, 'a')
        if(isTargetSet):
            modValue = lineTail
            cheatFile.write('targetModule = module_from_name(pm.process_handle, "'+str(globalTarget)+'").lpBaseOfDll')
        else:
            modValue = lineTail.split("<")[0]
            targetModule =  lineTail.split("<")[1]
            cheatFile.write('targetModule = module_from_name(pm.process_handle, "'+str(targetModule)+'").lpBaseOfDll')

        cheatFile.write('offsets = ['+pointerOffset+']')
        cheatFile.write('baseOffset = '+baseOffset)
        cheatFile.write('def get_pointer_address(base, offsets):')

        # Evaluate our architecture
        if(architecture == 64 or architecture ==32):
            if(architecture == 64):
                cheatFile.write('   addr = pm.read_longlong(base+baseOffset)')
            else:
                cheatFile.write('   addr = pm.read_int(base)')
        else:
            print("Unexpected Architecture type! Aborting!")
            cheatFile.close()
            exit()
        
        cheatFile.write('    for i in offsets:')
        cheatFile.write('        if(i != offsets[-1]):')

        # Evaluate our architecture one last time
        if(architecture == 64):
            cheatFile.write('            addr = pm.read_longlong(addr + i)')
        else:
            cheatFile.write('            addr = pm.read_int(addr + i)')
        
        cheatFile.write('    return addr + offsets[-1]')

        # Check for interaction type
        if(interactionType == 'Toggle'):
            cheatFile.write('while True:')
            cheatFile.write('    pm.write_int(get_pointer_address(targetModule, offsets), '+ modValue+ ')')
        elif(interactionType == 'Button'):
            cheatFile.write('while True:')
            pass  # Will need to update with button code when it gets written
        elif(interactionType == 'Instant'):
            cheatFile.write('pm.write_int(get_pointer_address(targetModule, offsets), '+modValue+')')
        else:
            print("Not a valid interaction type. Aborting!")
            cheatFile.close()
            exit()
        
        cheatFile.close

    

    python_gen()
    


def mod_name(name, path):
    print("Mod Name Function")


def program_version(line, path):
    print("Program Version Function")


def set_theme(theme, path):
    print("Set Theme Function")


def set_application(app, filePath):
    print("Set Application Function")

    newFile = open(filePath, "w")

    # Copy over our headers into the cheat file
    with open('./GenerativeP3Sources/headers.py', 'r') as headers:
        for line in headers:
            newFile.write(line)
    headers.close()

    with open('./GenerativeP3Sources/imports.py', 'r') as imports:
        for line in imports:
            newFile.write(line)
    imports.close()

    newFile.write('pm = Pymem("'+str(app)+'")')  # Should read like this in the cheat file:  pm = Pymem("myApplication.exe")
    newFile.close()
    


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
        application = None
        targetModule = None
        targetSet = False

        # First sweep to find {V}, {T}, {C}, {X}, {APP} shellfish
        print("Checking for {V}, {T}, {C}, {X}")
        for line in oyster:
            if('{V}' in line):
                program_version(line.strip('{V}'), path)
            elif('{T}' in line):
                targetModule = line.strip('{T}')
                targetSet = True
            elif('{C}' in line):
                theme = line.strip('{C}')
            elif('{X}' in line):
                arch = line.strip('{X}')
            elif('{APP}' in line):
                application = line.strip('{APP}')
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

        cheatCounter = 0  # Used to reference our python files for the cheats
        # Second sweep for the rest of our shellfish
        for line in oyster:
            if('{@}' in line):
                modderName = line.strip('{@}')
            elif('{}' in line):
                cheat_line(line.strip('{}'),arch, targetSet, path, application, cheatCounter, targetModule)
                cheatCounter = cheatCounter+1
            elif('{H5}' in line):
                gen_HTML(line.strip('{H5}'), path)
            elif('{JS}' in line):
                gen_JavaScript(line.strip('{JS}'), path)
            elif('{P3}' in line):
                gen_Python_3(line.strip('{P3}'), path)
                cheatCounter = cheatCounter+1
            else:
                pass

        # Checks to see if the modder provided their name. 
        if(modderName != None):
                    mod_name(modderName, path)
        
        oyster.close()