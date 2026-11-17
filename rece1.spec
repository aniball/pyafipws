# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['rece1.py'],
             pathex=['C:\\Users\\Anibal\\pyafipws'],
             binaries=[],
             datas=[],
             hiddenimports=['pyafipws.wsaa', 'pyafipws.wsfev1', 'dbf', 'httplib2', 'UserList', 'UserDict', 'UserString', 'commands', 'ConfigParser', 'Queue', 'SocketServer', 'BaseHTTPServer', 'SimpleHTTPServer', 'CGIHTTPServer', 'Cookie', 'cookielib', 'htmlentitydefs', 'HTMLParser', 'httplib', 'urllib2', 'urlparse', 'robotparser', 'xmlrpclib', 'SimpleXMLRPCServer', 'DocXMLRPCServer', 'cPickle', 'cStringIO', 'StringIO', 'repr', 'thread', 'dummy_thread', 'dbm', 'anydbm', 'whichdb', '_winreg', 'copy_reg'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='rece1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
