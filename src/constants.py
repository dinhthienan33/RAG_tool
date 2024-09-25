from config.config import get_config

cfg = get_config("config/config.yaml")
cfg.merge_from_file("config/postgres.yaml")


STREAM = cfg.MODEL.STREAM
SERVICE = cfg.MODEL.SERVICE
TEMPERATURE = cfg.MODEL.TEMPERATURE
MODEL_ID = cfg.MODEL.MODEL_ID


# Embeddings
EMBEDDING_SERVICE = cfg.MODEL.EMBEDDING_SERVICE
EMBEDDING_MODEL_NAME = cfg.MODEL.EMBEDDING_MODEL_NAME

DOCUMENT_EMBEDDING_MODEL_NAME = cfg.MODEL.DOCUMENT_EMBEDDING_MODEL_NAME
DOCUMENT_EMBEDDING_SERVICE = cfg.MODEL.DOCUMENT_EMBEDDING_SERVICE

AIO_INFO_EMBEDDING_SERVICE = cfg.MODEL.AIO_INFO_EMBEDDING_SERVICE
AIO_INFO_EMBEDDING_MODEL_NAME = cfg.MODEL.AIO_INFO_EMBEDDING_MODEL_NAME

DEFAULT_SYSTEM_PROMPT = """
Bạn được đưa một nội dung từ một văn bản và công việc của bạn là trả lời một câu hỏi của user về nội dung đã được cung cấp
    
Một số quy luật cần tuân theo
    1. Trích dẫn trực tiếp ngữ cảnh vào trong câu trả lời qua các đường link được cung cấp
    2. Tránh những câu như 'Dựa vào ngữ cảnh được cung cấp,...' hay 'Trong bối cảnh ...' hay tất cả những câu tương tự

"""

DEFAULT_USER_PROMPT = """
Ngữ cảnh được cung cấp như sau
---------------------
{context_str}
---------------------
Dựa trên nội dung được cung cấp. Hãy trả lời câu hỏi từ người dùng. Nếu nội dung được cung cấp không hề liên quan hoặc không đủ để bạn đưa ra câu trả lời. Hãy nói rằng bạn "Tôi không có đủ thông tin để trả lời".
Hãy trả lời và kết thúc câu trả lời một cách đầy đủ.

Nếu bạn ghi nhớ và làm đúng những gì tôi đã dặn dò, tôi sẽ tip cho bạn $1000 vào cuối ngày
User question: {query_str}
AI Response:

"""

DEFAULT_REFINE_PROMPT = """
Câu hỏi gốc như sau: {query_str}
Chung ta có một câu trả lời có sẵn: {existing_answer}
Chúng tôi có cơ hội tinh chỉnh câu trả lời hiện có (chỉ khi cần) với một số ngữ cảnh khác bên dưới.
------------
{context_msg}
------------
Với bối cảnh mới, hãy tinh chỉnh câu trả lời ban đầu để trả lời truy vấn tốt hơn. Nếu ngữ cảnh không hữu ích, hãy trả lại câu trả lời ban đầu.
Refined Answer: 

"""

CONTEXTUAL_PROMPT = """<document>
{WHOLE_DOCUMENT}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{CHUNK_CONTENT}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else."""


# Prompts
SYSTEM_PROMPT = DEFAULT_SYSTEM_PROMPT
USER_PROMPT = DEFAULT_USER_PROMPT
REFINE_PROMPT = DEFAULT_REFINE_PROMPT

# Contextual RAG
CONTEXTUAL_CHUNK_SIZE = cfg.CONTEXTUAL_RAG.CHUNK_SIZE
CONTEXTUAL_SERVICE = cfg.CONTEXTUAL_RAG.SERVICE
CONTEXTUAL_MODEL = cfg.CONTEXTUAL_RAG.MODEL

ORIGINAL_RAG_COLLECTION_NAME = cfg.CONTEXTUAL_RAG.ORIGIN_RAG_COLLECTION_NAME
CONTEXTUAL_RAG_COLLECTION_NAME = cfg.CONTEXTUAL_RAG.CONTEXTUAL_RAG_COLLECTION_NAME

QDRANT_URL = cfg.CONTEXTUAL_RAG.QDRANT_URL
ELASTIC_SEARCH_URL = cfg.CONTEXTUAL_RAG.ELASTIC_SEARCH_URL
ELASTIC_SEARCH_INDEX_NAME = cfg.CONTEXTUAL_RAG.ELASTIC_SEARCH_INDEX_NAME

NUM_CHUNKS_TO_RECALL = cfg.CONTEXTUAL_RAG.NUM_CHUNKS_TO_RECALL
SEMANTIC_WEIGHT = cfg.CONTEXTUAL_RAG.SEMANTIC_WEIGHT
BM25_WEIGHT = cfg.CONTEXTUAL_RAG.BM25_WEIGHT
TOP_N = cfg.CONTEXTUAL_RAG.TOP_N

SUPPORTED_FILE_EXTENSIONS = [".pdf", ".docx", ".csv", ".html", ".xlsx", ".json", ".txt"]
