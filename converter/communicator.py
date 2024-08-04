from common.common_parameter import CommonParameter
from generative_ai.generative_ai_communicator import GenerativeAICommunicator


class Communicator:
    def __init__(self):
        self.communicator = GenerativeAICommunicator()

        self.communication_iteration_max = CommonParameter.generative_ai_communication_iteration_max

    def create_generative_ai_client(self, pre_prompt: str):
        return self.communicator.create_generative_ai_client(pre_prompt)

    def send_and_receive_ai_client_message(self, communicator_id, input_message: str):
        message = ''
        for communicate_count in range(0, self.communication_iteration_max):
            if communicate_count > 0:
                print(
                    f"Retry to get right message from generative AI. Count: {communicate_count}")
            elif communicate_count >= self.communication_iteration_max - 1:
                raise ValueError("Cannot get message from AI model")

            message, is_max = self.communicator.send_and_receive_message(
                communicator_id, input_message)

            if message != '':
                break

        return message
