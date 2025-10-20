import tiktoken

def tokenize_text(text, encoding):
    return encoding.encode(text)

def decode_tokens(tokens, encoding):
    return [encoding.decode_single_token_bytes(token) for token in tokens]

if __name__ == "__main__":
    my_text = "Dzień dobry!"
    encoding = tiktoken.get_encoding("o200k_base")
    tokens = tokenize_text(my_text, encoding)
    [print(token) for token in tokens]

    decoded_tokens = decode_tokens(tokens, encoding)
    [print(decoded_token) for decoded_token in decoded_tokens]
