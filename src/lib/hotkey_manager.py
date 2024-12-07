import keyboard
from .logger_manager import LoggerManager

class HotkeyManager:
    def __init__(self, config, callback):
        self.config = config
        self.callback = callback
        self.logger = LoggerManager.get_logger()
    
    def setup_global_hotkey(self):
        """设置全局热键"""
            # 注册新热键
            
        hotkey = self.config['hotkeys']['show_window']
        try:
            keyboard.remove_hotkey(hotkey)
        except:
            pass

        try:
            keyboard.add_hotkey(hotkey, self.callback)
            self.logger.info(f"全局热键 {hotkey} 注册成功")
        except:
            self.logger.info(f"全局热键 {hotkey} 注册失败")