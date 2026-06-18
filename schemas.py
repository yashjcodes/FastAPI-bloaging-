from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title:str=Field(min_length=1,max_length=100)
    content:str=Field(min_length=1)
    auther:str=Field(min_length=1,max_length=50)

class PostCreate(PostBase):  #inherating from the PostBase class
    pass #later we can add field 

class PostResponse(PostBase):
    id:int
    date_posted:str
    model_config = ConfigDict(from_attributes=True) #When creating this model, you can read data from an object's attributes, not just from a dictionary
