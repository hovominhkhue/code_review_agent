# agent/llm_interface.py
import openai
import requests

class LLMClient:
    def __init__(self, provider, model, config):
        self.provider = provider
        self.model = model
        self.config = config

    def run(self, prompt, code_snippet):
        if self.provider == "openai":
            return self._call_openai(prompt, code_snippet)
        elif self.provider == "ollama":
            return self._call_ollama(prompt, code_snippet)
        elif self.provider == "anthropic":
            return self._call_claude(prompt, code_snippet)

    def _call_openai(self, prompt, code_snippet):
        openai.api_key = self.config["openai_api_key"]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": code_snippet}
            ]
        )
        return response['choices'][0]['message']['content']

    def _call_ollama(self, prompt, code_snippet):
        import json

        full_prompt = f"{prompt}\n\n{code_snippet}"
        data = {"model": self.model, "prompt": full_prompt, "stream": True}

        response = requests.post("http://localhost:11434/api/generate", json=data, stream=True)
        
        # 🧠 Ollama renvoie un flux de JSONs ligne par ligne
        output = ""
        for line in response.iter_lines():
            if line:
                try:
                    parsed = json.loads(line.decode("utf-8"))
                    output += parsed.get("response", "")
                except json.JSONDecodeError as e:
                    print("Erreur de décodage JSON :", e)

        return output

    def _call_claude(self, prompt, code_snippet):
        headers = {"x-api-key": self.config["anthropic_api_key"]}
        data = {
            "model": self.model,
            "prompt": f"{prompt}\n\n{code_snippet}",
            "max_tokens_to_sample": 1024,
        }
        response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=data)
        return response.json()["completion"]