#badger
import PyInstaller.__main__

v1:str=input("version: ")

PyInstaller.__main__.run([
	".\\main.py",
	"-F",
	"-n=encrypt"+v1,
	"-w",
	"-i=.\\resource\\icon.ico",
	"--clean"
])