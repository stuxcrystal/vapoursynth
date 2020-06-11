import unittest
import time
import sys
import os

successful = unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.abspath(os.path.dirname(__file__))).wasSuccessful()
if not successful:
    raise RuntimeError("Test failed")
else:
    import vapoursynth
    vapoursynth.core.std.BlankClip().set_output()

sys.stdout.flush()
