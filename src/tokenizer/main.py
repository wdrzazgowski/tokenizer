import tiktoken

if __name__ == "__main__":
    encoding = tiktoken.get_encoding("cl100k_base")
    [print(encoding.decode_single_token_bytes(token)) for token in encoding.encode("Hello, Large Language Models!")]