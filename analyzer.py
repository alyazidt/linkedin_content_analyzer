from generate_post import generate_post

def analyze_posts(posts, goal, dialect):
    report = "# تقرير تحليل منشورات لينكدن\n\n"
    for i, post in enumerate(posts):
        report += f"## منشور {i+1}\n"
        result = generate_post(post, goal, dialect)
        report += result + "\n\n---\n\n"
    return report