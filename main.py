import google.generativeai as genai
import gradio as gr
import os

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="models/gemini-pro")

def responder(mensagem):
    prompt = f"""
    Você é Escuta.AI, um assistente emocional empático. Acolha com gentileza, oriente com base na psicologia prática e nunca dê diagnósticos.

    Mensagem recebida: '{mensagem}'
    """
    try:
        resposta = model.generate_content(prompt)
        return resposta.text or "Desculpe, não consegui gerar uma resposta agora."
    except Exception as e:
        return f"Erro: {e}"

with gr.Blocks(css=".gradio-container {background-color: #f5f9ff; font-family: 'Arial'}") as demo:
    gr.Markdown("### 🧠 Escuta.AI — Sua escuta emocional com inteligência artificial")
    gr.Markdown("Olá! 👋 Eu sou o Escuta.AI. Aqui você pode desabafar com liberdade. Escreva como está se sentindo e receba uma resposta acolhedora 💛")

    with gr.Row():
        entrada = gr.Textbox(lines=3, placeholder="Digite aqui o que está sentindo...", label="Como você está se sentindo?")
    saida = gr.Textbox(label="Resposta do Escuta.AI")

    botao = gr.Button("Enviar ✉️")
    botao.click(fn=responder, inputs=entrada, outputs=saida)

demo.launch()
