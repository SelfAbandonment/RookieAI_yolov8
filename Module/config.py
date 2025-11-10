import os
from pathlib import Path
import sys
from typing import Any, Optional
import json

Root = Path(os.path.realpath(sys.argv[0])).parent


class Config:
    """配置管理类，提供配置文件的读取、保存和更新功能"""
    
    default = {
        "log_level": "info",
        "aim_range": 150,
        "aimBot": True,
        "confidence": 0.3,
        "aim_speed_x": 6.7,
        "aim_speed_y": 8.3,
        "model_file": "yolov8n.pt",
        "mouse_Side_Button_Witch": True,
        "ProcessMode": "single_process",
        "window_always_on_top": False,
        "target_class": "0",
        "lockKey": "VK_RBUTTON",
        "triggerType": "按下",
        "offset_centery": 0.75,
        "offset_centerx": 0.0,
        "screen_pixels_for_360_degrees": 6550,
        "screen_height_pixels": 3220,
        "near_speed_multiplier": 2.5,
        "slow_zone_radius": 0,
        "mouseMoveMode": "win32",
        "lockSpeed": 5.5,
        "jump_suppression_switch": False,
        "jump_suppression_fluctuation_range": 18
    }
    content: Optional[dict] = None

    @classmethod
    def read(cls) -> dict:
        """读取配置文件，如果文件不存在则返回默认配置"""
        try:
            config_dir = Root / "Data"
            config_file = config_dir / "settings.json"
            
            os.makedirs(config_dir, exist_ok=True)
            
            if not config_file.exists():
                return cls.default.copy()
                
            with open(config_file, "r", encoding="utf-8") as f:
                loaded_config = json.load(f)
                # 合并默认配置和加载的配置，确保所有键都存在
                return {**cls.default, **loaded_config}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"配置文件读取失败: {e}，使用默认配置")
            return cls.default.copy()

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """
        获取配置项的值，如果不存在则返回默认值
        
        Args:
            key: 配置项的键
            default: 自定义默认值，如果为None则使用类默认值
            
        Returns:
            配置项的值，类型可能是 int, str, list, float 或 bool
        """
        if cls.content is None:
            cls.content = cls.read()
        if default is not None:
            return cls.content.get(key, default)
        return cls.content.get(key, cls.default.get(key))

    @classmethod
    def update(cls, key: str, value: Any) -> None:
        """更新配置项并保存"""
        if cls.content is None:
            cls.content = cls.read()
        cls.content[key] = value
        cls.save()

    @classmethod
    def delete(cls, key: str) -> None:
        """删除配置项并保存"""
        if cls.content is None:
            cls.content = cls.read()
        if key in cls.content:
            del cls.content[key]
            cls.save()

    @classmethod
    def save(cls) -> None:
        """保存配置到文件"""
        if cls.content is None:
            cls.content = cls.read()
        
        config_dir = Root / "Data"
        config_file = config_dir / "settings.json"
        
        os.makedirs(config_dir, exist_ok=True)
        
        try:
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(cls.content, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"配置文件保存失败: {e}")
            raise
    
    @classmethod
    def reload(cls) -> None:
        """重新加载配置文件"""
        cls.content = cls.read()
