"""
Criado by Nicholas Borba
Para transferir todos Replays do Tryd para a pasta correta de uma vez
visto que cada arquivo de replay esta contido dentro de uma pasta com sua data
"""

import os
import pathlib
import shutil

SCRIPT_NAME = os.path.basename(__file__)
CURRENT_FOLDER = pathlib.Path().absolute()
TRYD_REPLAY_FOLDER = "C:\Tryd6\workspace\\replay\import\WDO&DOL"

for folder, b, files  in os.walk(CURRENT_FOLDER):
    for item in files:
        file_to_copy = os.path.join(folder, item)
        shutil.copy(file_to_copy, TRYD_REPLAY_FOLDER) 

os.remove(os.path.join(TRYD_REPLAY_FOLDER, SCRIPT_NAME))