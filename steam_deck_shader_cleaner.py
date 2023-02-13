import os, itertools
from pathlib import Path

### External dependency ###
import vdf


STEAM_ROOT_DIR = Path('/home/deck/.local/share/Steam')
LIBRARY_VDF_PATH = STEAM_ROOT_DIR / 'steamapps' / 'libraryfolders.vdf'
SHADER_CACHE_PATH = STEAM_ROOT_DIR / 'steamapps' / 'shadercache'
SHADER_FOLDERS = (d for d in SHADER_CACHE_PATH.iterdir() if d.is_dir())


def main():
    library_vdf = vdf.parse(open(LIBRARY_VDF_PATH))
    installed_app_ids = list(itertools.chain.from_iterable(
        (app_info.keys() for app_info in # Get AppIDs only \
            (storage_device_info['apps'] for storage_device, storage_device_info in \
                library_vdf['libraryfolders'].items()))) # Insert apps from all storage devices to one iterable
    )

    for folder in SHADER_FOLDERS:
        id = folder.name
        if id not in installed_app_ids:
            os.rmdir(SHADER_CACHE_PATH / id)


if __name__ == "__main__":
    main()
