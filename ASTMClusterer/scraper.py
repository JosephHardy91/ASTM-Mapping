# Title Scraper
import os, re, csv


class Scraper(object):
    def __init__(self, titles_path):
        self.titles_path = titles_path

    def scrape(self):
        self.titles_dict = {}
        for osobj in os.listdir(self.titles_path):
            if self.is_astm_standard(osobj):
                id, title = re.findall('([D,F]\d+-\d+) (.+)', os.path.splitext(osobj)[0])[0]
                self.titles_dict[id] = title

    def output_results(self, output_path):
        with open(output_path, 'wb') as outcsv:
            csvwriter = csv.writer(outcsv, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"')
            csvwriter.writerow(['Standard ID','Standard Title'])
            csvwriter.writerows(zip(self.titles_dict.keys(),self.titles_dict.values()))

    def is_astm_standard(self, file_name):
        try:
            return os.path.splitext(file_name)[1].lower() == '.pdf' \
                   and len(re.findall('([D,F]\d+-\d+) (.+)', os.path.splitext(file_name)[0])[0]) == 2
        except:
            return False
