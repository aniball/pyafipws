call .venv27\Scripts\activate.bat

python -m PyInstaller --clean --noconfirm --onefile --console --name rece1 ^
  --hidden-import=pyafipws.wsaa ^
  --hidden-import=pyafipws.wsfev1 ^
  --hidden-import=UserList ^
  --hidden-import=UserDict ^
  --hidden-import=UserString ^
  --hidden-import=dbf ^
  --hidden-import=httplib2 ^
  rece1.py