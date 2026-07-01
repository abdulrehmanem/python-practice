import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=['Apples', 'Bananas', 'Cherries'], y=[4, 1, 7])],
    layout_title_text="Modern Local Data Visualization"
)

# 1. Customize the Bars (Traces)
fig.update_traces(
    marker_color=['#ff4d4d', '#ffdb4d', '#cc0052'],  # Unique hex color for each bar
    marker_line_color='black',                     # Border color around bars
    marker_line_width=1.5,                         # Border width
    opacity=0.85                                   # Transparency (0 to 1)
)

# 2. Customize the Layout (Axes, Fonts, Backgrounds)
fig.update_layout(
    # Typography
    font=dict(family="Arial, sans-serif", size=14, color="#333333"),
    title_font=dict(size=22, color="#111111"),
    
    # Axes Labels and Styling
    xaxis=dict(title="Fruit Varieties", showgrid=False),
    yaxis=dict(title="Quantity (Tons)", showgrid=True, gridcolor="#e5e5e5"),
    
    # Background and Dimensions
    plot_bgcolor="white",                          # Chart area background color
    paper_bgcolor="#f8f9fa",                       # Outer canvas background color
    width=700,                                     # Width in pixels
    height=450                                     # Height in pixels
)

fig.show()
