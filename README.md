<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Azure-workshop</title>
</head>
<body>

  <h1>🚀 Azure-workshop</h1>
  <p><strong>가천대학교 SW 아카데미 6기</strong> - Azure OpenAI 기반 LLM을 활용한 고급 AI 솔루션 설계 및 구현 워크숍 실습 코드입니다.</p>
  <hr />

  <h1>📄 01.loader.py (LangChain 문서 로더 예제)</h1>
  <p><strong>LangChain</strong>을 활용하여 다양한 형식의 문서를 불러오는 예제입니다.</p>

  <h2>🛠️ 설치 패키지</h2>
  <pre><code>
pip install pypdf docx2txt
pip install langchain langchain-core langchain-community
  </code></pre>

  <h2>📚 불러오는 문서 종류</h2>
  <ul>
    <li><strong>PDF</strong> 파일: <code>PyPDFLoader</code></li>
    <li><strong>Word (docx)</strong> 파일: <code>Docx2txtLoader</code></li>
    <li><strong>CSV</strong> 파일: <code>CSVLoader</code></li>
  </ul>

  <hr />

  <h1>02.llm (Azure OpenAI 기반 LangChain LLM) 🤖</h1>
  <p>이 예제는 LangChain을 활용하여 Azure OpenAI LLM(GPT-4o-mini) 모델과 상호작용하는 방법을 보여줍니다.</p>

  <h2>📦 설치 패키지</h2>
  <pre><code>
pip install langchain langchain-core langchain-community
pip install openai
  </code></pre>

  <h2>🔐 환경 변수 설정</h2>
  <ul>
    <li><code>OPENAI_API_KEY</code></li>
    <li><code>AZURE_OPENAI_ENDPOINT</code></li>
    <li><code>OPENAI_API_TYPE</code>: azure</li>
    <li><code>OPENAI_API_VERSION</code>: 2023-05-15</li>
  </ul>

  <h2>🧪 주요 코드 기능</h2>

  <h3>1. 기본 질의응답</h3>
  <pre><code>
from langchain.chat_models import AzureChatOpenAI

llm = AzureChatOpenAI(model_name="dev-gpt-4o-mini")
answer = llm.invoke("이순신 장군이 누구니?")
print(answer.content)
  </code></pre>

  <h3>2. 시 생성 (창의성 조절)</h3>
  <pre><code>
llm = AzureChatOpenAI(model_name="dev-gpt-4o-mini", temperature=1)
answer = llm.invoke("가천대의 흐트러진 벗꽃을 주제로 청춘과 낭만에 대한 시를 지어줘?")
print(answer.content)
  </code></pre>

  <h3>3. 스트리밍 응답 출력</h3>
  <pre><code>
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = AzureChatOpenAI(
    model_name="dev-gpt-4o-mini",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=1,
    max_tokens=1000
)
answer = llm.invoke("가천대의 흐트러진 벗꽃을 주제로 청춘과 낭만에 대한 시를 지어줘?")
  </code></pre>

  <hr />
  <p><em>📌 본 실습은 LangChain과 Azure OpenAI 기반 LLM을 실제 프로젝트에 적용하기 위한 실습 예제입니다.</em></p>

</body>
</html>
