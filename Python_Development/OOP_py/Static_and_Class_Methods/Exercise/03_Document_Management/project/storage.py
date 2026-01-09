from project.topic import Topic

from project.category import Category

from project.document import Document


class Storage:
    def __init__(self):
        self.categories:list[Category]= []
        self.topics:list[Topic] = []
        self.documents:list[Document] = []

    def __add_obj(self, object, object_category):
        if object not in object_category:
            object_category.append(object)

    def add_category(self,category: Category)->None:
        self.__add_obj(category, self.categories)

    def add_topic(self, topic:Topic)->None:
        self.__add_obj(topic, self.topics)

    def add_document(self, document:Document)->None:
        self.__add_obj(document, self.documents)

    @staticmethod
    def __find_object(object_id, object_collection):
        return next((o for o in object_collection if o.id == object_id), None)

    def __edit_object(self, object_id, object_collection, *new_values):
        curr_object = self.__find_object(object_id, object_collection)
        if curr_object:
            curr_object.edit(*new_values)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic,new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def __delete_object(self, object_id, object_collection):
        curr_object = self.__find_object(object_id, object_collection)
        if curr_object:
            object_collection.remove(curr_object)

    def delete_category(self,category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        curr_d = self.__find_object(document_id, self.documents)
        if curr_d:
            return curr_d
    def __repr__(self):
        return '\n'.join(repr(d) for d in self.documents)