from langchain_text_splitters import CharacterTextSplitter
text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""
splitter = CharacterTextSplitter(
    chunk_size=500,      # max chars per chunk
    chunk_overlap=50,    # overlap to keep context
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)
print(len(chunks))