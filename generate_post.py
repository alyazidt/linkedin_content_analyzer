from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

TEMPLATE = """
أنت مساعد خبير في تحسين منشورات لينكدن باللهجة {dialect}. المستخدم هدفه: {goal}

إليك المحتوى:
"{content}"

- حلل أسلوب المنشور.
- استخرج نقاط القوة والضعف فيه.
- اقترح منشور جديد بأسلوب أقوى يخدم الهدف.

ابدأ بـ التحليل، ثم المقترح.
"""

prompt = PromptTemplate(
    input_variables=["content", "goal", "dialect"],
    template=TEMPLATE
)

llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192")

chain = LLMChain(prompt=prompt, llm=llm)

def generate_post(content: str, goal: str, dialect: str = "الصُّورية") -> str:
    return chain.run({
        "content": content,
        "goal": goal,
        "dialect": dialect
    })