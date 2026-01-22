from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>IST Digital Clock</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: #0b1c2d; /* navy blue */
            color: #f5f7fa;      /* soft white */
            font-family: "Segoe UI", Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .clock-box {
            padding: 40px 60px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.05);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            font-weight: 400;
            letter-spacing: 2px;
            font-size: 22px;
            opacity: 0.85;
        }

        .clock {
            font-size: 64px;
            letter-spacing: 4px;
            font-weight: 500;
        }

        .zone {
            margin-top: 12px;
            font-size: 14px;
            opacity: 0.7;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>

<div class="clock-box">
    <h1>DIGITAL CLOCK</h1>
    <div class="clock" id="time">00:00:00</div>
    <div class="zone">IST (Indian Standard Time)</div>
</div>

<script>
    function updateClock() {
        const now = new Date();

        // Convert to IST (UTC + 5:30)
        const utc = now.getTime() + now.getTimezoneOffset() * 60000;
        const istTime = new Date(utc + (5.5 * 60 * 60 * 1000));

        const hours = String(istTime.getHours()).padStart(2, '0');
        const minutes = String(istTime.getMinutes()).padStart(2, '0');
        const seconds = String(istTime.getSeconds()).padStart(2, '0');

        document.getElementById("time").innerText =
            `${hours}:${minutes}:${seconds}`;
    }

    setInterval(updateClock, 1000);
    updateClock();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
