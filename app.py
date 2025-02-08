from flask import Flask, render_template, request, redirect, url_for
import datetime
import video_processing
import plotly.graph_objs as go

app = Flask(__name__)

# Sample data to simulate the activity log
activity_log = [
    {"time": "2025-02-08 10:30:00", "activity": "Fire detected"},
    {"time": "2025-02-08 11:00:00", "activity": "Crowd gathering detected"},
]

@app.route("/")
def index():
    """Main Dashboard"""
    return render_template("index.html", activities=activity_log)

@app.route("/dashboard")
def dashboard():
    #Example data for chart
    labels = ['Fire Detected', 'Smoke Detected' 'Non Fire']
    values = [1, 2, 3] # Example statistics

    # Create Pie Chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # fig.update_layout(title_text='Fire Detection Statistics')
    chart_html = fig.to_html(full_html=False)

    return render_template("dashboard.html", chart_html=chart_html)


@app.route("/live-monitor", methods=["GET", "POST"])
def live_monitor():
    """Display live feed or file monitoring"""
    if request.method == "POST":
        video_file = request.files["video"]
        video_path = "uploaded_video.mp4"
        video_file.save(video_path)

        # Process video using YOLOv8
        video_processing.process_video(video_path)

    return render_template("live_monitor.html")

@app.route("/alerts")
def alerts():
    """Alert Management"""
    return render_template("alerts.html", activities=activity_log)

if __name__ == "__main__":
    app.run(debug=True)