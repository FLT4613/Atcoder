from requests import get
from pyquery import PyQuery as pq
from pathlib import Path

user_id = 'FLT'
submission_list_url = 'https://atcoder.jp/contests/{}/submissions?f.User=' + user_id

# crawl
res = get(f'https://kenkoooo.com/atcoder/atcoder-api/results?user={user_id}')
res.raise_for_status()
res = res.json()

# Get submission details
submission_urls = []
for contest in [x['contest_id'] for x in res if x['result'] == "AC"]:
    url = submission_list_url.format(contest)
    html = pq(url)
    tr = html('#main-container > div.row > div:nth-child(3) > div.panel.panel-default.panel-submission > div.table-responsive > table > tbody > tr')
    for el in tr[::-1]:
        if pq(el[6]).text() == 'AC':
            url = pq(el[9]).children('a').attr('href')
            submission_urls.append(url)
            print(url)
# parse
parsed = []
for url in submission_urls:
    html = pq(f'https://atcoder.jp{url}')
    contest_id = html('.contest-title').attr('href').split('/')[-1]
    code = html('.linenums').html()
    title = html('.panel > table > tr:nth-child(2) > td').text().replace(' ', '_')
    print(f'{title}')
    parsed.append({
        'contest_id': contest_id,
        'title': title,
        'code': code,
    })

# mkfile
root_dirname = 'atcoder'
Path(root_dirname).mkdir(exist_ok=True)

for item in parsed:
    path = Path(root_dirname+f'/{item["contest_id"]}')
    path.mkdir(exist_ok=True)
    with (path/(item['title'][0]+'.py')).open(mode='w') as f:
        f.write(item['code'])
