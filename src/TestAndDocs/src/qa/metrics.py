from dataclasses import dataclass
from pydantic import BaseModel, conint, confloat, Field


class Metric(BaseModel):
    respiration: conint(ge=12, le=16) = Field(..., description="Respiration rate (BPM), should be between 12-16 breaths per minute")
    heart_rate: conint(ge=60, le=100) = Field(..., description="Heart rate, should be between 60-100 beats per minute")
    blushing_level: conint(ge=1, le=6) = Field(..., description="Blushing level, should be between 1-6")
    pupillary_dilation: confloat(ge=2, le=8) = Field(..., description="Pupillary dilation, should be between 2-8 mm")


def get_metrics_from_user_input():
    respiration = int(input("Respiration: "))
    heart_rate = int(input("Heart rate: "))
    blushing_level = int(input("Blushing level: (6 possible level)"))
    pupillary_dilation = int(input("Pupillary dilation: "))

    # Здесь нужно передать аргументы как ключевые
    return Metric(respiration=respiration, heart_rate=heart_rate, blushing_level=blushing_level,
                  pupillary_dilation=pupillary_dilation)
