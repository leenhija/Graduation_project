# import json 
# import PyPDF2
# # import os 
# from groq import Groq
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import re
# import mysql.connector
# from datetime import datetime
# connection=mysql.connector.connect(host="localhost",user="root",password="",database="rapidly")
# if connection.is_connected():
#     print('connected')
# else:
#     print('faild to connect to database')


# #cursor object
# mycursor= connection.cursor()

# app= Flask(__name__)
# CORS(app)
# cors=CORS(app,resources={
#     r"/*":{
#         "origins":"*"
#     }
# })
# # function for converting PDF files into Text files to send it to the GroqAPI
# def extract_text(pdf_file:str)-> [str]: # type: ignore
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
# # @app.route("/upload", methods=["POST"])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file part'}), 400

# #     file = request.files['file']

# #     if file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400

# #     if file and file.filename.endswith('.pdf'):
# #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
# #         file.save(file_path)  # Save the file to a local path
# #         return jsonify({'file_path': file_path})

# #     return jsonify({'error': 'Invalid file type'}),400

# @app.route("/generate-exam", methods=["POST"])
# def generate_exam():
#  try:

#     data = request.get_json() #here we get the data
#     print(data)
#     exam_material = ""

#     # Handling text
#     if data["text"].strip() != "":
#         exam_material = data["text"]

#     elif data["sendFile"].strip() != "":
#         PDF_Path = data["sendFile"]

#         #converting the file from PDF format into text format 
#         extracted_text = extract_text( PDF_Path)
#         # exam_material = "".join( extracted_text)
#         for i in extracted_text:
#             exam_material+=i
#     else:
#         exam_material = None

#     # difficulty for each MCQ
#     easy_mcq = data["easy"]
#     mid_mcq = data["mid"]
#     hard_mcq= data["hard"]

#     # Number of options 
#     optionNum = data["numOfOptions"]
    
#     exam_name= data["examName"]
#     user_id = data["userId"]
#     created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     #sending to the database 
#     # exam_id= 12

#     #sending to the database 
#     mycursor.execute("INSERT INTO exam (ExamName, CreatedAt, userID) VALUES (%s, %s, %s)",(exam_name,created_at,user_id))
#     # mycursor.execute("INSERT INTO exam (ExamName, CreatedAt, userID) VALUES (%s,%s, %s, %s)",(exam_name, created_at,user_id))
#     # Get the last inserted ExamID
#     exam_id = mycursor.lastrowid
#     connection.commit()
#     # chat_completion = client.chat.completions.create(

#     #     model= "llama3-70b-8192",
#     #     messages= [
#     #         {"role":"system","content":"You are an exam master"},
#     #         {"role":"user","content": f"generate {easy_mcq} easy, {mid_mcq} medium, and {hard_mcq} multiple choice questions from this {exam_material}, each question should have {optionNum} options, return it in a json format like this {json_format} with double quotes only not single quotes without any additional text or explanation and without introductory text like here is a ...questions and don't write something like this: *Easy Questions (5)* or like this:Here are the questions:, and use double quotes only not single quotes"},        ],  
#     #  )
#     chat_completion = client.chat.completions.create(

#         model= "llama3-70b-8192",
#         messages= [
#             {"role":"system","content":"You are an expert MCQ maker."},
#             {
#             "role": "user",
#             "content": f"Generate a set of multiple choice questions based on the following material: {exam_material}. "
#                        f"Please specify the difficulty and number of questions: \n"
#                        f"- *Easy:* {easy_mcq} questions\n"
#                        f"- *Medium:* {mid_mcq} questions\n"
#                        f"- *Hard:* {hard_mcq} questions\n"
#                        f"Each question should have {optionNum} answer choices (including the correct answer). "
#                        f"the output should be a JSON object in the following format:\n"
#                        f"{json_format}\n"
#                        f"Respond with only the JSON object, without any additional text."
#             },   
#         ],  
#      )
#     responseData = json.loads(chat_completion.choices[0].message.content)
#     print(responseData)
#     # print(responseData)
#     # output_file_path = 'responseData.json'
#     # question_id=0
#     # option_id=0
#     for key, question_data in responseData.items():
#         question_text = question_data["mcq"]
#         # question_id+=1
#         mycursor.execute("INSERT INTO qustions (Qustion, ExamID) VALUES (%s,%s)", (question_text,exam_id))
#         question_id = mycursor.lastrowid
#         options= question_data["option"]
#         for option_key, option_text in options.items():
#             # option_id+=1
#             mycursor.execute(
#                 "INSERT INTO options (option,qustionID) VALUES (%s,%s)",
#                 (option_text, question_id))
#     # with open(output_file_path, 'w') as json_file:
#     #     json.dump(responseData, json_file, indent=4)
#     #sending the data from the database to the frontend:
#     # Fetch questions for the exam
#     # connection.commit()
#     # mycursor.execute("SELECT * FROM qustions WHERE ExamID = %s", (exam_id,))
#     # # connection.commit()
#     # questions = mycursor.fetchall()
#     # print(questions)
#    # Fetch options for each question
#     # exam_data = {}

