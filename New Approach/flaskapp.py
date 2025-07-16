from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel
import torch

# --- Load model and tokenizer ---
tokenizer = AutoTokenizer.from_pretrained("../models/flan_t5_lora_summary")
base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
model = PeftModel.from_pretrained(base_model, "../models/flan_t5_lora_summary")
model.eval().to("cuda" if torch.cuda.is_available() else "cpu")

# --- Initialize Flask app ---
app = Flask(__name__)

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json()
        text = data.get("text")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        prompt = f"Summarize this: {text}"
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=100,
                num_beams=4,
                early_stopping=True
            )

        summary = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)