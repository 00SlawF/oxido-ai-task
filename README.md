# oxido-ai-task
This repository is used for the Oxido recruitment task only. Written in Python, uses OpenAI.

# How to use
The main component is Python file *open_ai_api.py*. It serves as an application for connecting to OpenAI API, reading file, generating prompt, and saving the result to an HTML file.

It ensures that the text file (*tresc artykulu.txt*) the program reads is available in the working directory. The output is the HTML script, precisely the content between <body> and </body> tags
(without the tags themselves), named *artykul.html*.

The program does not ask for input; the first part of the prompt is already included there in Polish. The Python program is run with just executing the script. More details are included in the comments.
