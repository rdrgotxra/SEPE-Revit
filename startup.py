from pyrevit.extensions import extensionmgr

extensions = extensionmgr.get_thirdparty_extension_data()

for ext in extensions:
    print(ext.name)
