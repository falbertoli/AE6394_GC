import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import os

# Sample data for graphs
fleet_data = pd.DataFrame({
    "Fleet Type": ["Hydrogen", "Jet Fuel"],
    "Percentage": [40, 60]
})
land_use_data = pd.DataFrame({
    "Category": ["Used", "Available"],
    "Area (sq. ft.)": [5000, 15000]
})

# Create a pie chart for fleet composition
fleet_chart = px.pie(
    fleet_data,
    names="Fleet Type",
    values="Percentage",
    title="Fleet Composition"
)

# Create a bar chart for land use
land_use_chart = px.bar(
    land_use_data,
    x="Category",
    y="Area (sq. ft.)",
    title="Land Use"
)

# Initialize the Dash app with Font Awesome for icons
app = dash.Dash(__name__, external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])

# Layout of the dashboard
app.layout = html.Div([
    # Header Section
    html.Div([
        html.H1("Hydrogen Infrastructure Dashboard", style={"color": "#007BFF"}),  # Blue title
        html.H3("Visualizing compliance, costs, and operational impacts"),
        html.P("This dashboard provides an overview of hydrogen infrastructure planning, including compliance, land use, and economic impact.",
               style={"fontStyle": "italic", "color": "gray"})
    ], style={"textAlign": "center", "padding": "20px"}),

    # Alerts Section
    html.Div([
        html.Div([
            html.I(className="fas fa-exclamation-circle", style={"color": "#FF0000", "marginRight": "10px", "fontSize": "24px"}),  # Red alert icon
            html.H4("Alerts", style={"display": "inline-block", "color": "#FF0000"})  # Red alert title
        ], style={"display": "flex", "alignItems": "center"}),
        html.P("Warning: Tank location violates the 75-foot safety rule", style={"color": "red"}),
        html.P("This section displays warnings or success messages based on compliance with regulations.",
               style={"fontStyle": "italic", "color": "gray"})
    ], style={"padding": "20px", "border": "2px solid #FF0000", "margin": "20px", "borderRadius": "10px"}),  # Red border for alerts

    # Map Section
    html.Div([
        html.Div([
            html.I(className="fas fa-map-marker-alt", style={"color": "#007BFF", "marginRight": "10px", "fontSize": "24px"}),  # Blue map icon
            html.H4("Interactive Map", style={"display": "inline-block", "color": "#007BFF"})  # Blue title
        ], style={"display": "flex", "alignItems": "center"}),
        html.P("This section will display an interactive map showing zones, safety buffers, and tank locations.",
               style={"fontStyle": "italic", "color": "gray"}),
        html.Div(
            "Map Placeholder (Integrate Leaflet.js or Plotly Map here)",
            style={"height": "300px", "border": "1px solid black", "textAlign": "center", "lineHeight": "300px", "borderRadius": "10px"}
        )
    ], style={"padding": "20px"}),

    # Key Metrics Section
    html.Div([
        html.Div([
            html.H4("Land Use", style={"color": "#28A745"}),  # Green title
            html.P("5,000 sq. ft. used", style={"fontWeight": "bold"}),
            html.P("This metric shows the total land area currently occupied by hydrogen infrastructure.",
                   style={"fontStyle": "italic", "color": "gray"})
        ], style={"border": "2px solid #28A745", "padding": "10px", "margin": "10px", "width": "30%", "display": "inline-block", "borderRadius": "10px"}),

        html.Div([
            html.H4("Compliance", style={"color": "#FFC107"}),  # Yellow title
            html.P("3 tanks compliant, 1 tank non-compliant", style={"fontWeight": "bold"}),
            html.P("This metric tracks how many tanks meet safety regulations.",
                   style={"fontStyle": "italic", "color": "gray"})
        ], style={"border": "2px solid #FFC107", "padding": "10px", "margin": "10px", "width": "30%", "display": "inline-block", "borderRadius": "10px"}),

        html.Div([
            html.H4("Estimated Cost", style={"color": "#17A2B8"}),  # Teal title
            html.P("$1.2M", style={"fontWeight": "bold"}),
            html.P("This is the estimated cost of implementing the current hydrogen infrastructure.",
                   style={"fontStyle": "italic", "color": "gray"})
        ], style={"border": "2px solid #17A2B8", "padding": "10px", "margin": "10px", "width": "30%", "display": "inline-block", "borderRadius": "10px"})
    ], style={"textAlign": "center"}),

    # Graph Section with Side-by-Side Layout
    html.Div([
        html.Div([
            html.I(className="fas fa-chart-bar", style={"color": "#007BFF", "marginRight": "10px", "fontSize": "24px"}),  # Blue graph icon
            html.H4("Graphs and Visualizations", style={"display": "inline-block", "color": "#007BFF"})  # Blue title
        ], style={"display": "flex", "alignItems": "center"}),
        html.P("This section displays graphs and visualizations for fleet composition and land use.",
               style={"fontStyle": "italic", "color": "gray"}),
        html.Div([
            dcc.Graph(
                figure=fleet_chart,
                config={"displayModeBar": False},
                style={"width": "48%", "display": "inline-block"}
            ),
            dcc.Graph(
                figure=land_use_chart,
                config={"displayModeBar": False},
                style={"width": "48%", "display": "inline-block"}
            )
        ], style={"display": "flex", "justifyContent": "space-between"})
    ], style={"padding": "20px"})
])

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # Use the PORT environment variable or default to 8050
    app.run_server(debug=True, host="0.0.0.0", port=port)