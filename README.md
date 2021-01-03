# Install dependencies
pip3 install -r requirements.txt

# Run script
python main.py


# Compiled with Pyinstaller

# Windows
pyinstaller --onefile --windowed main.py

# MacOS
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' main.py
```

- Version: 1.0.0
- License: MIT
- Author: yassine elazrak
