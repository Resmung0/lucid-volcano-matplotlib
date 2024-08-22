# Inside the source path
from logging import Logger
from pathlib import Path

import matplotlib as mpl

logger = Logger('lucid-volcano')

def create_style_folder() -> Path:
    style_folder = Path(mpl.get_configdir()).joinpath('stylelib')
    style_folder.mkdir(exist_ok=True)
    return style_folder

def move_style_file(style_folder: Path) -> None:
    origin = Path('lucid-volcano.mplstyle')
    destination = style_folder.joinpath(origin)
    try:
        origin.rename(destination)
        logger.info(f'File moved to {destination}')
    except FileNotFoundError:
        logger.error(f'The file {origin.name} was not found.')
    except PermissionError:
        logger.error('Permission denied! The file already exists.')
    except Exception as e:
        logger.error(f'An error happened: {e}')
    
def install():
    logger.info('Installing...')
    logger.info('Creating style folder...')
    style_folder = create_style_folder()
    logger.info('Moving style file...')
    move_style_file(style_folder)
    logger.info('Installation completed!')


if __name__ == "__main__":
    install()