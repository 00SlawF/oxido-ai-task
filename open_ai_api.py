import os
from openai import OpenAI
key = os.environ.get("OPENAI_API_KEY")

# Connecting to OpenAI API
client = OpenAI(api_key = key)

# Reading a file with an article
file = open("tresc artykulu.txt", "r+")
f_text = file.read() # content of the file

# First part of the prompt - instructions in Polish
text_1 = """Przekształć tekst podany poniżej na strukturę HTML. Zastosuj odpowiednie kodowanie, aby otrzymać
poprawne znaki diakrytyczne. Ustal miejsca odpowiednie na obrazki. Wykorzystaj tag <img> z atrybutem src="image_placeholder.jpg".
Do każdego obrazka zastosuj atrybut 'alt' z tekstem, który pozwala na wygenerowanie odpowiedniej grafiki.
Za pomocą odpowiedniego tagu HTML umieść podpisy pod grafikami.
Zwróć jedynie fragment między znacznikami <body> i </body>. Samych znaczników <body> i </body> NIE dołączaj.
Podany tekst:
###\n
"""

full_content = text_1 + f_text + "\n###"

# The actual prompt
prompt = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role": "user", "content": full_content}],
)
# Obtained result (response)
response = prompt.choices[0].message.content

file.close()

# Writing the obtained result to HTML file
art = open("artykul.html", "w+")
for line in response:
    art.write(line)

art.close()
