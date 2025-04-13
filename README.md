# Azure-workshop
가천대학교-sw아카데미 6기-Azure OpenAI 기반 LLM을 활용한 고급 AI 솔루션 설계 및 구현


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
