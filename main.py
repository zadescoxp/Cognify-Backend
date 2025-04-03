from flask import Flask, request, jsonify
from flask_cors import CORS
import videoInfo
from google.genai.types import (
    Tool,
    GenerateContentConfig,
    GoogleSearch,
    Content,
    Part,
    FileData,
)
import videoInfo
from config import client

app = Flask(__name__)
CORS(app)

# @app.route("/analyze_video", methods=["POST"])
# def analyze_video():
#     try:
#         video_url = request.json.get("video_url")
#         if not video_url:
#             return jsonify({"error": "Missing video_url"}), 400

#         response = client.models.generate_content(
#             model="models/gemini-2.0-flash",
#             contents=Content(
#                 parts=[
#                     Part(
#                         text="""Analyse the YouTube video provided and share the title,
#                         write a detailed summary of the whole topic ,
#                         create a proper detailed blog on it, it should follow a format

#                         <title>[Title goes here]</title>

#                         <summary>[Summary goes here]</summary>

#                         <blog>[Blog goes here]</blog> ( in the blog portion make it in markdown format )

#                         that's it nothing more than that. Not a single text like 'okay here is a summary'"""
#                     ),
#                     Part(file_data=FileData(file_uri=video_url)),
#                 ]
#             ),
#         )
#         return jsonify({"blog_post": response.text})

#     except Exception as e:
#         print(e)
#         return jsonify({"error": str(e)}), 500


@app.route("/video", methods=["POST"])
def video():
    try:
        video_url = request.json.get("video_url")
        if not video_url:
            return jsonify({"error": "Missing video_url"}), 400

        result = videoInfo.get_details(video_url)
        return jsonify(
            {
                "title": result[0],
                "summary": result[1],
                "blog": result[2],
                "article": result[3],
            }
        )
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
