from google import genai

client = genai.Client(api_key="AIzaSyDrVB9PAdJDv8HQMOrrYWJnetUIWCoKl2I4")

for model in client.models.list():
    print(model.name)