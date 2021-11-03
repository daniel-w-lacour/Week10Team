def remainingvolume(boxlen, boxwid, boxhei, holerad):
    pi = 3.1415926
    if not (holerad > boxwid / 2 and holerad > boxlen / 2):
        print("Error, hole radius can't be >= the surface's dimensions.")
        quit()
    boxvol = boxhei * boxlen * boxwid
    holevol = pi * (holerad ** 2) * boxhei
    remvol = boxvol - holevol
    return remvol