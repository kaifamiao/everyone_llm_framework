# kfm_config.py
import os
def get_project_root():
    # 获取当前工作目录
    return os.path.dirname(os.path.abspath(__file__))

system_path =get_project_root()
def get_system_path():
    return system_path


from colorama import Fore, Style, init
init()
def qqqq(str):
    return Fore.LIGHTWHITE_EX + str + Style.RESET_ALL

def rrrr(str):
    return Fore.RED + str + Style.RESET_ALL

def mmmm(str):
    return Fore.MAGENTA + str + Style.RESET_ALL

def yyyy(str):
    return Fore.YELLOW + str + Style.RESET_ALL


import re
def extract_link(text):
    # 定义正则表达式模式，用于匹配方括号内的内容
    pattern = r'\[([^\]]+)\]'

    # 使用 re.search 查找匹配的内容
    match = re.search(pattern, text)

    # 如果找到匹配的内容，返回匹配的组（即方括号内的内容）
    if match:
        return match.group(1)
    else:
        return None


def extract_second_link(text):
    # 定义正则表达式模式，用于匹配第二个方括号内的内容
    pattern = r'\[[^\]]+\]\[\s*([^\]]+)\s*\]'

    # 使用 re.search 查找匹配的内容
    match = re.search(pattern, text)

    # 如果找到匹配的内容，返回匹配的组（即第二个方括号内的内容）
    if match:
        return match.group(1)
    else:
        return None




def read_markdown(filename):

    # 读取并显示 sidebar_content.md 文件中的内容
    filepath = os.path.join(get_project_root(), 'content/')
    markdown_file = filepath + filename
    sidebar_content = "ERROR"
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r', encoding='utf-8') as file:
            sidebar_content = file.read()
    else:
        sidebar_content = f"**content file `{filename}` not found.**"
    return sidebar_content


def read_html(filename):
    filepath = os.path.join(get_project_root(), 'content/')
    html_file = filepath + filename
    print(html_file)
    html_content = "ERROR"
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
    else:
        html_content = "<p style='color:red'>ERROR!</p>"
    return html_content


def out_html(st: object, sts: int, filename: object) -> object:
    if sts == 0:
        st.sidebar.markdown(read_html(filename), unsafe_allow_html=True)
    else:
        st.markdown(read_html(filename), unsafe_allow_html=True)

import streamlit.components.v1 as components
def com_out_html(sts:int,filename):

    components.html(read_html(filename))
    # components.html(read_html(filename), height=600, scrolling=False)
