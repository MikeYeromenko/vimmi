from pydantic import BaseModel, Field, field_validator, model_validator


class IntListModel(BaseModel):
    start: int = Field(default=28)
    end: int = Field(default=117)
    step: int = Field(default=7)

    @field_validator("step")
    @classmethod
    def validate_step(cls, step: int):
        if step == 0:
            raise ValueError("Step must not be zero - we'll come to the infinite loop!")
        return step

    @model_validator(mode="after")
    def validate_all(self) -> "IntListModel":
        if self.start < self.end and self.step <= 0 or self.start > self.end and self.step >= 0:
            raise ValueError("Bad ranges")
        return self
