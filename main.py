# Text to Handwriting Using Python

import pywhatkit as pw

txt = """Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language."""

# pw.text_to_handwriting(txt,"demo.png",[0,0,138])
pw.text_to_handwriting(txt,"demo.png",[255,0,0])

print(" END ")