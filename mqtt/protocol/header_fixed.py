from mqtt.utils.types_mqtt import MessageType, QualityService


class HeaderFixedMQTTProtocol:

    def __init__(self,
                 message_type: MessageType,
                 duplicate_flag: bool,
                 quality_service: QualityService,
                 retain_flag: bool,
                 content_length: int) -> None:
        self.message_type = message_type
        self.duplicate_flag = duplicate_flag
        self.quality_service = quality_service
        self.retain_flag = retain_flag
        self.content_length = content_length
