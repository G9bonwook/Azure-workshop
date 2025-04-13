# -*- coding: utf-8 -*-
"""7.paper_review.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p_j63avOGE1m7hNbMW8WRTC4cd-axI_3
"""

!pip install langchain langchain-core langchain-community
!pip install pypdf
!pip install openai
!pip install tiktoken

import os
os.environ["OPENAI_API_KEY"] = "G2PRojIueFtGUZc0SHf2E0xjooxgn3V9FZt1kl8r2UKpNFdeZAGNJQQJ99BDACYeBjFXJ3w3AAABACOGIMEc"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://azure18-openai.openai.azure.com/"
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2025-01-01-preview"

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import AzureOpenAI
import tiktoken

# PDF 불러오기
loader = PyPDFLoader("/content/NetLLM.pdf")
pages = loader.load_and_split()
pages

# 토큰 단위로 잘라주기 작업을 하기 위해 토크나이저 생성
tokenizer = tiktoken.encoding_for_model("gpt-4o-mini")
def tiktoken_len(text):
  tokens = tokenizer.encode(text)
  return len(tokens)

# 문서를 토큰 단위로 split
text_spliiter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 20,
    length_function = tiktoken_len,
)

docs = text_spliiter.split_documents(pages)

from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def build_review_chain():
    template = """
    너는 논문 리뷰어야. 다음 논문 내용을 보고 아래를 수행해줘:

    1. 연구 목적을 간결하게 요약해줘.
    2. 강점과 한계점을 bullet point로 정리해줘.
    3. 다음 항목별로 5점 만점 기준으로 점수를 매겨줘:
       - 혁신성
       - 논리성
       - 실용성

    논문 내용:
    {context}

    출력 형식:
    [요약]
    ...

    [강점]
    - ...

    [한계점]
    - ...

    [평점]
    - 혁신성: ? / 5
    - 논리성: ? / 5
    - 실용성: ? / 5
    """

    prompt = PromptTemplate(
        input_variables=["context"],
        template=template,
    )

    llm = AzureChatOpenAI(
    model_name="dev-gpt-4o-mini",
    temperature=0.4,
    max_tokens=500
)


    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

chain = build_review_chain()

# 처음 2개 chunk만 사용 (속도 문제 방지)
context = docs
review = chain.run(context)

from IPython.display import Markdown
Markdown(f"### 📝 리뷰 결과\n\n```\n{review}\n```")