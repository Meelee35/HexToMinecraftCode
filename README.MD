# Hex2MC
Convert hex codes easily to MC colour codes.

# BUILDING

## Linux
```shell
pyinstaller --onefile --windowed \
  --add-data "main.ui:." \
  --add-data "output.ui:." \
  main.py
```

## Windows
```cmd
pyinstaller --onefile --windowed --add-data "main.ui;." --add-data "output.ui;." main.py
```
