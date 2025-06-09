#!/usr/bin/env python3
# Author ID: kbay@myseneca.ca


import subprocess

def free_space():
    #Launch the Linux commande pipeline
    process = subprocess.Popen(
        "df -h |grep '/$' |awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True

    )


# Capture output and errors
    output = process.communicate()

# Return cleaned output
    return  output.strip() 

if __name__ == "__main__":
    #print(free_space())

    import lab3d

lab3d.free_space()

# Will return 9.6G 
