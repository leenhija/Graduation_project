import json 
import PyPDF2
# import os 
from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="",database="loginusers")
if connection.is_connected():
    print('connected')
else:
    print('faild to connect to database')
app= Flask(__name__)
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":"*"
    }
})
# function for converting PDF files into Text files to send it to the GroqAPI
def extract_text(pdf_file:str)-> [str]: # type: ignore
    with open(pdf_file,'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf,strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
        return pdf_text
    

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

    data = request.get_json() #here we get the data

    exam_material = ""

    # Handling text
    if data["text"].strip() != "":
        exam_material = data["text"]

    elif data["sendFile"].strip() != "":
        PDF_Path = data["sendFile"]

        #converting the file from PDF format into text format 
        extracted_text = extract_text( PDF_Path)
        # exam_material = "".join( extracted_text)
        for i in extracted_text:
            exam_material+=i
    else:
        exam_material = None

    # difficulty for each MCQ
    easy_mcq = data["easy"]
    mid_mcq = data["mid"]
    hard_mcq= data["hard"]

    # Number of options 
    optionNum = data["numOfOptions"]
    
    

    # chat_completion = client.chat.completions.create(

    #     model= "llama3-70b-8192",
    #     messages= [
    #         {"role":"system","content":"You are an exam master"},
    #         {"role":"user","content": f"generate {easy_mcq} easy, {mid_mcq} medium, and {hard_mcq} multiple choice questions from this {exam_material}, each question should have {optionNum} options, return it in a json format like this {json_format} with double quotes only not single quotes without any additional text or explanation and without introductory text like here is a ...questions and don't write something like this: *Easy Questions (5)* or like this:Here are the questions:, and use double quotes only not single quotes"},        ],  
    #  )
    chat_completion = client.chat.completions.create(

        model= "llama3-70b-8192",
        messages= [
            {"role":"system","content":"You are an expert MCQ maker."},
            {
            "role": "user",
            "content": f"Generate a set of multiple choice questions based on the following material: {exam_material}. "
                       f"Please specify the difficulty and number of questions: \n"
                       f"- *Easy:* {easy_mcq} questions\n"
                       f"- *Medium:* {mid_mcq} questions\n"
                       f"- *Hard:* {hard_mcq} questions\n"
                       f"Each question should have {optionNum} answer choices (including the correct answer). "
                       f"the output should be a JSON object in the following format:\n"
                       f"{json_format}\n"
                       f"Respond with only the JSON object, without any additional text."
            },   
        ],  
     )
    responseData = json.loads(chat_completion.choices[0].message.content)
    # output_file_path = 'responseData.json'

    # with open(output_file_path, 'w') as json_file:
    #     json.dump(responseData, json_file, indent=4)

    return responseData,201


    # mcq_text = chat_completion.choices[0].message.content  # Assuming consistent structure
    # return jsonify({"mcq": mcq_text}), 201  # Return only the MCQ in a dictionary

if __name__ == "__main__":
    app.run(debug=True,port=5173)

# print(chat_completion.choices[0].message.content)