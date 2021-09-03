import yaml
import pkg_resources


#-----------------------
# Load and organize product descriptions and metadata
#-----------------------

def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.load(f, Loader=yaml.Loader)

sensor_files = dict(Landsat = 'product_files/Landsat.yaml',
                     MODIS  = 'product_files/MODIS.yaml')

product_list_by_sensor = {}
for sensor, sensor_file in sensor_files.items():
    package_path = pkg_resources.resource_filename(__name__, sensor_file)
    product_list_by_sensor[sensor] = load_yaml(package_path)

all_products = {}
for sensor in product_list_by_sensor.keys():
    all_products.update(product_list_by_sensor[sensor])

#----------------------
# User facing functions
#----------------------

def list_sensors():
    """
    Return a list of available sensors configured in the package.

    Returns
    -------
    list
        List of sensor names

    """
    return list(product_list_by_sensor.keys())

def list_products(sensor='all'):
    """
    Return a list of available products for QA unpacking. 
    'all', the default, returns the identifers for all products
    for all sensors

    Parameters
    ----------
    sensor : int, optional
        Sensor ID. The default is 'all'.

    Returns
    -------
    list
        List of product identifers

    """
    if sensor == 'all':
        return list(all_products.keys())
    elif sensor in list_sensors():
        return list(product_list_by_sensor[sensor].keys())
    else:
        error_message = 'Unknown sensor: {}. available sensors are {}'
        raise ValueError(error_message.format(sensor, list_sensors()))

def list_qa_flags(product):
    """
    Return a list of QA flags configured for a specific product.

    Parameters
    ----------
    product : str
        A unique product identifer. See `list_products()` for availability.

    Returns
    -------
    list
        List of QA flags. The descripters are used in the flag argument
        of `unpack_to_array()` and `unpack_to_dict()`.

    """
    if product in all_products:
        return list(all_products[product]['flag_info'].keys())
    else:
        error_message  = 'Unknown product: {}. Use list_products() for availability'
        raise ValueError(error_message.format(product))