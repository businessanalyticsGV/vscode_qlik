#path: C:\Users\alexisalvarez\OneDrive - Grupo Vidanta\UPDATE\Work\10. 05Feb19 - Summerfest Quickie\query.qvw

import psutil
import numpy as np

ls_OpenedWindows = [item.name() for item in psutil.process_iter() \
                    if 'Code.exe' in item.name() or 'Qv.exe' in item.name()]

ls_OpenedWindows = np.unique(ls_OpenedWindows)
print(len(ls_OpenedWindows))
