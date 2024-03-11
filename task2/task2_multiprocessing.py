import multiprocessing
import time

def search_in_files(files, keywords, results_queue):
    local_results = {}
    for file in files:
        try:
            with open(file, 'r') as f:
                content = f.read()
                for keyword in keywords:
                    if keyword in content:
                        if keyword not in local_results:
                            local_results[keyword] = []
                        local_results[keyword].append(file)
        except Exception as e:
            print(f"Помилка при читанні файлу {file}: {e}")
    results_queue.put(local_results)

def main():
    files = ['C:/Users/echur/Desktop/goit-cs-hw-04/task2/folder1/doc1.txt', 'C:/Users/echur/Desktop/goit-cs-hw-04/task2/folder2/doc2.txt', 'C:/Users/echur/Desktop/goit-cs-hw-04/task2/folder3/doc3.txt']
    keywords = ['Lorem', 'passages', 'Contrary']
    results = {}
    num_processes = 4

    start_time = time.time()

    results_queue = multiprocessing.Queue()

    processes = []
    chunk_size = len(files) // num_processes
    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size if i < num_processes - 1 else len(files)
        process = multiprocessing.Process(target=search_in_files, args=(files[start:end], keywords, results_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not results_queue.empty():
        local_results = results_queue.get()
        for keyword, files in local_results.items():
            if keyword not in results:
                results[keyword] = []
            results[keyword].extend(files)

    end_time = time.time()

    print("Час виконання: ", end_time - start_time)
    print(results)

if __name__ == "__main__":
    main()
