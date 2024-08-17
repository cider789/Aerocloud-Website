import re
from cssbeautifier import beautify

# File paths
input_css_file = 'C:/Users/Bender/Documents/Payment Portal/main_web/assets/bootstrap/css/bootstrap.min.css'
output_css_file = 'C:/Users/Bender/Documents/Payment Portal/main_web/assets/bootstrap/css/output_bootstrap.css'


# Regex to match class names
class_pattern = r'(\.[a-zA-Z0-9-_]+)'

# Function to convert class names to readable names
def convert_classes(css):
    classes = re.findall(class_pattern, css)
    class_mapping = {}
    
    # Generate a readable class name
    for index, class_name in enumerate(set(classes)):
        readable_class_name = f'.class-{index+1}'
        class_mapping[class_name] = readable_class_name
    
    # Replace class names with readable names
    for class_name, readable_class_name in class_mapping.items():
        css = css.replace(class_name, readable_class_name)
    
    return css

# Read the original CSS from the input file
with open(input_css_file, 'r') as file:
    input_css = file.read()

# Convert the CSS
converted_css = convert_classes(input_css)

# Beautify the CSS to make it more readable
formatted_css = beautify(converted_css)

# Write the formatted and converted CSS to the output file
with open(output_css_file, 'w') as file:
    file.write(formatted_css)

# Print completion message
print(f"Conversion and formatting complete! Check '{output_css_file}' for the readable CSS.")