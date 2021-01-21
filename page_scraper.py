import bs4
import re
import urllib.parse

import configs


class SearchState:
    def __init__(self):
        self.sentences_count = 0
        self.found_tag = None


class PageScraper:
    def __init__(self, page_data, url):
        self.stop_tag_names = configs.stop_tag_names
        self.container_tag_names = configs.container_tag_names
        self.soup = bs4.BeautifulSoup(page_data, 'lxml')
        self.title = self.soup.find('head').find('title').text
        self.url = url
        self.cleanup_soup()
        self.replace_relative_links_with_absolute()

    def cleanup_soup(self):
        """
        Clean up data of tags.
        """
        for tag in self.soup(self.stop_tag_names):
            tag.extract()

    def replace_relative_links_with_absolute(self):
        for a in self.soup.find_all('a', href=True):
            if a.get('href'):
                a['href'] = urllib.parse.urljoin(self.url, a['href'])

    def find_node_with_biggest_sentences_count(self) -> bs4.Tag:
        """
        Search for a node with the highest number of sentences.
        It has to be from self.container_tag_names.
        """
        body = self.soup.find('body')
        search_state = SearchState()
        self.search_for_tag_recursively(body, search_state)
        return search_state.found_tag

    def search_for_tag_recursively(self, root: bs4.Tag, search_state: SearchState):
        """
        Recursive tree search for nodes from self.container_tag_names
        that have no children from self.container_tag_names. Count sentences
        and extract current node. Go to extracted node's parent and repeat.
        """
        # regular expression for sentences
        sentence_regex = r"\s*[^.!?]*[.!?]"

        for child in root.find_all(recursive=False):
            self.search_for_tag_recursively(child, search_state)
            if child.name in self.container_tag_names:
                # count amount of elements that matches sentence_regex in child
                current_sentence_count = len(list(re.findall(sentence_regex,  child.text)))
                child.extract()
                # save maximum and respective tag
                if current_sentence_count > search_state.sentences_count:
                    search_state.sentences_count = current_sentence_count
                    search_state.found_tag = child
