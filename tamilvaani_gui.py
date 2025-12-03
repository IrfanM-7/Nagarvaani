import gradio as gr
from voice_bot.ai_response import get_ai_reply

# Gradio interface
iface = gr.Interface(
    fn=get_ai_reply,
    inputs="text",
    outputs="text",
    title="🗣️ தமிழ்வாணி - தமிழ் குரல்/உரை உதவியாளர்",
    description="தமிழில் கேள்வி கேள், தமிழில் பதில் பெறு!",
    theme="default"
)

iface.launch()
