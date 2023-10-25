from abc import ABC, abstractmethod


class MyContent(ABC):

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(MyContent):
    def __init__(self, content_type):
        self.content_type = content_type
        self.__content = None

    def set_content(self, content):
        if self.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content, '</myML>'])
        else:
            self.__content = content


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IContent, IEmail):
    def __init__(self, protocol, content_type):
        super().__init__(content_type)
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None


    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def __repr__(self):

        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


email = Email('IM', 'MyML')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content('Hello, there!')
print(email)
