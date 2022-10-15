from datetime import datetime
from colorama import Fore


class Logger:
    class LogLevel:
        def __init__(self, name, color: str = Fore.RESET, isFatal: bool = False):
            self.name = name
            self.color = color
            self.isFatal = isFatal

        def log(self, message):
            logger = Logger()
            logger.log(message, self)
            if self.isFatal and Logger.quitWhenLogFatal:
                quit()

    logLevel = True
    colorLevelText = True
    quitWhenLogFatal = True
    colorText = True
    warnLevel = LogLevel("WARN", Fore.YELLOW)
    infoLevel = LogLevel("INFO", Fore.RESET)
    debugLevel = LogLevel("DEBUG", Fore.WHITE)
    errorLevel = LogLevel("ERROR", Fore.LIGHTRED_EX)
    fatalLevel = LogLevel("FATAL", Fore.RED)

    # def log(self, message: str, color: str = Fore.RESET, level: LogLevel = "DEBUG", end: str = "\n"):
    def log(self, message: str, level: LogLevel = debugLevel, end: str = "\n"):
        current_time = datetime.now()
        if Logger.colorText:
            if Logger.logLevel:
                print(
                    f"[{current_time.strftime('%X')}] {level.color if Logger.colorLevelText else Fore.RESET}[{level.name}]",
                    level.color + str(message), end=end + Fore.RESET)

            else:
                print(f"[{current_time.strftime('%X')}]", level.color + str(message), end=end + Fore.RESET)
        else:
            if Logger.logLevel:
                print(f"[{current_time.strftime('%X')}] [{level.name}]",
                      str(message), end=end)

            else:
                print(f"[{current_time.strftime('%X')}]", str(message), end=end)

    def log_warning(self, message: str):
        self.log(message, Logger.warnLevel)

    def log_info(self, message: str):
        self.log(message, Logger.infoLevel)

    def log_debug(self, message: str):
        self.log(message, Logger.debugLevel)

    def log_error(self, message: str):
        self.log(message, Logger.errorLevel)

    def log_fatal(self, message: str, exception=""):
        self.log(message, Logger.fatalLevel)
        if Logger.quitWhenLogFatal:
            quit(exception)
