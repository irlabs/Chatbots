#!/usr/bin/env python

with open("pulpfiction.txt") as f:
    textlines = f.readlines()


dialoglines = []

for line in textlines:
    # names
    if line.startswith("                                     "):
        pass
    # dialog
    elif line.startswith("                         "):
        dialoglines.append(line)
    


# Save the filtered lines

# Create one long txt
outtext = ""
for dialog in dialoglines:
    outtext += dialog
    
# Save to file
with open("pulpfiction_dialog.txt", 'w') as f:
    f.write(outtext)