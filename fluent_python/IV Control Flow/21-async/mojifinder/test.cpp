#include <iostream>
#include <future>
#include <thread>
#include <chrono>

void task() {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "Task completed on thread: " << std::this_thread::get_id() << std::endl;
}

int main() {
    std::cout << "Main thread ID: " << std::this_thread::get_id() << std::endl;

    // Case 1: Default policy, future not captured
    // This will block main thread because the temporary future is destroyed immediately.
    // The output order will be "Task completed..." then "Main continues..."
    std::cout << "Starting async (default, no capture)..." << std::endl;
    std::async(task);
    std::cout << "Main continues after first async (might be blocked)." << std::endl;

    std::cout << "\n-----------------\n" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Small delay

    // Case 2: Explicit std::launch::async, future captured
    // This will (almost certainly) spawn a new thread and run concurrently.
    // Main thread will continue, and 'task' will print later.
    std::cout << "Starting async (explicit async, captured)..." << std::endl;
    std::future<void> f = std::async(std::launch::async, task);
    std::cout << "Main continues immediately after second async." << std::endl;
    f.get(); // Blocks main until 'f' completes, ensuring it runs before main exits.
    std::cout << "Main finished waiting for second async." << std::endl;

    std::cout << "\n-----------------\n" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Small delay

    // Case 3: Explicit std::launch::deferred, future captured
    // No new thread. 'task' runs when f.get() is called.
    std::cout << "Starting async (explicit deferred, captured)..." << std::endl;
    std::future<void> g = std::async(std::launch::deferred, task);
    std::cout << "Main continues immediately after deferred async (task not run yet)." << std::endl;
    g.get(); // Task actually runs here, on the main thread
    std::cout << "Main finished waiting for deferred async (task just ran)." << std::endl;

    return 0;
}
