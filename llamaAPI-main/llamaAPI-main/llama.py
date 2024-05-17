# from  llamaapi import LlamaAPI
# from dotenv import load_dotenv
# import json 
# import PyPDF2


# #pdf to text
# def extract_text(pdf_file:str)-> [str]: # type: ignore
#     with open(pdf_file,'rb') as pdf:
#         reader = PyPDF2.PdfReader(pdf,strict=False)
#         pdf_text = []

#         for page in reader.pages:
#             content = page.extract_text()
#             pdf_text.append(content)
#         return pdf_text
    
# extracted_text = extract_text('convert.pdf')
# text = ""
# for i in extracted_text:
#     text+=i

# load_dotenv()
# llama = LlamaAPI(os.getenv("LLAMA_API_TOKEN"))

# api_request_json={
#     "model": "llama3-70b",
#     "messages": [
#         {"role":"system","content":"You are an exam master"},
#         {"role":"user","content": f"generate 10 multiple choice questions from this {text}"},
#     ]
# }

# response = llama.run(api_request_json)
# print(json.dumps(response.json()['choices'][0]['message']['content'],indent=2).replace('"',''))