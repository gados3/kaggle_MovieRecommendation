from operator import mul
from functools import reduce


class Naive_Bayes:

    def __init__(self, training_data, classifier_name):
        self.item_count = 0
        self.attributes_matrix = {}
        self.__gen_attributes_matrix(training_data, classifier_name)

    def __sort_items_by_classifier(self, data, classifier_name):
        sorted_items = {}
        item_count = 0
        for item in data:
            for attribute in item:
                if attribute[0] == classifier_name:
                    item.remove(attribute)
                    sorted_items[attribute].append(item)
                    break
            item_count += 1
        return sorted_items, item_count

    def __count_attributes_of_items(self, items):
        attributes = {}
        item_count = 0
        for item in items:
            for attribute in item:
                attributes[attribute] += 1
            item_count += 1
        return attributes, item_count

    def __gen_attributes_matrix(self, data, classifier_name):
        items_by_classifier, self.item_count = self.__sort_items_by_classifier(
            data, classifier_name)
        for classifier, item_array in items_by_classifier.items():
            self.attributes_matrix[classifier] = self.__count_attributes_of_items(
                item_array)

    def __prob_of_a_knowing_c(self, attribute, classifier):
        attr_dict, c_count = self.attributes_matrix[classifier]
        return attr_dict[attribute] / c_count

    def __prob_of_c(self, classifier):
        return self.attributes_matrix[classifier][1] / self.item_count

    def classify(self, item):
        best_classifier = (None, 0)
        for classifier in self.attributes_matrix:
            cond_probs = []
            for attribute in item:
                cond_probs.append(
                    self.__prob_of_a_knowing_c(attribute, classifier))
            current = reduce(mul, cond_probs, 1) * self.__prob_of_c(classifier)
            if current > best_classifier[1]:
                best_classifier = (classifier, current)
        return best_classifier[0]
