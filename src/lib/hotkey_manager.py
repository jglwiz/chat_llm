from .logger_manager import LoggerManager
from global_hotkeys import *

class HotkeyManager:
    def __init__(self, config, callback):
        self.config = config
        self.callback = callback
        self.logger = LoggerManager.get_logger()
        self.is_running = False
    
    def _convert_hotkey(self, hotkey_str):
        """转换热键格式
        将热键字符串转换为标准格式
        例如:
        "ctrl+shift+z" -> "control + shift + z"
        "win+1" -> "window + 1"
        """
        # 转换为小写以统一处理
        hotkey_str = hotkey_str.lower()
        
        # 替换常见的缩写
        replacements = {
            'ctrl': 'control',
            'win': 'window'
        }
        
        # 分割组合键
        parts = [part.strip() for part in hotkey_str.split('+')]
        
        # 转换每个部分
        converted_parts = []
        for part in parts:
            part = part.strip()
            # 检查是否需要替换
            if part in replacements:
                converted_parts.append(replacements[part])
            else:
                converted_parts.append(part)
        
        # 用 " + " 连接所有部分
        return " + ".join(converted_parts)
    
    def setup_global_hotkey(self):
        """设置全局热键"""
        try:
            # 如果已在运行，先停止
            if self.is_running:
                stop_checking_hotkeys()
                self.is_running = False
            
            hotkey_str = self.config['hotkeys']['show_window']
            hotkey_str = self._convert_hotkey(hotkey_str)
            bindings =  [
                    [hotkey_str, None, lambda: self.callback(), True],
            ]
            
            # 注册热键
            register_hotkeys(bindings)
            
            # 开始监听
            start_checking_hotkeys()
            self.is_running = True
            self.logger.info(f"全局热键 {hotkey_str} 注册成功")
        except Exception as e:
            self.logger.error(f"全局热键 {hotkey_str} 注册失败: {str(e)}")
    
    def __del__(self):
        """清理资源"""
        if self.is_running:
            stop_checking_hotkeys()
            self.is_running = False
