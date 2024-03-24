from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

# Set input and output file paths
input_file = r"D:\Document\对比剂增强\MICCAI\画图\fig1.svg"
output_file = r"D:\Document\对比剂增强\MICCAI\画图\fig1.eps"

# Convert SVG to EPS
drawing = svg2rlg(input_file)
renderPDF.drawToFile(drawing, output_file)

# Print success message
# print(f"Converted {input_file} to {output_file}")

# In this code, we use the "svg2rlg" function from the "svglib" package
# to convert the SVG image to a "ReportLab Graphics" (RLG) object.
# We then use the "renderPDF" function from the "reportlab.graphics" module
# to convert the RLG object to EPS format and save it to the specified output file path.

# Note that the "reportlab" package is required for the EPS conversion to work,
# so you'll need to make sure it's installed before running this code.