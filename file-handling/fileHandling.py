import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="(asctime)s - %(levelname)s - %(message)s"
)

def openFile(filePath, mode="r", enconding="utf-8"):
    if "r" in mode and not os.path.exists(filePath):
        logging.error(f"file not found: {filePath}")
        return None
    
    try:
        if "b" in mode:
            file = open(filePath, mode)
        else:
            file=open(filePath, mode, encoding=enconding)

        logging.info(f"successfully opened file: {filePath} in '{mode}' mode")
        return file
    
    except FileNotFoundError:
        logging.error(f"File not found: {filePath}")
    except PermissionError:
        logging.error(f"permission denied: {filePath}")
    except ValueError as e:
        logging.error(f"invalid mode or encoding: {e}")
    except Exception as e:
        logging.error(f"an unexpected error occured while opening the file: {e}")

    return None

# def getWordCount():
#     int wc = 0
#     return wc

def main():
    filePath = "text-file\sample.txt"
    with openFile(filePath, "r") as file:
        if file: 
            content = file.read()
            print("File Content:")
            print(content)