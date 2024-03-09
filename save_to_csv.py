from devfolio_data_downloader import DevfolioDataDownloader

def main():
    # Provide the path to your JSON file when instantiating the class
    filename = r'C:\Users\DELL\Downloads\500.json'
    downloader = DevfolioDataDownloader(filename)
    
    # Provide the path where you want to save the CSV file
    csv_filename = r'C:\Users\DELL\Downloads\500.csv'
    
    # Call the save_to_csv method to save data to CSV
    downloader.save_to_csv(csv_filename)

if __name__ == "__main__":
    main()
