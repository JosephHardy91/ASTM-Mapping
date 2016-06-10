# Design plan
import ASTMClusterer
import time
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

# init menu
while True:
    try:
        first_choice = int(
            raw_input("What would you like to do?\n\t1.Title Clusterer\n\t2.SOP Clusterer\n\t3.Cluster Mapper\n\t4.Do all.\n>"))

        break
    except:
        print "Make an actual selection."

if first_choice == 1:
    ASTMClusterer.run()

elif first_choice == 2:
    print "Choice not available."
    time.sleep(5)
    exit()

elif first_choice == 3:
    print "Choice not available."
    time.sleep(5)
    exit()

elif first_choice==4:
    print "Choice not available."
    time.sleep(5)
    exit()
