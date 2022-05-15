# This script should read all of the jpeg or CR2 files in a given directory.
# It should then iterate over the files looking for files that have been given a star rating
# Inbetween star rated files we should add those images to a new directory based off of a starting index number
import typer
from os import listdir, getcwd
from os.path import isfile, join

SUPPORTED_FILE_TYPES = ("jpg", "jpeg", "cr2")

def get_files(path: str) -> list[str]:
    return [f for f in listdir(path) if isfile(join(path, f))]

def filter_files(files: list[str]) -> list[str]:
    return [ file for file in files if file.endswith(SUPPORTED_FILE_TYPES) ]

def is_star_rated(filePath: str) -> bool:
    starRated = False
    print(info["keywords"])
    return starRated

def find_star_files(files: list[str]) -> list[str]:
    

    return []


app = typer.Typer()

@app.command()
def organize(directory: str = typer.Argument(getcwd(), help="The absolute path for the directory where this should be ran.")):
    all_files = get_files(directory)
    filtered_files = filter_files(all_files)
    star_files = find_star_files(filtered_files)
    
#organize("C:\\dev\\test-photos")

print(is_star_rated("C:\\dev\\test-photos\\Box 01_00001B.jpg"))
