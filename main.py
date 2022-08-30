import sys

from util import *
from pathlib import Path




logo = '''
    __  __       _____                  _            
   |  \/  |     / ____|                | |           
   | \  / |_ __| |     _ __ _   _ _ __ | |_ ___ _ __ 
   | |\/| | '__| |    | '__| | | | '_ \| __/ _ \ '__|
   | |  | | |  | |____| |  | |_| | |_) | ||  __/ |   
   |_|  |_|_|   \_____|_|   \__, | .__/ \__\___|_|   
                             __/ | |                 
                            |___/|_|      v. 0.2           
                            By   Aha
        '''


# Main Code
def StartEncryption(path, key1, key2, typ):
    Util.ClearConsole()
    Logger.PrintLogo(logo)
    key1_bytes = Crypt.ConvertKeySha256(key1, 16)
    key2_bytes = Crypt.ConvertKeySha256(key2, 15)
    files = list()

    Logger.Info(f'Path      > {path}')
    Logger.Info(f'Key 1     > {key1}  |  {key1_bytes}')
    Logger.Info(f'Key 2     > {key2}  |  {key2_bytes}')
    Logger.Info(f'Path Type > {typ}')
    Logger.Info(f'Enc Type  > Encryption')

    key1_bytes = key1_bytes.encode()
    key2_bytes = key2_bytes.encode()

    crypt = Crypt(key1_bytes, key2_bytes)

    if typ == "Directory":
        print()
        Logger.Info(f'Getting files in Directory and Subdirectories...')
        files = Util.getListOfFiles(path)
        Logger.Success(f'Found {len(files)} files')
        Logger.Success(f'Encryption started.')
        i = 0
        for file in files:
            i += 1
            Logger.Progress("Encryption Progress > ", i, len(files))
            crypt.EncryptFile(file)
        Logger.ClearLine()
        Logger.Success(f'All {len(files)} files were encrypted')
    if typ == "File":
        print()
        Logger.Success(f'Encryption started.')
        crypt.EncryptFile(path)
        Logger.Success(f'File was encrypted')

def StartDecryption(path, key1, key2, typ):
    Util.ClearConsole()
    Logger.PrintLogo(logo)
    key1_bytes = Crypt.ConvertKeySha256(key1, 16)
    key2_bytes = Crypt.ConvertKeySha256(key2, 15)
    files = list()

    Logger.Info(f'Path      > {path}')
    Logger.Info(f'Key 1     > {key1}  |  {key1_bytes}')
    Logger.Info(f'Key 2     > {key2}  |  {key2_bytes}')
    Logger.Info(f'Path Type > {typ}')
    Logger.Info(f'Enc Type  > Decryption')

    key1_bytes = key1_bytes.encode()
    key2_bytes = key2_bytes.encode()

    crypt = Crypt(key1_bytes, key2_bytes)

    if typ == "Directory":
        print()
        Logger.Info(f'Getting files in Directory and Subdirectories...')
        files = Util.getListOfFiles(path)
        Logger.Success(f'Found {len(files)} files')
        Logger.Success(f'Decryption started.')
        i = 0
        for file in files:
            i += 1
            Logger.Progress("Decryption Progress > ", i, len(files))
            crypt.DecryptFile(file)
        Logger.ClearLine()
        Logger.Success(f'All {len(files)} files were decrypted')
    if typ == "File":
        print()
        Logger.Success(f'Decryption started.')
        crypt.DecryptFile(path)
        Logger.Success(f'File was decrypted')


# Get Path
Util.ClearConsole()
Logger.PrintLogo(logo)
path = Logger.InputText("Enter File Path / Directory Path  > ")

path = Path(path)
typ = "?"

if path.is_file():
    Logger.Success(f"File found at {path}")
    typ = 'File'
elif path.is_dir():
    Logger.Success(f"Directory found at {path}")
    typ = 'Directory'
else:
    Logger.Error(f"Coudn't found any file or directory at {path}")
    sys.exit()

# Get Key 1
key1 = Logger.InputText("Enter Key 1 > ")
if not key1:
    Logger.Error("You didn't enter any key")
    sys.exit()

Logger.Success(f"Key 1 > {key1}")

# Get Key 2
key2 = Logger.InputText("Enter Key 2 > ")
if not key1:
    Logger.Error("You didn't enter any key")
    sys.exit()

Logger.Success(f"Key 2 > {key2}")

# Choose
choosing = Logger.InputText("You want to [1] Encrypt [2] Decrypt > ")
if choosing == "1":
    StartEncryption(path, key1, key2, typ)
elif choosing == "2":
    StartDecryption(path, key1, key2, typ)
else:
    Logger.Error("You inputed invalid number")


