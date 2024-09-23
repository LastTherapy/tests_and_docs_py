from dataclasses import dataclass
from pydantic import BaseModel, conint, confloat, Field


class Metric(BaseModel):
    """
    Represents a set of biological metrics for a person.

    Attributes:
        respiration (int): Respiration rate in breaths per minute (BPM), must be between 12 and 16.
        heart_rate (int): Heart rate in beats per minute, must be between 60 and 100.
        blushing_level (int): Blushing level, must be between 1 and 6.
        pupillary_dilation (float): Pupillary dilation in millimeters, must be between 2 and 8.
    """

    respiration: conint(ge=12, le=16) = Field(..., description="Respiration rate (BPM), should be between 12-16 breaths per minute")
    heart_rate: conint(ge=60, le=100) = Field(..., description="Heart rate, should be between 60-100 beats per minute")
    blushing_level: conint(ge=1, le=6) = Field(..., description="Blushing level, should be between 1-6")
    pupillary_dilation: confloat(ge=2, le=8) = Field(..., description="Pupillary dilation, should be between 2-8 mm")


def get_metrics_from_user_input() -> Metric:
    """
    Prompts the user to input biological metrics, validates them, and returns a Metric object.

    The function collects user input for respiration, heart rate, blushing level, and pupillary dilation.
    It validates the input using the Metric model from Pydantic to ensure that all inputs fall within
    the specified ranges.

    Raises:
        ValueError: If the user enters a value that is outside the allowed range for any metric.

    Returns:
        Metric: A validated Metric object containing respiration, heart rate, blushing level, and pupillary dilation.
    """
    respiration = int(input("Respiration (12-16): "))
    heart_rate = int(input("Heart rate (60-100): "))
    blushing_level = int(input("Blushing level: (6 possible level)"))
    pupillary_dilation = int(input("Pupillary dilation (2-8): "))

    # Здесь нужно передать аргументы как ключевые
    return Metric(respiration=respiration, heart_rate=heart_rate, blushing_level=blushing_level,
                  pupillary_dilation=pupillary_dilation)
