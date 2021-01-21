import tag_format_rules

max_width = 80
current_directory = True
output_folder = '\\articles'
stop_tag_names = ['script', 'img', 'svg', 'meta', 'link', 'nav', 'iframe', 'style']
container_tag_names = ['div', 'article', 'main', 'section']
console_output = True

tag_format_rules = {'p': tag_format_rules.TagFormatRules.rule_for_p,
                    'a': tag_format_rules.TagFormatRules.common_rule_for_a,
                    'h1': tag_format_rules.TagFormatRules.common_rule_for_header,
                    'h2': tag_format_rules.TagFormatRules.common_rule_for_header,
                    'h3': tag_format_rules.TagFormatRules.common_rule_for_header,
                    'h4': tag_format_rules.TagFormatRules.common_rule_for_header,
                    'h5': tag_format_rules.TagFormatRules.common_rule_for_header,
                    'h6': tag_format_rules.TagFormatRules.common_rule_for_header, }


def get_rules():
    return tag_format_rules

