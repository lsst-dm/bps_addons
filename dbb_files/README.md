
Copy the directory to your home archive (e.g., /work/dbb_acsws02/OPS/HSC/config/w_2018-37-v1).  (If you change filenames, you will need to modify submit wcl to match.)

To run just the examples provided you should not have to edit the butler yaml file (path is relative path inside compute job)
If you are creating new tests, you may need to add new templates.

The sqlite3 file is from a ci_hsc run using a specific weekly.   

You will need to have whatever image files the examples use registered in your home archive (if you haven't already registered all of ci_hsc input data)

Run register_files.py on the yaml and sqlite3 file (--filetype config).
