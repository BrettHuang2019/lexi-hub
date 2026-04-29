
Create a gemini api balance caller that balance the workflow by rate limit to different models. 

provide a config file that the user will write down the rate limite. 


api key in .env file.

# Code Snippet

pip install -q -U google-genai


from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)


