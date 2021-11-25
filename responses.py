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
        Bot_Response(message, ['Ассаламу', '1алейкум'], 'Ва|алейкум ассалям варах|матулох|и ва баракатух|у '),
        
        Bot_Response(message, ['бот', 'тупой'], 'Давай я расскажу тебе одну историю, после которой ты станешь полным идиотом. Хотя нет, вижу, ты эту историю уже слышал.'),

        Bot_Response(message, ['сколько тебе лет', 'type cmd'], 'click me /list'),
        
        Bot_Response(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        #new
        Bot_Response(message, ['how', 'you', 'created'], 'I was created by using python and got deployed on Herkou'),
        
        #Name
        Bot_Response(message, ['your', 'name'], 'My name is Rohan\'s Bot, nice to meet you!'), 
        #Help
        Bot_Response(message, ['help', 'please'], 'I will do my best to assist you!'),
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
        
        Bot_Response(message, ['дурак','дур',], 'I дурак'),
                
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

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = ''
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response