#     # for question in questions:
#     #     question_id = mycursor.lastrowid 
      
#     #     mycursor.execute("SELECT * FROM options WHERE qustionID = %s", (question_id,))
#     #     options = mycursor.fetchall()
        

#     #     options_list =[ {"optionID": opt[0], "optionText": opt[1], "qustionID": opt[2]} for opt in options]

#     #     #Construct the response data structure
#     #     exam_data["ExamID"]=exam_id
#     #     exam_data["question"]=question
#     #     exam_data["options"]=options
#     #     exam_data["questionID"]=question_id
#     # connection.commit()
#     # return jsonify(exam_data),200
#     return responseData,201
#  except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({'error': 'An error occurred while generating the exam'}), 500

#     # mcq_text = chat_completion.choices[0].message.content  # Assuming consistent structure
#     # return jsonify({"mcq": mcq_text}), 201  # Return only the MCQ in a dictionary

# if __name__ == "__main__":
#     app.run(debug=True,port=5173)

# # print(chat_completion.choices[0].message.content)
import json 
import PyPDF2
# import os 
from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import mysql.connector
from datetime import datetime
connection=mysql.connector.connect(host="localhost",user="root",password="",database="rapidly")
if connection.is_connected():
    print('connected')
else:
    print('faild to connect to database')


#cursor object
mycursor= connection.cursor()

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
    try:
        data = request.get_json()  # here we get the data
        exam_material = ""

        # Handling text
        if data["text"].strip() != "":
            exam_material = data["text"]

        elif data["sendFile"].strip() != "":
            PDF_Path = data["sendFile"]
            # converting the file from PDF format into text format 
            extracted_text = extract_text(PDF_Path)
            for i in extracted_text:
                exam_material += i
        else:
            exam_material = None

        # difficulty for each MCQ
        easy_mcq = data["easy"]
        mid_mcq = data["mid"]
        hard_mcq = data["hard"]

        # Number of options 
        optionNum = data["numOfOptions"]

        exam_name = data["examName"]
        user_id = data["userId"]
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # sending to the database 
        mycursor.execute("INSERT INTO exam (ExamName, CreatedAt, userID) VALUES (%s, %s, %s)", (exam_name, created_at, user_id))
        exam_id = mycursor.lastrowid
        connection.commit()

        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are an expert MCQ maker."},
                {
                    "role": "user",
                    "content": f"Generate a set of multiple choice questions based on the following material: {exam_material}. "
                               f"Please specify the difficulty and number of questions: \n"
                               f"- *Easy:* {easy_mcq} questions\n"
                               f"- *Medium:* {mid_mcq} questions\n"
                               f"- *Hard:* {hard_mcq} questions\n"
                               f"Each question should have {optionNum} answer choices (including the correct answer). "
                               f"The output should be a JSON object in the following format:\n"
                               f"{json_format}\n"
                               f"Respond with only the JSON object, without any additional text."
                },
            ],
        )

        # Debugging: Print the raw response content
        raw_response = chat_completion.choices[0].message.content
        print("Raw Response:", raw_response)

        # Clean and validate the JSON structure
        raw_response = raw_response.strip()
        if raw_response.startswith('```json'):
            raw_response = raw_response[7:]
        if raw_response.endswith('```'):
            raw_response = raw_response[:-3]
        raw_response = raw_response.strip()

        try:
            responseData = json.loads(raw_response)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print("Raw Response for Debugging:", raw_response)
            return jsonify({"error": "Invalid JSON response from API"}), 500

        print(responseData)

        for key, question_data in responseData.items():
            question_text = question_data["mcq"]
            mycursor.execute("INSERT INTO qustions (Qustion, ExamID) VALUES (%s, %s)", (question_text, exam_id))
            question_id = mycursor.lastrowid
            options = question_data["option"]
            for option_key, option_text in options.items():
                mycursor.execute(
                    "INSERT INTO options (option, qustionID) VALUES (%s, %s)",
                    (option_text, question_id))
        
        connection.commit()
        return jsonify(responseData), 201

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return jsonify({"error": "Invalid JSON response"}), 500
    except Exception as e:
        print(f"Something else went wrong: {e}")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5173)
