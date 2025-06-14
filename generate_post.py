from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

TEMPLATE = """
أنت مساعد خبير في تحسين منشورات لينكدن  {dialect}. المستخدم هدفه: {goal}

إليك المحتوى:
"{content}"

قم بالتالي:
1. 🔍 تحليل أسلوب المنشور.
2. ✅ استخراج نقاط القوة والضعف.
3. 🪝 توليد ٣ Hooks مختلفة (مثل: سؤال - رقم - شيء مفاجئ).
4. 💬 توليد أول تعليق محفّز للنقاش (Comment bait).
5. ✍️ اقتراح منشور جديد بأسلوب أقوى يخدم الهدف.
6. ⏰ ما هو أفضل وقت لنشر هذا النوع من المحتوى.
7. 🧩 تحليل الجمهور المستهدف (اهتماماته، لهجته، توقّعاته).
8. 🎯 قيّم مدى توافق المنشور مع الهدف.
9. 💡 أعطِ سؤالًا تحفيزيًا لزيادة التفاعل بالتعليقات.

رجاءً رد باللغة العربية الفصحى فقط، ولا تستخدم أي لغة أخرى.
ابدأ بـ التحليل، ثم انتقل بالنقاط بالتسلسل.
"""

prompt = PromptTemplate(
    input_variables=["content", "goal", "dialect"],
    template=TEMPLATE
)

llm = ChatGroq(temperature=0.7, model_name="llama3-70b-8192")

chain = LLMChain(prompt=prompt, llm=llm)

def generate_post(content: str, goal: str, dialect: str = "العربية الفصحى") -> str:
    return chain.run({
        "content": content,
        "goal": goal,
        "dialect": dialect
    })
