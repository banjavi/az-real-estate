import csv
import pandas as pd
from redfin_scraper import RedfinScraper

# Initialize the scraper
scraper = RedfinScraper()

def main():
    zip_database_path = 'zip_code_database.csv'
    
    # Setup the scraper with the zip database and multiprocessing option
    scraper.setup(zip_database_path, multiprocessing=False)

    # Zip code to scrape
    zip_codes = ['85032']

    # Activate the scraper for the given zip code
    # Selecting sold homes and sales within the last 3 years
    scraper.scrape(zip_codes=zip_codes, sold=True, sale_period='3yr')

    # If you want to retrieve the scraped data by its ID
    # assuming the ID is "D001" for the first scrape, adjust accordingly
    data = scraper.get_data("D001")
    
    
    print(data)
    data.to_csv('scraped_data.csv', index=False)





if __name__ == '__main__':
    main()
