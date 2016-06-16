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
import scraper


def run(option):
    qdspath = "N:/Common/Joe Hardy/Quality/Quality Documents"
    outputpath = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/links.csv"

    s = scraper.Scraper(qdspath, option)
    s.walk()
    s.scrape()
    s.organize_results()
    s.output_results(outputpath)
