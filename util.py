import os

from Crypto.Cipher import AES
from hashlib import sha256
from colorama import Fore, init

init(autoreset = True)

class Crypt: 
    def __init__(self, Key1, Key2):
        self.Key1 = Key1
        self.Key2 = Key2
    
    def Encrypt(self, Data):
        cipher = AES.new(self.Key1, AES.MODE_EAX, self.Key2)
        encryptedData = cipher.encrypt(Data)
        return encryptedData

    def Decrypt(self, Encrypted_Data):
        cipher = AES.new(self.Key1, AES.MODE_EAX, self.Key2)
        Data = cipher.decrypt(Encrypted_Data)
        return Data

    def EncryptFile(self, File):
        Data = Util.readFileBytes(File)
        Encrypted_Data = self.Encrypt(Data)
        Util.writeFileBytes(File, Encrypted_Data)

    def DecryptFile(self, File):
        Encrypted_Data = Util.readFileBytes(File)
        Data = self.Decrypt(Encrypted_Data)
        Util.writeFileBytes(File, Data)

    def ConvertKeySha256(Key, Lenght=64):
        return sha256(Key.encode('utf-8')).hexdigest()[0:Lenght]
    
class Util:
    def getListOfFiles(Directory):
        listOfFile = os.listdir(Directory)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(Directory, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + Util.getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
                    
        return allFiles
    def writeFileBytes(Path, Data):
        f = open(Path, "wb")
        f.write(Data)
        f.close()

    def readFileBytes(Path):
        f = open(Path, "rb")
        Data = f.read()
        f.close()
        return Data

    def ClearConsole():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

class Logger:
    def PrintLogo(Logo):
        print(Fore.CYAN + Logo)

    def Error(txt):
        print(f'[{Fore.RED}ERROR{Fore.RESET}]    {Fore.RED}{txt}')

    def Info(txt):
        print(f'[{Fore.BLUE}INFO{Fore.RESET}]     {Fore.BLUE}{txt}')

    def Success(txt):
        print(f'[{Fore.GREEN}SUCCESS{Fore.RESET}]  {Fore.GREEN}{txt}')

    def Progress(txt, fromNumber, toNumber):
        print(f'[{Fore.BLUE}PROGRESS{Fore.RESET}] {Fore.BLUE}{txt}[{Fore.RESET}{fromNumber}{Fore.BLUE}/{Fore.RESET}{toNumber}{Fore.BLUE}]', end="\r")
        
    def ProgressEnd(txt, fromNumber, toNumber):
        print(f'[{Fore.BLUE}PROGRESS{Fore.RESET}] {Fore.BLUE}{txt}[{Fore.RESET}{fromNumber}{Fore.BLUE}/{Fore.RESET}{toNumber}{Fore.BLUE}]', end="\n")

    def ClearLine():
        print('                                                                                                  ', end="\r")

    def InputText(txt):
        return input(f'[{Fore.YELLOW}INPUT{Fore.RESET}]    {Fore.YELLOW}{txt}{Fore.RESET}')