import os

mtime_opts = ''
if os.environ.get('FORCE_MTIME') == 'true':
    mtime_opts = ' --force'

os.system('python3 scripts/source/git-restore-mtime.py' + mtime_opts)