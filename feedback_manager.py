class FeedbackManager:
    def __init__(self, data_store):
        self.data_store = data_store

    def collect_feedback(self, item, feedback):
        self.data_store.add_feedbac((item, feedback))
        print(f"Feedback for '{item}' added")

    def generate_ad_content(self, item):
        feedbacl_list = self.data_store.get_feedback(item)
        if not feedback_list:
            return "No feedback yet"
