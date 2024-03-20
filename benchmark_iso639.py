def load_pt3_values(file_path):
    pt3_values = []
    with open(file_path, encoding="utf-8") as f:
        next(f)
        for line in f:
            row = line.rstrip().split("\t")
            pt3_values.append(row[0])
    return pt3_values


def select_library_function(library_name: str):
    if library_name == "iso639-lang":
        from iso639.iso639 import Lang

        func = lambda x: Lang(x).pt1
    elif library_name == "python-iso639":
        from iso639 import Language

        func = lambda x: Language.from_part3(x).part1
    elif library_name == "iso-639":
        from iso639 import languages

        func = lambda x: languages.get(part3=x).part1
    else:
        func = None

    return func


if __name__ == "__main__":

    import argparse
    import random

    from datetime import datetime

    n = 10000  # number of iterations to complete the benchmark

    pt3_values = load_pt3_values("iso-639-3.tab")
    benchmark_inputs = list(random.choices(pt3_values, k=n))

    parser = argparse.ArgumentParser()
    parser.add_argument("library")
    args = parser.parse_args()

    get_language_name = select_library_function(args.library)

    start_time = datetime.now()
    for pt3 in benchmark_inputs:
        try:
            language_name = get_language_name(pt3)
        except Exception:
            pass
    benchmark_duration = (datetime.now() - start_time).total_seconds()

    print(
        f"{len(benchmark_inputs)} iterations in {benchmark_duration} second(s)."
    )

    benchmark_speed = int(len(benchmark_inputs) / benchmark_duration)
    print(f"{benchmark_speed} iterations per second.")
