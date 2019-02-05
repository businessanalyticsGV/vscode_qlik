#path: C:\Users\alexisalvarez\OneDrive - Grupo Vidanta\UPDATE\Work\10. 05Feb19 - Summerfest Quickie\query.qvw

### I.- 
import psutil
import win32api
import numpy as np

var_OpenedWindows = [item.name() for item in psutil.process_iter() \
                    if 'Code.exe' in item.name() or 'Qv.exe' in item.name()]

var_OpenedWindows = len(np.unique(var_OpenedWindows))

if var_OpenedWindows != 2:
    win32api.MessageBox(0,'VSCode y QlikView tienen que estar abiertos.','Error')
    exit()

print(var_OpenedWindows)