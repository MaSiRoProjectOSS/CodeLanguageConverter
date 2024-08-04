from anthropic import Anthropic


class AnthropicCommunicator:
    def __init__(self, pre_prompt: str) -> None:
        self.model = "claude-3-5-sonnet-20240620"
        # self.model = "claude-3-sonnet-20240229"
        # self.model = "claude-3-opus-20240229"

        self.max_tokens = 4096

        self.client = Anthropic()
        self.pre_prompt = pre_prompt

    def send_and_receive_message(self, input_message: str):
        completion = self.client.messages.create(
            max_tokens=self.max_tokens,
            model=self.model,
            system=self.pre_prompt,
            messages=[
                {
                    "role": "user",
                    "content": input_message
                }
            ]
        )

        is_max = False
        # Need to check if this is the correct way to check if the completion is max tokens
        # if completion.usage.completion_tokens >= self.max_tokens:
        #     is_max = True

        return completion.content[0].text, is_max
