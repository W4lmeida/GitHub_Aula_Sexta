import requests

'''
Este sistema funciona como um gerador de textos e também como um chatbot, pois a API da Cohere é voltada para chatbots. 
Ela pode apresentar alguns problemas de retorno, pois não foi treinada especificamente para todos os contextos, mas tivemos bons resultados.

Usei duas APIs: uma para gerar o texto e outra para traduzir. 
A API de geração responde originalmente em inglês, mesmo que o prompt peça respostas em português, então a tradução garante que todo o texto fique em português.
'''


api_key_gerador= "SEU_TOKEM_AQUI" # Aqui você coloca o teken que você gera nestes sites após crair sua conta
url_api_texto = "https://api.cohere.ai/v1/generate"
header = {
    "Authorization": f"Bearer {api_key_gerador}",
    "Content-Type": "application/json"
}

api_key_tradutor = "SEU_TOKEM_AQUI" # Aqui você coloca o teken que você gera nestes sites após crair sua conta
url_api_tradutor = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-pt"
headers = {"Authorization": f"Bearer {api_key_tradutor}"}

def tradutor(texto):
    resp = requests.post(url_api_tradutor, headers=headers, json={"inputs": texto})
    if resp.ok:
        return resp.json()[0]["translation_text"]
    return texto



while True: # Loop para deixar o codigo rodando até o usuário pedir para sair
    frase = str(input("Digite uma frase (ou digite 'sair' para encerrar): ")).strip()

    if frase.lower() == "sair":
        break
    
    dados = {
        "model": "command",
        "prompt": f"Sempre responda **100% em português do Brasil**. Não use inglês, mesmo que a pergunta esteja em outro idioma. Evite misturar idiomas. As frases também deve ser curtas. Frase do usuário: {frase}",
        "max_tokens": 1000, # Define qual será o tamanho máximo dos tokens, não define quantida de caractere mas sim de tokes, um token não necessária mente sera uma letra
    }

    resultado = requests.post(url_api_texto, headers=header, json=dados) #header só é usado se a API precisar de key

    if resultado.ok:
        texto_ingles = resultado.json()["generations"][0]["text"]
        texto_traduzido = tradutor(texto_ingles)
        
        print(f"Resposta: {texto_traduzido}\n")
    else:
        print("Error:", resultado.status_code, resultado.text)
        