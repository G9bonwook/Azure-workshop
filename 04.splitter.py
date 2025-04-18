# -*- coding: utf-8 -*-
"""4.splitter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cNG70EqY1Qkz2jfJeW9FUw-kF3zA3W0-
"""

!pip install langchain langchain-core langchain-community

# 파일 읽어오기
with open("/content/generative ai.txt") as f:
  text_gen_ai = f.read()

text_gen_ai[0:50]

# 파일을 자를 때 사용되는 라이브러리
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. CharacterTextSplitter
# 1000 글자를 하나의 청크로 나눔, 오버랩은 100글자
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
    )

# 1000자가 넘어도 WARNING 메세지만 표시
texts = text_splitter.split_text(text_gen_ai)

print(texts[0])
print("-" * 100)
print(texts[1])
print("-" * 100)
print(texts[2])

# 각 청크가 얼마나 오버 되었는지 확인
char_list = []
for i in range(len(texts)):
  char_list.append(len(texts[i]))

print(char_list)

# 2. RecursiveCharacterSplitter
# 1000 글자를 하나의 청크로 나눔, 오버랩은 100글자
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=len,
    )

texts = text_splitter.split_text(text_gen_ai)

print(texts[0])
print("-" * 100)
print(texts[1])
print("-" * 100)
print(texts[2])

# 각 청크의 글자 수 확인
char_list = []
for i in range(len(texts)):
  char_list.append(len(texts[i]))

print(char_list)

# 토큰을 세는 패키지
!pip install tiktoken

# 토크나이저 생성
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4o-mini")

tokens = tokenizer.encode("Gu Bon Wook")

print("Tokens: ",  tokens)
print("Token Count: ", len(tokens))

# 토큰 수를 세어주는 함수
def tiktoken_len(text):
  tokens = tokenizer.encode(text)
  return len(tokens)

tiktoken_len("hello how are you?")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50,
    length_function = tiktoken_len,
)

texts = text_splitter.split_text(text_gen_ai)

char_list = []
for i in range(len(texts)):
  char_list.append(tiktoken_len(texts[i]))

print(char_list)

