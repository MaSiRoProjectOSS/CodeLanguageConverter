from openai import OpenAI


class OpenAICommunicator:
    def __init__(self, pre_prompt: str) -> None:
        self.model = "gpt-4o"

        self.max_tokens = 4096

        self.client = OpenAI()
        self.pre_prompt = pre_prompt

    def send_and_receive_message(self, input_message: str):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.pre_prompt},
                {"role": "user", "content": input_message}
            ],
            max_tokens=self.max_tokens
        )

        is_max = False
        if completion.usage.completion_tokens >= self.max_tokens:
            is_max = True

        return completion.choices[0].message.content, is_max

    def send_image_and_receive_message(self, input_image):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                    "content": self.pre_prompt},
                {"role": "user", "content": [
                    {"type": "text", "text": "こちらが入力画像です。"},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/png;base64,{input_image}"}}
                ]}
            ],
            temperature=0.0,
        )

        return completion.choices[0].message.content
