import csv
import time
from multiprocessing import Process, Queue
from os import path
from core.data_load import Test_Data_Holder, Comp_Data_Holder, Data_Holder
from core.data_types import Star_Rating
from core.utils import avg
from learning_algorithms.naive_bayes import Naive_Bayes
from learning_algorithms.simple_hybrid_system import SimpleHybridSystem

# GLOBAL VARIABLES
RELATIVE_PATH = path.dirname(__file__)
USERS_PATH = path.join(RELATIVE_PATH, 'resources/users.dat')
MOVIES_PATH = path.join(RELATIVE_PATH, 'resources/movies.dat')
RESULT_PATH = path.join(RELATIVE_PATH, 'testing/result.csv')
SAMPLE_PATH = path.join(RELATIVE_PATH, 'resources/sample_submission.csv')
TRAINING_PATH = path.join(
    RELATIVE_PATH, 'resources/training_ratings_for_kaggle_comp.csv')


def parse_file(file_path):
    d = {}
    with open(file_path, 'r', encoding="latin-1") as file:
        next(file)
        for item_string in file.readlines():
            elements = item_string.replace("\n", "").split(',')
            d[elements[2]] = elements[1]
    return d


def test_solution(answers_dict, solution_file_path, star_gap=0):
    results = parse_file(solution_file_path)
    item_count = 0
    right_answer_count = 0
    for rating_id, rating in results.items():
        item_count += 1
        if abs(int(rating) - int(answers_dict[rating_id])) < star_gap + 1:
            right_answer_count += 1
    return (right_answer_count / float(item_count)) * 100


def compare_solution(answers_dict, solution_file_path):
    exact = test_solution(answers_dict, solution_file_path)
    one_star = test_solution(answers_dict, solution_file_path, 1)
    two_stars = test_solution(answers_dict, solution_file_path, 2)
    return exact, one_star, two_stars


def write_solution_to_file(results_list, file_path):
    with open(file_path, 'w') as result_file:
        wr = csv.writer(result_file, delimiter=',', quoting=csv.QUOTE_NONE)
        wr.writerow(["user", "rating", "id"])
        for user_id, rating, movie_id in results_list:
            wr.writerow([user_id, rating.value, str(
                user_id) + "_" + str(movie_id)])


def use_nbc_solution(data: Data_Holder):
    nbc = Naive_Bayes(data.get_bayes_data(), "rating")
    return list(map(lambda x: (x[0], nbc.classify(
        data.itemize_association(x[0], x[1])), x[1]), data.movies_to_rate))


def shs_classify(q, shs, l):
    q.put(list(map(lambda x: (x[0], shs.classify(x[0], x[1]), x[1]), l)))


def use_shs_solution(data: Data_Holder):
    shs = SimpleHybridSystem(data.users, data.movies, data.ratings)
    rate_list = data.movies_to_rate
    threshold = int(len(rate_list) / 4)
    q = Queue()
    p1 = Process(target=shs_classify, args=(q, shs, rate_list[:threshold]))
    p2 = Process(target=shs_classify, args=(
        q, shs, rate_list[threshold:threshold * 2]))
    p3 = Process(target=shs_classify, args=(
        q, shs, rate_list[threshold * 2:threshold * 3]))
    p4 = Process(target=shs_classify, args=(q, shs, rate_list[threshold * 3:]))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    r1 = q.get()
    r2 = q.get()
    r3 = q.get()
    r4 = q.get()
    return r1 + r2 + r3 + r4


def use_both_solutions(data: Data_Holder):
    nbc = Naive_Bayes(data.get_bayes_data(), "rating")
    shs = SimpleHybridSystem(data.users, data.movies, data.ratings)
    results_list = []
    for user_id, movie_id in data.movies_to_rate:
        nbc_rating = nbc.classify(data.itemize_association(user_id, movie_id))
        shs_rating = shs.classify(user_id, movie_id)
        avg_rating = Star_Rating(
            int(avg([nbc_rating.value, shs_rating.value])))
        results_list.append((user_id, avg_rating, movie_id))
    return results_list


def test(solution_fnct):
    print("Fetching data from files...")
    start_time = time.time()

    # VARIABLES DECLARATION
    data_holder = Test_Data_Holder(USERS_PATH, MOVIES_PATH, TRAINING_PATH)
    test_ratio = 10.0
    chunck_size = int(data_holder.total_count / test_ratio)
    efficiency0, efficiency1, efficiency2, times = [], [], [], []

    print(time.time() - start_time, "seconds")

    for i in range(0, int(test_ratio)):
        if i == 0:
            data_holder.update_test_range(TRAINING_PATH, "START", chunck_size)
            current_time = time.time()
            solution = solution_fnct(data_holder)
        elif i == test_ratio - 1:
            data_holder.update_test_range(
                TRAINING_PATH, chunck_size * i, "END")
            current_time = time.time()
            solution = solution_fnct(data_holder)
        else:
            data_holder.update_test_range(
                TRAINING_PATH, chunck_size * i, chunck_size * (i + 1))
            current_time = time.time()
            solution = solution_fnct(data_holder)
        solution_time = time.time() - current_time
        write_solution_to_file(solution, RESULT_PATH)
        exact, one_star, two_star = compare_solution(
            data_holder.answers, RESULT_PATH)
        efficiency0.append(exact)
        efficiency1.append(one_star)
        efficiency2.append(two_star)
        times.append(solution_time)

    print("Testing solution finished!")
    print(time.time() - start_time, "seconds")
    print("Average precision for exact rating:", avg(efficiency0), "%")
    print("Average precision with 1 star incertitude:", avg(efficiency1), "%")
    print("Average precision with 2 star incertitude:", avg(efficiency2), "%")
    print("Average time:", avg(times), "seconds")


def comp(solution_fnct):
    print("Fetching data from files...")
    start_time = time.time()
    data_holder = Comp_Data_Holder(
        USERS_PATH, MOVIES_PATH, TRAINING_PATH, SAMPLE_PATH)
    print(time.time() - start_time, "seconds")
    start_time = time.time()
    print("Rendering solution...")
    write_solution_to_file(solution_fnct(data_holder), RESULT_PATH)
    print("Done!")
    print(time.time() - start_time, "seconds")


if __name__ == "__main__":

    # NAIVE BAYES CLASSIFIER
    # test(use_nbc_solution)
    # SIMPLE HYBRID RECOMMENDATION SYSTEM
    # test(use_shs_solution)
    # SOLUTIONS COMBINED
    # test(use_both_solutions)
    # Generate competition file
    comp(use_nbc_solution)
