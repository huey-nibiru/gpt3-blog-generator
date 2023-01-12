import openai, os, time
from secrets import api_key
from progress.bar import Bar


os.system("clear")
openai.api_key = api_key 
blogs = {}


def gpt3_prompts(PATH):   
    with open(PATH, "r") as f:
        for i in f:
            i = i.strip()
            q = ("Write me a blog about " + i + " in 500 words or more.")
            model_engine = "text-davinci-003"
            try: 
                response = openai.Completion.create(
                    engine=model_engine,
                    prompt=q,
                    max_tokens=500,
                    n=1,
                    stop=None,
                    temperature=0.7,
                )
                blogs[i] = response["choices"][0]["text"]
                time.sleep(2)
            except openai.error.ServiceUnavailableError:
                print("The server is overloaded or not ready yet.")




def download_file(PATH):
    new_dir = PATH
    counter=1
    for post in blogs:
        with open(new_dir+f"/blog_{counter}.txt", "w") as f:
            f.write(post +"\n" + blogs[post])
        counter+=1

