from devfolio_data_downloader import DevfolioDataDownloader

def main():
    # Provide the path to your JSON file when instantiating the class
    filename = r'C:\Users\DELL\Downloads\500.json'
    downloader = DevfolioDataDownloader(filename)
    
    # Call the display_data method to print the data
    downloader.display_data()

if __name__ == "__main__":
    main()
