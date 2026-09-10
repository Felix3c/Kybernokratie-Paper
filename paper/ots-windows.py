# OpenTimestamps-Client unter Windows: laedt die von Python mitgelieferte libcrypto, weil find_library("ssl") dort leer ist.
# Aufruf: python paper/ots-windows.py stamp|upgrade|verify|info <datei>
import sys, ctypes.util, glob, os
dlls = glob.glob(os.path.join(os.path.dirname(sys.executable), "DLLs", "libcrypto*.dll"))
orig = ctypes.util.find_library
ctypes.util.find_library = lambda n: (dlls[0] if n in ("ssl","crypto","libeay32") and dlls else orig(n))
from otsclient.ots import main
sys.argv = ["ots"] + sys.argv[1:]
main()
