import json 
import PyPDF2
from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app= Flask(__name__)
CORS(app)
# def extract_text(pdf_file:str)-> [str]: # type: ignore
#     with open(pdf_file,'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf,strict=False)
#         pdf_text = []

#         for page in reader.pages:
#             content = page.extract_text()
#             pdf_text.append(content)
#         return pdf_text

client = Groq(
    api_key = "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"
)

json_format = {
    "1": {
        "mcq": "multiple choice question",
        "option": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    },
    "2": {
        "mcq": "multiple choice question",
        "option": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    },
    "3": {
        "mcq": "multiple choice question",
        "option": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    }

}

@app.route("/generate-exam", methods=["POST"])
def generate_exam():

    data = request.get_json()

    mcqMaterial= data["material"]
    mcqNumber = data["mcqNum"]
    mcqOptionNum=data["optionNum"]
    mcqDifficulty= data["difficulty"]
    
    # extracted_text = extract_text('convert.pdf')
    # text = ""
    # for i in extracted_text:
    #     text+=i

    chat_completion = client.chat.completions.create(

        model= "llama3-70b-8192",
        messages= [
            {"role":"system","content":"You are an exam master"},
            {"role":"user","content": f"generate {mcqNumber} {mcqDifficulty} multiple choice questions from this {mcqMaterial}, each question should have {mcqOptionNum} options, return it in a json format like this {json_format} without any additional text or explanation and without introductory text like here is a ...questions ."},        ],  
     )
    
    responseData = json.loads(chat_completion.choices[0].message.content)
    # output_file_path = 'responseData.json'

    # with open(output_file_path, 'w') as json_file:
    #     json.dump(responseData, json_file, indent=4)

    return responseData,201


    # mcq_text = chat_completion.choices[0].message.content  # Assuming consistent structure
    # return jsonify({"mcq": mcq_text}), 201  # Return only the MCQ in a dictionary

if __name__ == "__main__":
    app.run(debug=True)

# print(chat_completion.choices[0].message.content)
# import json 
# import PyPDF2
# import os 
# from groq import Groq
# from flask import Flask, request, jsonify

# app= Flask(__name__)


# def extract_text(pdf_file:str)-> [str]:
#     with open(pdf_file,'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf,strict=False)
#         pdf_text = []

#         for page in reader.pages:
#             content = page.extract_text()
#             pdf_text.append(content)
#         return pdf_text
    

# client = Groq(
#     api_key = "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"
# )

# json_format = {
#     "1": {
#         "mcq": "multiple choice question",
#         "option": {
#             "a": "choice here",
#             "b": "choice here",
#             "c": "choice here",
#             "d": "choice here"
#         },
#         "correct": "correct answer"
#     },
#     "2": {
#         "mcq": "multiple choice question",
#         "option": {
#             "a": "choice here",
#             "b": "choice here",
#             "c": "choice here",
#             "d": "choice here"
#         },
#         "correct": "correct answer"
#     },
#     "3": {
#         "mcq": "multiple choice question",
#         "option": {
#             "a": "choice here",
#             "b": "choice here",
#             "c": "choice here",
#             "d": "choice here"
#         },
#         "correct": "correct answer"
#     }

# }

# @app.route("/generate-exam", methods=["POST"])
# def generate_exam():
#     if request.method == "POST":

#         extracted_text = extract_text('convert.pdf')
#         text = ""
#         for i in extracted_text:
#             text+=i


#         chat_completion = client.chat.completions.create(

#             model= "llama3-70b-8192",
#             messages= [
#                 {"role":"system","content":"You are an exam master"},
#                 {"role":"user","content": f"generate 10 easy multiple choice questions from this {text}, each question should have 3 options, return it in a json format like this ${json_format}"},
#             ],  
#         )
#         return jsonify(chat_completion.choices[0].message.content),200

# if __name__ == "__main__":
#     app.run(debug=True)

# # print(chat_completion.choices[0].message.content)