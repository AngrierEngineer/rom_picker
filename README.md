# Rom Picker
This is part of a Python projects that aims to handle the gap between archive grade ROM dumps and roms that are playable by current generation emulations. The goal is to be able to take a archived image and convert it to a playable image per request. This relies hevealy on MAME's CHDMAN tool to convert the image into a playable format, so the emulator must be able to support the CHD format. This tool alsoaims to change one compression to another so that older collections can be converted to new compressions meathods as they become avalible. 

Planned features:
- 7z/zip/rar convertion to chd for image based ROMs
- 7z/zip/rar to 7z/zip/rar convertion
- Maintaining a cache of converted images so that the coversion doesn't have to be done every time
- "Cleaning up" old images when space quota is hit.
- Intergration into Retro Pi nd other SBC projects.
- Batch conversion of files to avoid long wait times.

Limitations:
- To my knowledge there isn't any python based libraries that allow for direct CHD conversion so this program will have to be a wrapper program until such a thing exsist. If anyone has a good way to use the C++ code in python, please let me know.
- Since this tool uses CHDMAN, all the limitations CHD has, this tool will also have.
- Due to the nature of compression and limited resources of SBC, conversion will always be time consuming. 
- Due to limited memory, sbc will most likely not be able to use memory to temerary files.
- Network communications will depend on samba or nfs mounted shares.


