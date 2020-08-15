import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions": []
}

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    vote_count = que.select_one('.vote-count-post').getText()
    views = que.select_one('.views').attrs['title']
    tags = [tag.getText() for tag in (que.select('.post-tag'))]
    time = que.select_one(".relativetime").getText()
    askedby = que.select_one(".user-details").a.getText()
    avatar = que.select_one(".user-gravatar32").a.attrs["href"]
    
    questions_data['questions'].append({
        "question": q,
        "views": views,
        "vote_count": vote_count,
        "tags": tags,
        "time": time,
        "askedby": askedby,
        # "avatar": f"https://stackoverflow.com/{avatar}"
    })

json_data = json.dumps(questions_data, sort_keys=True, indent=4)

# pprint(questions_data)
print(json_data)
