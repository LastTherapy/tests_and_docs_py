from dataclasses import dataclass

@dataclass
class Metric:
    respiration: int
    heart_rate: int
    blushing_level: int
    pupillary_dilation: int


def get_metrics_from_user_input():
    respiration = int(input("Respiration: "))
    heart_rate = int(input("Heart rate: "))
    blushing_level = int(input("Blushing level: (6 possible level)"))
    pupillary_dilation = int(input("Pupillary dilation: "))
    return Metric(respiration, heart_rate, blushing_level, pupillary_dilation)