import threading
import time

def search_in_files(files, keywords, results):
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
    results.update(local_results)

def main():
    files = ['C:/Users/echur/Desktop/goit-cs-hw-04/task1/folder1/doc1.txt', 'C:/Users/echur/Desktop/goit-cs-hw-04/task1/folder2/doc2.txt', 'C:/Users/echur/Desktop/goit-cs-hw-04/task1/folder3/doc3.txt']
    keywords = ['Lorem', 'passages', 'Contrary']
    results = {}
    num_threads = 4

    start_time = time.time()

    threads = []
    chunk_size = len(files) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(files)
        thread = threading.Thread(target=search_in_files, args=(files[start:end], keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print("Час виконання: ", end_time - start_time)
    print(results)
    
    return results

if __name__ == "__main__":
    main()
