from mqtt.protocol.header_fixed import HeaderFixedMQTTProtocol
from mqtt.protocol.header_variable import HeaderVariableMQTTProtocol


class MQTTProtocol:
    def __init__(self,
                 header_fixed: HeaderFixedMQTTProtocol,
                 header_variable: HeaderVariableMQTTProtocol) -> None:
        self.header_fixed = header_fixed
        self.header_variable = header_variable
