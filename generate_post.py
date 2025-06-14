from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

TEMPLATE = """
أنت مساعد خبير في تحسين منشورات لينكدن  {dialect}. المستخدم هدفه: {goal}

إليك المحتوى:
"{content}"

رجاءً قسّمه إلى الأجزاء التالية:

١. تحليل أسلوب المنشور الحالي:
   - نوع النبرة، أسلوب السرد، مدى وضوح الرسالة.
   - نقاط القوة.
   - نقاط الضعف.

٢. منشور محسّن يخدم الهدف:
   - بنفس الفكرة ولكن بأسلوب أقوى، منظم أكثر، وله تأثير واضح.

٣. جملة بداية جذابة (Hook):
   - تُلفت انتباه القارئ خلال أول ٣ ثوانٍ.

٤. Call-to-Action واضح:
   - مثل: "وش رأيكم؟" أو "وش أكثر شي شد انتباهك؟"

٥. سؤال تحفيزي ختامي (لزيادة التعليقات)

٦. هاشتاقات مقترحة:
   - ٥ إلى ٧ هاشتاقات مناسبة ومحدّثة

٧. ملخص جذاب (Meta Caption):
   - سطر واحد يلخص المنشور ويمكن استخدامه كعنوان

٨. اقتراح توقيت النشر:
   - الوقت الأفضل للنشر لتحقيق تفاعل أعلى

٩. نسخة قصيرة:
   - تصلح لـ Story أو Reel مكتوبة باللهجة المطلوبة


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
