import os
import shutil


manufacturers = {
    'ARM':['ARM','CMSDK'],
    'Allwinner_Community':['D1'],
    'Silicon_Labs': ['EFM', 'EFR', 'EZR','MGM','ZGM','BGM'],
    'Texas_Instruments': ['TM4C', 'MSP', 'CC13', 'CC26'],
    'Cypress':['psoc'],
    'GigaDevice':['GD3'],
    'Holtek':['HT3'],
    'Espressif-Community':['ESP'],
    'Freescale':['MK'],
    'STMicroelectronics': ['STM'],
    'NXP_Semiconductors': ['LPC', 'QN9','MIM'],
    'Atmel': ['SAM','AT'],
    'Renesas_Electronics_Corporation': ['RX'],
    'Nuvoton':['NUC','M05'],
    'Nordic_Semiconductor': ['NRF'],
    'RaspberryPi':['RP'],
    'Microchip': ['PIC', 'SAM'],
    'STMicroelectronics': ['STM'],
    'Fuji_Electric': ['MB9', 'S6E']
}

def classify_manufacturer(filename):
    for manufacturer, prefixes in manufacturers.items():
        for prefix in prefixes:
            if filename.upper().startswith(prefix):
                return manufacturer
    return 'manufacturer_not_listed'

def main():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        svd_files = [f for f in files if f.endswith('.svd')]
        for svd in svd_files:
            manufacturer = classify_manufacturer(svd)
            directory = os.path.join(path, manufacturer)
            if not os.path.exists(directory):
                os.makedirs(directory)
            try:
                svd_src = os.path.join(root, svd)
                svd_dst = os.path.join(directory, svd)
                if os.path.exists(svd_dst):
                    src_size = os.stat(svd_src).st_size
                    dst_size = os.stat(svd_dst).st_size
                    if src_size > dst_size:
                        os.remove(svd_dst)
                        shutil.move(svd_src, svd_dst)
                else:
                    shutil.move(svd_src, svd_dst)
            except FileNotFoundError:
                pass

if __name__ == '__main__':
    main()
