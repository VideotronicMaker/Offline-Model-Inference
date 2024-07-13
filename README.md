# Offline-Model-Inference-CPU

# stable_lm_1_6b_loop.py - Enhanced Conversational AI Model

This repository provides a simple Python script for interacting with the `stabilityai/stablelm-2-zephyr-1_6b` language model from Hugging Face. It has been enhanced with additional features by Gemini Advanced for a more engaging and user-friendly experience.
This code is a starting point and encourages users to utilize GPT or Gemini for assistance with adding additional features and troubleshooting.  There are 2 initial issues but they are left to prompt the user to troubleshoot with an online AI assistant.

1. **First message in terminal may be:**
   ```bash
   The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to            obtain reliable results. Setting `pad_token_id` to `eos_token_id`:100257 for open-end generation.
   The attention mask is not set and cannot be inferred from input because pad token is same as eos token.As a consequence, you may observe unexpected behavior.        Please pass your input's `attention_mask` to obtain reliable results.
2. **Error may be:**
   ```bash
   Cannot access attribute "to" for class "str"
   Attribute "to" is unknown

   These should not prevent inferencing.  
    
      

## Features

* **Continuous Conversation:** Engage in natural back-and-forth dialogue with the model.
* **Context Awareness:** The model remembers past interactions to provide contextually relevant responses.
* **Temperature Control:** Adjust the `temperature` parameter to influence the creativity and focus of the model's output.
* **Graceful Exit:** Easily end the conversation by typing "exit".

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VideotronicMaker/Offline-Model-Inference

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

(Make sure you have the correct path to requirements.txt in your terminal or command prompt)

## Usage

1. Run the script from your terminal:
   ```bash
   python stable_lm_1_6b_loop.py

Start chatting with the model. Type "exit" to quit.

Additional Notes

    This script leverages the transformers library from Hugging Face, so make sure you have enough RAM to load the model (~8GB recommended).
    You can experiment with different values for the temperature parameter to see how it affects the model's responses.
    This script is a modification of the original example provided by Hugging Face. It has been adapted to run efficiently on a CPU and include the additional features mentioned above.

Acknowledgements

    Original Model Code (CPU): stabilityai/stablelm-2-zephyr-1_6b from Hugging Face
    Enhancements: Gemini Advanced

License

This project is licensed under the MIT License - see the LICENSE file for details.


**Key Improvements:**

* **Clear Structure:** The README is organized into sections (Features, Installation, Usage, etc.) for easy navigation.
* **Concise Description:** The introduction explains the purpose and enhancements of the script.
* **Installation Instructions:** Detailed steps are provided for cloning the repository and installing dependencies.
* **Usage Guide:** Explains how to run the script and interact with the model.
* **Additional Notes:** Provides tips on resource requirements and adjusting the `temperature` parameter.
* **Acknowledgements:** Credits the original model and the developer who made the enhancements.
* **License:** Includes a standard MIT license to clarify usage permissions.

**Important:**

* Make sure to replace `yourusername` and `your-repo-name` with your actual GitHub information in the README.md file.
   




