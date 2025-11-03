from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dhruv Doshi - Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 60px 50px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 800px;
            width: 100%;
        }
        h1 {
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #667eea;
            font-size: 1.3em;
            margin-bottom: 30px;
            font-weight: 500;
        }
        .intro {
            color: #555;
            font-size: 1.1em;
            line-height: 1.8;
            margin-bottom: 30px;
        }
        .skills {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin-top: 30px;
        }
        .skills h2 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.5em;
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .skill-tag {
            background: #667eea;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            color: #777;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hi, I'm Dhruv Doshi</h1>
        <div class="subtitle">Aspiring Software Engineer from Symbiosis</div>
        
        <div class="intro">
            <p>I'm passionate about using technology to solve real-world problems. I'm a naturally curious person, which helps me to quickly learn and adapt to new tools and technologies.</p>
        </div>
        
        <div class="skills">
            <h2>Areas of Interest</h2>
            <div class="skills-list">
                <span class="skill-tag">Java Backend Development</span>
                <span class="skill-tag">DevOps</span>
                <span class="skill-tag">Cloud Computing</span>
            </div>
        </div>
        
        <div class="intro" style="margin-top: 30px;">
            <p>I've worked on 3–4 major projects, where I applied my skills to build practical, impactful solutions.</p>
        </div>
        
        <div class="footer">
            <p>Building the future, one project at a time.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)