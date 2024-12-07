## Text to speech

# Requirements:  
Create python virtual environment and install requirements.  

python3 -m venv venv  

source venv/bin/activate   

pip install -r requirements.txt  

Note: if adding new requirements first do:  
pip install google-cloud-texttospeech   
then to save to requirements.txt:    
pip freeze > requirements.txt  

Create a google cloud project and enable their Text-To-Speech API, download a JSON credentials file (you can rename it as well).  

Create a .env with path, in this example it's in same folder as the code.   
GOOGLE_APPLICATION_CREDENTIALS=service_account.json   

# Usage:  
python main.py "Hello this is a test" "test.mp3" 