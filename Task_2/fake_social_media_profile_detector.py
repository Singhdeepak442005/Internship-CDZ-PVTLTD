from flask import Flask, render_template, request

app = Flask(__name__)

def detect_fake_profile(followers, following, posts, profile_pic, bio):
    score = 0
    reasons = []

    if followers < 20:
        score += 1
        reasons.append("Very few followers")

    if following > followers * 5:
        score += 1
        reasons.append("Following too many accounts")

    if posts < 3:
        score += 1
        reasons.append("Very few posts")

    if profile_pic == "no":
        score += 1
        reasons.append("No profile picture")

    if len(bio.strip()) < 10:
        score += 1
        reasons.append("Bio is too short")

    if score >= 3:
        result = "⚠ Fake Profile Suspected"
    else:
        result = "✅ Profile Looks Genuine"

    return result, reasons


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    followers = int(request.form["followers"])
    following = int(request.form["following"])
    posts = int(request.form["posts"])
    profile_pic = request.form["profile_pic"]
    bio = request.form["bio"]

    result, reasons = detect_fake_profile(
        followers,
        following,
        posts,
        profile_pic,
        bio
    )

    return render_template(
        "index.html",
        result=result,
        reasons=reasons
    )


if __name__ == "__main__":
    app.run(debug=True)