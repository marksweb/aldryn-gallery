import sys
import os

cmd = 'coverage run `which djangocms-helper` aldryn_gallery test --cms --extra-settings=test_settings'

sys.exit(os.system(cmd))
