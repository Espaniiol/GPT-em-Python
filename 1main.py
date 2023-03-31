import openai
openai.api_key="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"
while True:
 pergunta = input("Qual a sua duvida ?")

 resultado = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user","content":pergunta }]
)
 print(resultado)
 entrada = input("De [ENTER] para fazer outra pergunta (ou digite 'sair' para sair): ")
 if entrada == "sair":
        break  # Sai do loop

