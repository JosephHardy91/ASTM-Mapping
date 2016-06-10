import os, re, csv, string
from collections import defaultdict, Counter
from insigwords import insig_words


class Clusterer(object):
    def __init__(self, data_path):
        self.data_path = data_path
        self.read_in_data()

    def read_in_data(self):
        self.title_dict = {}
        with open(self.data_path, 'rb') as dcsv:
            dcsvreader = csv.DictReader(dcsv)
            for row in dcsvreader:
                st = row['Standard Title']
                exclude = set(string.punctuation)
                s = ''.join(ch for ch in st if ch not in exclude)
                stcats = [x for x in s.split(" ") if x not in insig_words]
                self.title_dict[row['Standard ID']] = (st, stcats)

    def categorize_data(self):
        unique_categories = set(word for title, categories in self.title_dict.values() for word in categories)
        new_uniques = []
        for unique_category in list(unique_categories):
            for unique_category2 in list(unique_categories)[1:]:
                if unique_category[:-1] == unique_category2:
                    new_uniques.append(unique_category2)
                else:
                    new_uniques.extend([unique_category, unique_category2])

        unique_categories = set(new_uniques)
        unique_category_counts = defaultdict(int)
        for unique_category in unique_categories:
            for id, categories in self.title_dict.values():
                if unique_category in categories:
                    unique_category_counts[unique_category] += 1
        unique_category_counts = {key: value for key, value in
                                  zip(unique_category_counts.keys(), unique_category_counts.values()) if value > 10}
        self.marked_keys = []
        self.cat_dict = defaultdict(list)
        for id in self.title_dict:
            for category in unique_category_counts:
                if category in self.title_dict[id][1]:
                    self.cat_dict[category].append(' '.join([id, self.title_dict[id][0]]))
                    self.marked_keys.append(id)

    def output_categorization(self, output_path, uncat_output_path):
        unmarked_keys = [' '.join([id, self.title_dict[id][0]]) for id in self.title_dict if id not in self.marked_keys]
        running_id = 1
        with open(output_path, 'wb') as catcsv:
            catwriter = csv.writer(catcsv)
            catwriter.writerow(['StID', 'Object', 'Parent'])
            catwriter.writerow([running_id, 'ASTM', ''])
            for category in self.cat_dict:
                running_id += 1
                cat_id = running_id
                catwriter.writerow([running_id, category, 1])
                running_id += 1
                for title in self.cat_dict[category]:
                    catwriter.writerow([running_id, title, cat_id])
                    running_id += 1
        with open(uncat_output_path, 'wb') as uncat:
            for key in unmarked_keys:
                uncat.write(key)
                uncat.write(',\n')


"""-----Junk Code-----"""

# import matplotlib.pyplot as plt

# data_path = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/titles.csv"

# catwriter.writerow(['Standard ID', 'Standard Title'] + ['Category {}'.format(i + 1) for i in range(max_num_cats)])
#     for title in title_dict.keys():
#         catwriter.writerow([title, title_dict[title][0]] + [x for x in title_dict[title][1]])

# c = Counter(unique_category_counts.values())
# cvalarea = []
# for k, ck in enumerate(sorted(c.keys())):
#     cvalarea.append(sum([c[v] for v in sorted(c.keys())[:k]]) / float(sum(c.values())))
# plt.plot(sorted(c.keys()), cvalarea)
# plt.show()
# max_num_cats = max(sum(
#     1 for cat, ccount in zip(unique_category_counts.keys(), unique_category_counts.values()) if cat in titval[1])
#                    for titval in self.title_dict.values())
# output_path = "C:/Users/User/SyncedFolder/Quality Share/ASTM Mapping/Data/ASTMCategorization.csv"
# with open(output_path, 'wb') as catcsv:
#     catwriter = csv.writer(catcsv)
#     catwriter.writerow(['Standard ID', 'Standard Title'] + ['Category {}'.format(i + 1) for i in range(max_num_cats)])
#     for title in title_dict.keys():
#         catwriter.writerow([title, title_dict[title][0]] + [x for x in title_dict[title][1]])
