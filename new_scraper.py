import csv
import pandas as pd
from redfin_scraper import RedfinScraper
import os

# initialize the scraper
scraper = RedfinScraper()

def main():
    zip_database_path = 'zip_code_database.csv'
    
    # setup the scraper with the zip database and disable multiprocessing
    scraper.setup(zip_database_path, multiprocessing=False)
    
    # list of all Maricopa County zip codes
    zip_codes = [
        '85142', '85225', '85032', '85326', '85204', '85301', '85383', '85308', '85041', '85345',
        '85033', '85008', '85338', '85035', '85009', '85282', '85234', '85339', '85037', '85207',
        '85022', '85201', '85379', '85286', '85029', '85295', '85296', '85224', '85212', '85281',
        '85323', '85042', '85254', '85353', '85249', '85205', '85051', '85283', '85015', '85226',
        '85202', '85255', '85382', '85086', '85017', '85044', '85209', '85374', '85213', '85021',
        '85210', '85298', '85251', '85027', '85297', '85260', '85392', '85233', '85303', '85302',
        '85203', '85340', '85208', '85018', '85248', '85206', '85043', '85395', '85016', '85023',
        '85040', '85335', '85048', '85388', '85020', '85031', '85331', '85050', '85257', '85351',
        '85375', '85019', '85053', '85304', '85381', '85014', '85396', '85085', '85024', '85006',
        '85306', '85258', '85268', '85259', '85284', '85013', '85139', '85028', '85310', '85288',
        '85083', '85373', '85253', '85215', '85250', '85387', '85007', '85305', '85355', '85307',
        '85118', '85262', '85266', '85378', '85004', '85087', '85054', '85012', '85361', '85003',
        '85390', '85354', '85256', '85034', '85045', '85239', '85363', '85321', '85289', '85342',
        '85337', '85077', '85263', '85264', '85320', '85322', '85329', '85309', '85545', '85287',
        '85333', '85377', '85219', '85025', '85098', '85227', '85097', '85099', '85096', '85290',
        '85055', '85313', '85358', '85372', '85376', '85380', '85385', '85269', '85275', '85274',
        '85277', '85280', '85285', '85299', '85311', '85312', '85318', '85327', '85343', '85080',
        '85079', '85082', '85211', '85214', '85216', '85236', '85244', '85246', '85252', '85261',
        '85267', '85271', '85001', '85002', '85005', '85011', '85010', '85026', '85030', '85036',
        '85039', '85038', '85046', '85060', '85062', '85061', '85064', '85063', '85066', '85065',
        '85068', '85067', '85070', '85069', '85072', '85071', '85074', '85073', '85076', '85075',
        '85078', '85190', '85127'
    ]

    # ensure the "zipcodes" directory exists
    if not os.path.exists('zipcodes'):
        os.makedirs('zipcodes')

    # activate the scraper for each zip code
    for zip_code in zip_codes:
        try:
            data = scraper.scrape(zip_codes=[zip_code], sold=True, sale_period='3yr')
            data.to_csv(f'zipcodes/scraped_data_{zip_code}.csv', index=False)
        except Exception as e:
            print(f"error scraping data for zip code {zip_code}: {e}")

    # combine all individual zip code CSVs into one consolidated CSV
    all_data = pd.concat([pd.read_csv(f'zipcodes/scraped_data_{zip_code}.csv') for zip_code in zip_codes], ignore_index=True)
    all_data.to_csv('new_scraped_data.csv', index=False)
    print(f"total number of records after scraping: {all_data.shape[0]}")

if __name__ == '__main__':
    main()
