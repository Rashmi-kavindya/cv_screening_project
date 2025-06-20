from flask import Flask, request, render_template
from utils.extractor import extract_text
from utils.screener import score_cv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screen_cv', methods=['POST'])
def screen_cv():
    file = request.files['cv_file']
    jd = request.form['job_desc']

    cv_text = extract_text(file)
    score = score_cv(cv_text, jd)

    if score >= 70:
        result = f"✅ CV matched {score}% – Suitable Candidate"
    elif score >= 50:
        result = f"⚠️ CV matched {score}% – Consider Carefully"
    else:
        result = f"❌ CV matched only {score}% – Not a Good Fit"

    return render_template('index.html', result=result, score=score)

if __name__ == '__main__':
    app.run(debug=True)
