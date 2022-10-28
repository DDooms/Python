from pathlib import Path

# Absolute path -> c:\program files...
# Relative path

# if you don't specify argument in Path(), it will take the current dir
path = Path("packages")
print(path.exists())
