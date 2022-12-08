class LogMixin:
    @staticmethod
    def escreva(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.escreva(f'INFO: {msg}')

    def log_erro(self, msg):
        self.escreva(f'ERRO! {msg}')
