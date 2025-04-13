<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Azure OpenAI 기반 LangChain 실습 프로젝트</title>
</head>
<body>
  <h1>🚀 Azure OpenAI 기반 LangChain 실습 프로젝트</h1>
  <p><strong>가천대학교 SW 아카데미 6기</strong> 워크숍 실습 프로젝트입니다.</p>
  <p>LangChain과 Azure OpenAI를 활용해 문서 처리, 자연어 응답, 이미지 생성 등 고급 AI 기능을 단계적으로 학습했습니다.</p>
  <hr>

  <!-- 01 -->
  <h2>📄 01_loader.py - 문서 로딩 실습</h2>
  <p>PDF, DOCX, CSV 등 다양한 문서 포맷을 LangChain 문서 로더를 통해 불러옵니다.</p>
  <ul>
    <li>PDF: <code>PyPDFLoader</code></li>
    <li>DOCX: <code>Docx2txtLoader</code></li>
    <li>CSV: <code>CSVLoader</code></li>
  </ul>
  <pre><code>
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("sample.pdf")
pages = loader.load_and_split()
print(pages[0].page_content)
  </code></pre>

  <!-- 02 -->
  <h2>🤖 02_llm.py - Azure LLM 연동 및 질문 응답</h2>
  <p>Azure OpenAI의 GPT-4o-mini 모델과 LangChain 연동을 통해 다양한 프롬프트 응답을 테스트합니다.</p>
  <ul>
    <li>기본 질의응답</li>
    <li>창의적인 시 생성</li>
    <li>스트리밍 응답 처리</li>
  </ul>
  <pre><code>
from langchain.chat_models import AzureChatOpenAI
llm = AzureChatOpenAI(model_name="dev-gpt-4o-mini")
answer = llm.invoke("이순신 장군이 누구니?")
print(answer.content)
  </code></pre>

  <!-- 03 -->
  <h2>🧠 03_template.py - 프롬프트 템플릿</h2>
  <p>LangChain의 <code>PromptTemplate</code>과 <code>ChatPromptTemplate</code>을 사용하여 사용자 요청을 정형화된 프롬프트로 만들어줍니다.</p>
  <ul>
    <li>변수화된 프롬프트 생성</li>
    <li>템플릿 응답 조립 및 디버깅 용이</li>
  </ul>
  <pre><code>
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
print(prompt.format_prompt(topic="cats").to_string())
  </code></pre>

  <!-- 04 -->
  <h2>📚 04_splitter.py - 텍스트 분할 (Tokenizer 기반)</h2>
  <p>문서의 긴 내용을 GPT 모델 기준의 토큰 단위로 나누기 위한 실습입니다.</p>
  <ul>
    <li>토큰 길이에 따라 자동 분할</li>
    <li>중복(overlap)을 활용해 의미 보존</li>
  </ul>
  <pre><code>
from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
chunks = splitter.split_documents(pages)
  </code></pre>

  <!-- 05 -->
  <h2>🧬 05_embedding.py - Azure 기반 문서 임베딩</h2>
  <p>Azure OpenAI의 <code>text-embedding-3-small</code> 모델을 활용하여 문서를 벡터화합니다.</p>
  <pre><code>
from langchain.embeddings import AzureOpenAIEmbeddings
embedding_model = AzureOpenAIEmbeddings(model="dev-text-embedding-3-small")
vectors = embedding_model.embed_documents([chunk.page_content for chunk in docs])
  </code></pre>

  <!-- 06 -->
  <h2>🗂️ 06_vector_store.py - 벡터 저장 및 검색</h2>
  <p>문서를 벡터화한 후, <strong>Chroma DB</strong>에 저장하고 유사도 기반 검색을 수행합니다.</p>
  <ul>
    <li>벡터 저장: <code>Chroma.from_documents()</code></li>
    <li>검색: <code>similarity_search</code>, <code>similarity_search_with_relevance_scores</code></li>
  </ul>
  <pre><code>
from langchain.vectorstores import Chroma
db = Chroma.from_documents(docs, embeddings)
results = db.similarity_search("탄소중립이 뭐야?")
print(results[0].page_content)
  </code></pre>

  <!-- 07 -->
  <h2>📑 07_paper_review.py - 논문 리뷰 자동화</h2>
  <p>LLM과 Prompt Template을 이용하여 논문 내용을 요약하고, 강점/한계점 분석, 평점 매기기까지 수행합니다.</p>
  <pre><code>
template = """
너는 논문 리뷰어야. 다음 논문 내용을 보고 아래를 수행해줘:
1. 연구 목적 요약
2. 강점과 한계 정리
3. 평점 부여 (5점 기준)
논문 내용: {context}
"""
  </code></pre>

  <!-- PROJECT -->
  <h2>🎨 project.py - AI 네 컷 만화 생성기</h2>
  <p><strong>DALL·E 3 + GPT-4o-mini</strong>를 조합하여 사용자의 주제로 4컷 만화를 자동 생성하는 프로젝트입니다.</p>
  <ul>
    <li>사용자 프롬프트 입력</li>
    <li>GPT가 컷별 스토리 생성</li>
    <li>DALL·E로 각 컷 이미지를 생성</li>
    <li>전체 만화를 이어붙여 스토리 완성</li>
  </ul>
  <pre><code>
# 1. 유저 프롬프트 수집 → 컷별 스토리 작성
# 2. GPT가 컷별 묘사 생성 → 이미지 프롬프트 생성
# 3. DALL-E로 이미지 4장 생성
# 4. 네 장의 이미지를 한 장으로 합성
  </code></pre>

  <hr>
  <h2>✅ 종합 정리</h2>
  <ol>
    <li>문서 로드 → 텍스트 분할</li>
    <li>문서 임베딩 → 벡터 저장</li>
    <li>유사도 검색 → LLM으로 응답 생성</li>
    <li>LLM의 고급 프롬프트 활용 → 리뷰, 요약, 생성</li>
    <li>AI 생성 기술(DALL·E) 연동 → 시각적 스토리 제작</li>
  </ol>

  <p><em>본 워크숍은 실무에서 바로 응용 가능한 AI 기술을 중심으로 구성되었으며, 모든 코드는 LangChain + Azure 기반으로 작성되었습니다.</em></p>
</body>
</html>
