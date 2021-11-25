import re


def Bot_Response(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        Bot_Response(message, ['ассаламу', '1алейкум', 'hey','sup'], 'Ва|алейкум ассалям варах|матулох|и ва баракатух|у'),
        
        Bot_Response(message, ['тупой бот', 'goodbye'], 'сам ты бот'),

        Bot_Response(message, ['cmd', 'type cmd'], 'нажми на меня /list'),
        
        Bot_Response(message, ['how', 'are', 'you'], 'У меня все хорошо спасибо!'),
        #new
        Bot_Response(message, ['how', 'you', 'created'], 'Я был создан с помощью python и развернут на Heroku'),
        
        #Name
        Bot_Response(message, ['your', 'name'], 'Меня зовут Бот Рохана, приятно познакомиться!'), 
        #Help
        Bot_Response(message, ['урод', 'дурак'], 'Я сделаю все возможное, чтобы помочь тебе!'),
        #Website
        Bot_Response(message, ['link','links',], 'website https://rohan.ml'),
        
        #Song
        Bot_Response(message, ['play','song',], 'https://youtu.be/edzt82nC45k'),
        
        #Notes
        Bot_Response(message, ['notes','note',], 'Soon, notes will be available'),

        Bot_Response(message, ['socials','socials',], 'Here you Go\n /socials'),

        Bot_Response(message, ['source','code',], 'Here you Go\n /source_code'),
        
        #Nude Joke Lol
        Bot_Response(message, ['nude','nudes',], 'I just took a screenshot, and I\'m sending your photo to @amrohan right now, you lil horny ass😏'),
                
        #When Querry
        Bot_Response(message, ['when','?','query','question','inform','developer'], 'Inquire with the developer about this. @amrohan'),
            
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]


    print('Bot response:', bot_response)
    return bot_response
