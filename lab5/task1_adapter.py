class Logger:
    def Log(self, message):
        print("\033[90m" + message + "\033[0m")  #Gray

    def Error(self, message):
        print("\033[91m" + message + "\033[0m")  #Black

    def Warn(self, message):
        print("\033[93m" + message + "\033[0m")  #Orange

class FileWriter:
    def Write(self, content):
        with open("output.txt", "a") as file:
            file.write(content)

    def WriteLine(self, content):
        with open("output.txt", "a") as file:
            file.write(content + "\n")

class FileLoggerAdapter(Logger):
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def Log(self, message):
        self.file_writer.Write(message)
        super().Log(message)

    def Error(self, message):
        self.file_writer.Write(message)
        super().Error(message)

    def Warn(self, message):
        self.file_writer.Write(message)
        super().Warn(message)
