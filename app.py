# app.py
import dash
from dash import html
import dash_bootstrap_components as dbc

# -----------------------------------------------------------------------------
# Dash app setup
# -----------------------------------------------------------------------------
app = dash.Dash(
    __name__,
    use_pages=True,                             # 🔑 turn on multi-page support
    external_stylesheets=[dbc.themes.BOOTSTRAP] # any Bootswatch theme works
)
server = app.server                              # for gunicorn / Heroku etc.

# print(dash.page_registry.keys())  # 👉 check the page registry to see what it looks like

# -----------------------------------------------------------------------------
# Navigation bar (auto-build links from the page registry)
# -----------------------------------------------------------------------------
navbar = dbc.NavbarSimple(
    brand="Stocks Dashboard",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink(children=page["name"], href=page["path"]))
        for page in dash.page_registry.values()
    ],
)

# -----------------------------------------------------------------------------
# Top-level layout: navbar + whatever page is requested
# -----------------------------------------------------------------------------
app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        dash.page_container,  # 🔑 this is whereimport dash
    ],
    fluid=True,
)

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
