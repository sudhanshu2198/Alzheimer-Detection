import streamlit as st
import streamlit.components.v1 as components
import os

dirname=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.join(dirname,os.pardir)
html_file_pth=os.path.join(root_dir,"html_files","data_integrity.html")
HtmlFile = open(html_file_pth, 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code,height=6000)
