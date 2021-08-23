"""
Render the product pages. From the yaml files in product_files/

These are from the 'description' entry of each product

One file per sensor. Where within each file each product has a ## markdown heading.
"""

from pyUnpackQA.product_loader import product_list_by_sensor

auto_generated_header = '<!-- this markdown file automatically generated. do not edit directly-->'

for sensor, product_list in product_list_by_sensor.items():
    file_text = '{}\n\n'.format(auto_generated_header)
    for product_name, product_details in product_list.items():
        file_text += '## {}\n'.format(product_name)
        # when loading yaml files, whitespace at the end of lines is stripped.
        # so replace newlines with two spaces + newline because that's
        # what markdown expects.
        file_text += product_details['description'].replace('\n','  \n')
        file_text += '\n'
    
    filepath = './docs/{}.md'.format(sensor)
    with open(filepath, 'w') as f:
        f.write(file_text)
