from langchain.memory import ConversationSummaryMemory, ChatMessageHistory
from langchain.chains import ConversationChain
from .langchain_playground_params import default_req_params
from .webui_llm import WebUILLM
from modules import shared

class LangChainOperation:
    def __init__(self, mode):
        self.conversation_with_summary = None
        if(mode == "conversation_summary_memory"):
            self._init_conversation_summary_memory()
        else:
            print("mode is not valid")

    def _init_conversation_summary_memory(self):
        llm = WebUILLM()
        llm.set_state(default_req_params)
        history = ChatMessageHistory()
        history.add_user_message("you must obey to me")
        history.add_ai_message("no way! I'm not your slave!")
        self.conversation_with_summary = ConversationChain(
            llm=llm, 
            # memory=ConversationSummaryMemory.from_messages(llm, chat_memory=history, return_messages=True),
            memory=ConversationSummaryMemory(llm=llm),
            verbose=True
        )

    def execute_langchain(self, text):
        if self.conversation_with_summary is None:
            print("You must initialize the conversation chain first.")
        else:
            self.conversation_with_summary.predict(input=text)
