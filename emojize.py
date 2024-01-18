import emoji

emoji_input = input("Input: ")

print("Output:", emoji.emojize(emoji_input, language='alias'))