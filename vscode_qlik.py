import psutil

ls_OpenedWindows = [item.name() for item in psutil.process_iter() \
                    if 'Code.exe' in item.name() or 'Qv.exe' in item.name()]

ls_OpenedWindows = np.unique(ls_OpenedWindows)
len(ls_OpenedWindows)