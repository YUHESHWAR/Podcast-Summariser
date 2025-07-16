# Podcast Summarization using FLAN-T5 + LoRA + Flask

This project is a **lightweight and scalable summarization pipeline** for podcast and long-form audio transcripts. It leverages a **LoRA fine-tuned FLAN-T5** model to generate concise summaries, and provides a minimal Flask API for integration into web or batch-based systems.  

> **Note**: The current implementation reflects the **New Approach** with the **latest working code** for model loading, summarization logic, and endpoint setup based on the most recent iteration of the project.

---

## Overview

The system consists of:

- A **fine-tuned FLAN-T5 model with LoRA adapters** for abstractive summarization.
- A **Flask-based API endpoint** that accepts raw text and returns a generated summary.
- **Jupyter notebooks** to test model inference and validate summarization quality.
- Support for **YouTube transcript extraction** for real-world podcast use cases.

---

## Project Structure

```
.New Approach
├── flaskapp.py              # Flask API to serve summarization POST endpoint
├── load.ipynb              # Loads and tests the summarization model locally
├── testing.ipynb           # Runs summarization tests and evaluation metrics
├── models/
│   └── flan_t5_lora_summary/  # Directory with fine-tuned LoRA model weights
```

---

## Dependencies

Install the following packages to run the code:

| Package                  | Purpose                                                        |
|--------------------------|----------------------------------------------------------------|
| `torch`                  | Tensor computations and inference                              |
| `transformers`           | Tokenizer/model loading for FLAN-T5                            |
| `peft`                   | Parameter-Efficient Fine-Tuning (LoRA integration)             |
| `flask`                  | Serving the API for summarization                              |
| `tqdm`                   | Displaying progress bars (used in notebooks)                   |
| `evaluate`               | Summarization metric evaluation (e.g., ROUGE)                  |
| `youtube-transcript-api` | Fetching transcripts from YouTube video URLs                   |
| `IPython.display`        | Pretty printing notebook outputs                               |
| `os`, `json`             | Python built-in modules                                        |

### Installation

Run the following to install all dependencies:

```bash
pip install torch transformers peft flask tqdm evaluate youtube-transcript-api
```

---

## Notebooks Summary

### `load.ipynb`
- Loads the **FLAN-T5 base model** with **LoRA adapters**.
- Tests summarization on example inputs.
- Ensures correct device placement (CUDA/CPU).
- Uses `transformers`, `torch`, and `peft`.

### `testing.ipynb`
- Validates summarization quality on longer inputs.
- Uses `evaluate` for metrics like **ROUGE**.
- Includes progress tracking with `tqdm`.
- Fetches transcripts using `YouTubeTranscriptApi`.

---

## Model Configuration

| Setting              | Value                                |
|----------------------|----------------------------------------|
| Base Model           | `google/flan-t5-base`                 |
| LoRA Adapter Path    | `../models/flan_t5_lora_summary`      |
| Prompt Format        | `"Summarize this: <your_text>"`       |
| Generation Parameters| `max_new_tokens=100`, `num_beams=4`, `early_stopping=True` |
| Device               | Auto-detects GPU or falls back to CPU |

---

## Status

- 🔄 Actively using the **latest model loading and summarization code**.
- 🧪 Fully testable through the provided notebooks.
- 💡 Easily extendable for full pipeline use (transcription → chunking → summarization → visualization).

---

### 📚 Dataset and Credits

This model was fine-tuned on the **[`vwxyzjn/summarize_from_feedback_tldr_3_filtered`](https://huggingface.co/datasets/vwxyzjn/summarize_from_feedback_tldr_3_filtered)** dataset available on Hugging Face.

- The dataset contains high-quality human-written summaries from **TL;DR OpenAI Feedback Summarization** tasks.
- It is curated specifically for training **abstractive summarization models** with human preference alignment.

> 📢 **Credits**:  
Special thanks to **Shengyi Costa Huang** for creating and sharing the dataset publicly.