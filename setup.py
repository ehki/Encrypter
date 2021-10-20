import sys
from cx_Freeze import setup, Executable
from crypttools import VERSION as __version__

if 'bdist_msi' in sys.argv:
    sys.argv += ['--add-to-path', 'True']

upgrade_code = '{5c302335-a116-43e6-8e46-1764395facda}'

shortcut_table = [
    ('DesktopShortcut',        # Shortcut
     'DesktopFolder',          # Directory
     "Encrypter",           # Name
     'TARGETDIR',              # Component
     '[TARGETDIR]encrypter.exe',   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR',              # WkDir
     )
]

msi_data = {'Shortcut': shortcut_table}

build_exe_options = {
    'packages': [],
    'excludes': [],
    'includes': [],
    'include_files': [
        'README.md',
        ]
}

bdist_msi_options = {
    'upgrade_code': upgrade_code,
    'add_to_path': True,
    'all_users': False,
    'data': msi_data,
    'install_icon': 'icon.ico'
}

bdist_mac_options = {
    'iconfile': 'icon.ico',
    'bundle_name': 'Encrypter',
    'include_resources': [
        ('README.md', 'README.md'),
        ]
}

bdist_dmg_options = {
    'volume_label': 'Encrypter',
    'applications_shortcut': True,
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options,
    'bdist_mac': bdist_mac_options,
    'bdist_dmg': bdist_dmg_options,
}

base = 'Win32GUI' if sys.platform == 'win32' else None

exe = Executable(
    script='encrypter.py',
    target_name='encrypter.exe',
    base=base,
    icon='icon.ico'
)

setup(
    name='Encrypter',
    version=__version__,
    description='Simple text encryption tool',
    options=options,
    executables=[exe])
