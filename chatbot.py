from responses import responses


def get_response(user_input):

    user_input = user_input.lower().strip()

    if user_input in responses:
        return responses[user_input]

    return "Sorry! I don't understand that."
