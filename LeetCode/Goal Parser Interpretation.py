class Solution:
    def interpret(self, command: str):
        return command.replace("(al)", "al").replace("()", "o")