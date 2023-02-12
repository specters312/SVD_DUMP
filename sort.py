import os
import shutil
manufacturers = {
    'Silicon_Labs': ['EFM', 'EFR', 'EZR'],
    'Texas_Instruments': ['TM4C', 'MSP', 'CC13', 'CC26'],
    'STMicroelectronics': ['STM'],
    'NXP_Semiconductors': ['LPC', 'Kinetis'],
    'Atmel': ['SAM'],
    'Renesas_Electronics_Corporation': ['RX'],
    'Nordic_Semiconductor': ['NRF'],
    'Microchip': ['PIC', 'SAM'],
    'STMicroelectronics': ['STM'],
    'Fuji_Electric': ['MB9', 'MK5']
}

def classify_manufacturer(filename):
    for manufacturer, prefixes in manufacturers.items():
        for prefix in prefixes:
            if filename.startswith(prefix):
                return manufacturer
    return 'manufacturer_not_listed'

def main():
    path = os.getcwd()
    svd_files = [f for f in os.listdir(path) if f.endswith('.svd')]

    for svd in svd_files:
        manufacturer = classify_manufacturer(svd)
        directory = os.path.join(path, manufacturer)
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            shutil.move(svd, os.path.join(directory, svd))
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    main()
