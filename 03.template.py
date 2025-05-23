# -*- coding: utf-8 -*-
"""03.template.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LbsxxTAkRlPw1zmCeQK5jI96I3DOalW_
"""

!pip install langchain langchain-core langchain-community
!pip install openai

from langchain.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chat_prompt_value = chat_prompt.format_prompt(topic="cats")

print(chat_prompt_value.to_string())
