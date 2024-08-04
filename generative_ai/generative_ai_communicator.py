from common.common_parameter import CommonParameter
from generative_ai.generative_ai_type import GenerativeAIType
from generative_ai.OpenAI_communicator import OpenAICommunicator
from generative_ai.Anthropic_communicator import AnthropicCommunicator
from generative_ai.ollama_communicator import OllamaCommunicator


class GenerativeAICommunicator:
    def __init__(self) -> None:
        self.communicators = [None]

    def create_generative_ai_client(self, pre_prompt: str):
        if GenerativeAIType.OpenAI == CommonParameter.generative_ai_type:
            self.communicators.append(OpenAICommunicator(pre_prompt))
        elif GenerativeAIType.Anthropic == CommonParameter.generative_ai_type:
            self.communicators.append(AnthropicCommunicator(pre_prompt))
        elif GenerativeAIType.ollama == CommonParameter.generative_ai_type:
            self.communicators.append(OllamaCommunicator(pre_prompt))
        else:
            raise ValueError("GenerativeAIType is invalid.")

        if self.communicators[0] == None:
            self.communicators = self.communicators[1:]

        return len(self.communicators) - 1

    def send_and_receive_message(self, communicator_id, input_message: str):
        message, is_max = self.communicators[communicator_id].send_and_receive_message(
            input_message)
        message = self.eliminate_unnecessary_message(message)

        return message, is_max

    def eliminate_unnecessary_message(self, input_text):
        text_lines = input_text.split("\n")
        quote_line_index = []
        for i, line in enumerate(text_lines):
            if line.startswith("```"):
                quote_line_index.append(i)

        output_text = ""
        if len(quote_line_index) == 0:
            output_text = input_text
        elif len(quote_line_index) == 1:
            for i, text in enumerate(text_lines):
                if i > quote_line_index[0]:
                    output_text += text + "\n"
        elif len(quote_line_index) == 2:
            for i, text in enumerate(text_lines):
                if i > quote_line_index[0] and i < quote_line_index[1]:
                    output_text += text + "\n"
        elif len(quote_line_index) % 2 == 0:
            text_accepted = False
            index_to_look = 0
            for i, text in enumerate(text_lines):
                if index_to_look >= len(quote_line_index):
                    break
                if i > quote_line_index[index_to_look]:
                    if True == text_accepted:
                        text_accepted = False
                    else:
                        text_accepted = True
                    index_to_look += 1

                if True == text_accepted:
                    if text.startswith("```"):
                        output_text += "\n"
                    else:
                        output_text += text + "\n"
        else:
            output_text = input_text

        return output_text
