linguagens = ["python", "js", "c", "java", "csharp"]

# exemplos de prints usando o sorted e o parâmetro reverse
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))

# print(sorted(linguagens))