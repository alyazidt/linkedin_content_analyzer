from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

TEMPLATE = """
أنت مساعد خبير في تحسين منشورات لينكدن  {dialect}. المستخدم هدفه: {goal}

إليك المحتوى:
"{content}"

رجاءً قسّمه إلى الأجزاء التالية مع التنسيق واللغة العربية الفصحى:

---
# 📄 التقرير الكامل لتحليل المنشور

### ١. تحليل أسلوب المنشور الحالي:
- نوع النبرة:
- أسلوب السرد:
- مدى وضوح الرسالة:

#### نقاط القوة:
- 
- 

#### نقاط الضعف:
- 
- 

---

### ٢. تحسينات مقترحة لمنشور أكثر تأثيرًا وتفاعلاً:

#### جملة بداية جذابة (Hook):
> 

#### دعوة لاتخاذ إجراء (Call-to-Action):
> 

#### سؤال تحفيزي ختامي:
> 

#### هاشتاقات مقترحة:
> 

#### ملخص جذاب (Meta Caption):
> 

#### اقتراح توقيت النشر:
> 

#### نسخة قصيرة مناسبة لـ Story أو Reel:
> 

---

### ٣. المنشور المحسن المقترح:

> 

---

### ملخص:
باختصار، هذا المنشور الجديد يدمج بين جذب القارئ، عرض محتوى واضح، ودعوة تفاعل مباشرة، بالإضافة إلى استخدام هاشتاقات مدروسة واقتراح توقيت النشر.

---

أرجو أن يكون التنسيق واضحًا وجذابًا.
رجاءً رد باللغة العربية الفصحى فقط، ولا تستخدم أي لغة أخرى.
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
