import google.generativeai as palm

# Enter your api key
# API_KEY = 'YOUR_API_KEY'

def model(prompt, API_KEY=''):
    palm.configure(api_key = API_KEY)
    # Use the palm.list_models function to find available models:
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    # models = [m for m in palm.list_models()]
    model = models[0].name
    # print(palm.list_models(),models)
    # prompt = """
    # Hi! I am alice. How's wheather today?
    # """
    prompt ='Your name is Alice, please answer following questio: ' + str(prompt) + ', please reponse in 30 words.'
    # prompt = "Hi! I am alice. What's your name?"
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.1,
        # The maximum length of the response
        max_output_tokens=100,
    )

    return completion.result

def palm_chat(prompt, API_KEY=''):
    palm.configure(api_key = API_KEY)
    # Use the palm.list_models function to find available models:
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    response = palm.chat(messages=prompt)

    return response.last

if __name__ == '__main__':
    msg = ''
    
    while(True):
        msg = input('input: ')
        if(msg == 'q'):
            print('quit')
            break
        response = model(msg)
        # response = palm_chat(msg)
        print(f'response:{response}')
