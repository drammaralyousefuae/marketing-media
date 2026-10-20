import sys, runpy, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n
script=sys.argv[1]; sys.argv=[script]+sys.argv[2:]
runpy.run_path(script, run_name='__main__')
