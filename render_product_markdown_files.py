"""
Render the product pages. From the yaml files in product_files/

These are from the 'description' entry of each product

One file per sensor. Where within each file each product has a ## markdown heading.
"""

from unpackqa.product_loader import product_list_by_sensor

auto_generated_header = '<!-- this markdown file automatically generated. do not edit directly-->'

for sensor, product_list in product_list_by_sensor.items():
    file_text = '{}\n\n'.format(auto_generated_header)
    for product_identifer, product_details in product_list.items():
        pass
        # title text as header and sidebar entry
        file_text += '## {}\n\n'.format(product_details['product_name'])
        
        # product identifer
        file_text += '**Product Identifer**: `{}`\n\n'.format(product_identifer)
        
        # The 'description' entry in the yaml files which details everything else.
        # 
        # when loading yaml files, whitespace at the end of lines is stripped.
        # so replace newlines with two spaces + newline because that's
        # what markdown expects.
        file_text += product_details['description'].replace('\n','  \n')
        file_text += '\n'
    
    filepath = './docs/{}.md'.format(sensor)
    with open(filepath, 'w') as f:
        f.write(file_text)
