import logging

class Logger:
    """Клас для журналювання подій у грі."""

    def __init__(self, log_file="game.log"):
        self.logger = logging.getLogger("GameLogger")
        self.logger.setLevel(logging.INFO)
        

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        

        self.logger.addHandler(handler)

    def log(self, message: str):
        """Журналює повідомлення."""
        self.logger.info(message)
    
    def log_action(self, action: str, result: str):
        """Журналює конкретну дію та її результат."""
        self.logger.info(f"Дія: {action}, Результат: {result}")
