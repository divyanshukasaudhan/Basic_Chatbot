from chatbot import get_response


def chatbot():

    print("=" * 50)
    print("      BASIC RULE-BASED CHATBOT")
    print("=" * 50)

    print("\nType 'bye' to exit.\n")

    while True:

        user = input("You : ")

        reply = get_response(user)

        print("Bot :", reply)

        if user.lower() == "bye":
            break


if __name__ == "__main__":
    chatbot()