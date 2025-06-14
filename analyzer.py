from generate_post import generate_post

def analyze_post(post, goal, dialect="العربية الفصحى"):
    report = "# تقرير تحليل منشور لينكدن\n\n"
    result = generate_post(post, goal, dialect)
    report += result + "\n\n"
    return report
