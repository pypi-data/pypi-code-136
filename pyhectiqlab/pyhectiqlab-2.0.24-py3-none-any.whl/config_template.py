import json
from pydantic import BaseModel
from pyhectiqlab import Config

"""
The ConfigTemplate is an attempt for a good practice of using
pydantic to declare our configuration files

Example usage:

```
class SubConfig(ConfigTemplate):
    path: str = Field(description="Path to the thing")
        
class MainConfig(ConfigTemplate):
    path: str = Field(description="Path to the thing")
    sizes: List[int] = Field(description="Something is one")
    sub: Optional[SubConfig] = Field(description="DoThis")

MainConfig.help() # Show help

sub = SubConfig(path="test")
config = MainConfig(path="test", sizes=[2,4,5], sub=sub) # Initialize

config = config.to_config() # Convert to pyhectiqlab.Config

```         

"""
class ConfigTemplate(BaseModel):
    """
    A config template with pydantic
    """
    @classmethod
    def help(cls):
        help_dict = cls.format_help()
        print(json.dumps(help_dict, indent=3))
    
    @classmethod
    def format_help(cls):
        # Store
        fields = cls.__fields__
        schema = cls.schema()
        help_str = {}
        for field in fields:
            if hasattr(fields[field].type_, "to_config"):
                help_str[field] = fields[field].type_.format_help()
            else:
                help_str[field] = f"[{fields[field]._type_display()}] "
                help_str[field] += f"{schema['properties'][field].get('description', 'No description')}"
        return help_str

    def to_config(self, store_description: bool = False):
        config = Config.from_dict(self.dict())
        if store_description:
            config.__help__ = self.format_help()
        return config