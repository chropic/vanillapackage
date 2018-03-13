
import os
import shutil
import tkMessageBox

import defs
from easyinstallers.Skype import signTo


def run():
    CMA = defs.getCmaDir()
    if not os.path.exists(CMA + "/EXTRACTED/APP/PCSF00124"):
        shutil.copytree(defs.getWorkingDir() + "/easyinstallers/Skype/PCSF00124", CMA + "/EXTRACTED/APP/PCSF00124")
    signTo.vp_start_gui()


