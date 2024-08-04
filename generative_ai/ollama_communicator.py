from ollama import Client
ollama_client = Client(host='http://localhost:11434')


class OllamaCommunicator:
    def __init__(self, pre_prompt: str) -> None:
        self.model = "llama3.1:8b"

        self.client = ollama_client
        self.pre_prompt = pre_prompt

    def send_and_receive_message(self, input_message: str):
        completion = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.pre_prompt},
                {"role": "user", "content": input_message}
            ]
        )

        is_max = False

        return completion['message']['content'], is_max
