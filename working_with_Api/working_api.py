import requests
import plotly.graph_objects as go



url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f'Status code:{r.status_code}\n')

response_dict = r.json()

# print(f'Total repositories : {response_dict['total_count']}')

repo_dicts = response_dict['items']

repo_names,repo_stars,repo_des = [],[],[]

# print(f"repositories returned:{len(repo_dicts)}")

# repo_dict = repo_dicts[0]
# print(f'\n keys: {len(repo_dict)}')
# for repo_dict in repo_dicts:
#     print(f'Name: {repo_dict['name']}')
#     print(f'Owner: {repo_dict['owner']['login']}')
#     print(f'Stars: {repo_dict['stargazers_count']}')
#     print(f'Repository: {repo_dict['html_url']}')
#     print(f'Created: {repo_dict['created_at']}')
#     print(f'Updated: {repo_dict['updated_at']}')
#     print(f'Description: {repo_dict['owner']['login']}\n')

for item in repo_dicts:
    repo_stars.append(item['stargazers_count'])
    r_name = item['name']
    r_url = item['html_url']
    r_des = f"{item['owner']['login']}<br >{item['description']}"

    href_name = f"<a href='{r_url }'>{r_name}</a>"

    repo_names.append(href_name)
    repo_des.append(r_des)


# print(repo_names)
# print(repo_stars)


# Build the layout structure 
fig = go.Figure(
    data=[go.Bar(x=repo_names, y=repo_stars, customdata=repo_des, 
    hovertemplate="<b>Stars:</b> %{y}<br><b>Description:</b> %{customdata}<extra></extra>")],
    layout_title_text="Modern Local Data Visualization"
)

fig.update_layout(
    # Typography
    font=dict(family="Arial, sans-serif", size=16, color="#111111"),
    title_font=dict(size=28, color="#363232"),
    
    # Axes Labels and Styling
    xaxis=dict(title="Repositories", showgrid=False),
    yaxis=dict(title="Stars", showgrid=True, gridcolor="#e5e5e5"),
    
    # Background and Dimensions
    plot_bgcolor="white",                          # Chart area background color
    paper_bgcolor="#f8f9fa"                      # Outer canvas background color
    # width=700,                                     # Width in pixels
    # height=450                                     # Height in pixels
)

# Open an interactive window locally on your machine
fig.show()