from typing import Optional, Dict, Any

from pydantic import BaseModel


class EditPostRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image_paths: Optional[list] = None

    def dict_excluding_none(self) -> Dict[str, Any]:
        return {k: v for k, v in self.model_dump().items() if v is not None}


class EditPostResponse(BaseModel):
    pass


class GetUploadUrlResponse(BaseModel):
    upload_url: str

class UploadPostImageResponse(BaseModel):
    path: str