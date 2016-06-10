# Design plan

# ---SOPs---
# Scraper
# Clusterer
# Output

# ---Titles---
# Scraper
# File reader
# Clusterer
# Output

# ---SOP-Title Mapper---
# Outputs Reader
# Cluster Mapper
# Output

import scraper, clusterer


def run():
    #Scraper
    titles_path = "N:/Common/ASTMs & Standards/ASTM/2015 Standards"
    output_path = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/titles.csv"

    scraper_ = scraper.Scraper(titles_path)
    scraper_.scrape()
    scraper_.output_results(output_path)


    #Clusterer
    cat_output_path = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/ASTMCategorization.csv"
    uncat_output_path = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/ASTMUncategorized.csv"

    clusterer_ = clusterer.Clusterer(output_path)
    clusterer_.categorize_data()
    clusterer_.output_categorization(cat_output_path, uncat_output_path)
