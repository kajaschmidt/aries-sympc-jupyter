from datetime import datetime

class Message:

    def __init__(self, content, state):
        self.content = content
        self.state = state
        self.time = datetime.now()
        
    def to_string(self):
        msg_str = self.time.strftime("%c")
        n = 25
        words = self.content.split()
        
        msg_chunks = [self.content[i:i+n] for i in range(0, len(self.content), n)]
        line_start = ""
        if self.state == "sent":
            line_start += (" "*25)
        current_line = ""
        for word in words:
            current_line += (word + " ")
            if len(current_line) > 25:
                msg_str += "\n"
                msg_str += (line_start + current_line)
                current_line = ""
        if not current_line == "":
            msg_str += "\n"
            msg_str += (line_start + current_line)
        msg_str += "\n"
        msg_str += ("-"*50)
        return msg_str