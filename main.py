import argparse

import data_from_url
import configs
import convert_to_text
import os
import page_scraper
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='page link to format')
    args = parser.parse_args()
    url = args.url

    page_data = data_from_url.data_from_url(url)
    if configs.console_output:
        sys.stdout.write('Data is downloaded.\n')
    scraper = page_scraper.PageScraper(page_data, url)
    node_to_save = scraper.find_node_with_biggest_sentences_count()
    rules = configs.get_rules()
    text = convert_to_text.ConvertToText(node_to_save, rules, wrap_len=configs.max_width,
                                         title=scraper.title).get_formatted_text()
    if configs.console_output:
        sys.stdout.write('Article is converted to text.\n')
    if configs.console_output:
        sys.stdout.write('Result:\n{}\n'.format(text))

    if configs.current_directory:
        path = os.getcwd() + configs.output_folder
    else:
        path = configs.output_folder

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            sys.stderr.write("Error creating directory: {}\n".format(path))
        else:
            if configs.console_output:
                sys.stdout.write("Directory {} is created.\n".format(path))
    filename = url.replace('/', '-').replace(':', '').replace('.', '-') + '.txt'
    with open(path + '\\' + filename, "w") as output:
        output.write(text)

    if configs.console_output:
        sys.stdout.write('Article is saved to {}\n'.format(path + '\\' + filename))
