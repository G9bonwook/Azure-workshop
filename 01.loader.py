# -*- coding: utf-8 -*-
"""01.loader.ipynb

pdf 파일을 불러오는 코드입니다.
"""

!pip install pypdf docx2txt
!pip install langchain langchain-community langchain-core

from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("/content/[정책브리프 2021-04] 탄소중립 대응을 위한 정부 정책과 동향.pdf")
pages = loader.load_and_split()

pages[0].page_content

from langchain.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("/content/LLM이 만들어 내는 혁명과 교통산업.docx")
pages = loader.load_and_split()

pages[0].page_content

from langchain.document_loaders import CSVLoader

loader = CSVLoader("/content/titanic3.csv")
pages = loader.load_and_split()

pages[0].page_content
