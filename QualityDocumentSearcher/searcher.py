import os, re, sys, docx, openpyxl


class Searcher(object):
    def __init__(self, cod_path, file, file_in_cat_dict):
        self.path = os.path.join(cod_path, file)
        self.extension = os.path.splitext(file)[1]
        # self.ext_dict = {'.docx': self.search_docx_for_tags, '.txt': self.search_txt_for_tags,
        #                  '.xlsx': self.search_xlsx_for_tags}
        self.tags = {'QD': 'QD(?: |-)(\d+)(?: )?(.+)?(?:\t|\n)?', 'SOP': 'SOP (\d+(?: |-)\d+)(?: )?(.+)?(?:\t|\n)?',
                     'TD': 'TD(?: |-)(\d+)(?: )?(.+)?(?:\t|\n)?', 'FUS': 'FUS(\d+.\d+)(?: )?(.+)?(?:\t|\n)?',
                     'ST': 'ST(?: |-)(\d+)(?: )?(.+)?(?:\t|\n)?', 'SR': 'SR(?: |-)(\d+)(?: )?(.+)?(?:\t|\n)?'}
        self.known_files_dict = file_in_cat_dict

    def search(self):
        # self.results = self.ext_dict[self.extension]()
        self.results = {}
        data = open(self.path, 'rb').read()
        for tag in self.tags:
            self.results[tag] = re.findall(self.tags[tag], data)
        for category in self.known_files_dict:
            for file in self.known_files_dict[category]:
                if re.search(file, data):
                    self.results[category].append(re.findall(file, data))
                    #     #return results
                    # def search_docx_for_tags(self):
                    #     pass
                    #
                    # def search_txt_for_tags(self):
                    #     results = {}
                    #     data = open(self.path, 'rb').read()
                    #     for tag in self.tags:
                    #         results[tag] = re.findall(self.tags[tag], data)
                    #     for category in self.known_files_dict:
                    #         for file in self.known_files_dict[category]:
                    #             if re.search(file, data):
                    #                 results[category].append(re.findall(file, data))
                    #     return results
                    #
                    # def search_xlsx_for_tags(self):
                    #     pass
