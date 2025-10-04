import re

def replace_title_braces(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有title={xx}的模式，并替换其中的括号

  new_content = re.sub(r'title	=\{([^}]*)\}', r'title	=\{\{\\1\}\}', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 调用函数，替换指定文件中的title字段的括号
replace_title_braces('references.bib')