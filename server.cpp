#include <iostream>
#include <string>
#include <cstring>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    constexpr int PORT = 65432;
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) { perror("socket"); return 1; }

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;  // listen on all interfaces
    addr.sin_port = htons(PORT);

    if (bind(server_fd, (sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("bind"); return 1;
    }
    if (listen(server_fd, 1) < 0) {
        perror("listen"); return 1;
    }
    std::cout << "Waiting for connection on port " << PORT << "...\n";

    sockaddr_in client_addr{};
    socklen_t client_len = sizeof(client_addr);
    int client_fd = accept(server_fd, (sockaddr*)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("accept"); return 1;
    }

    char buffer[1024];
    std::memset(buffer, 0, sizeof(buffer));
    ssize_t bytes = read(client_fd, buffer, sizeof(buffer)-1);
    if (bytes < 0) {
        perror("read");
    } else {
        std::string msg(buffer);
        std::cout << "Received message: " << msg << "\n";

        // --- here’s where you “run” something in C++ ---
        // for instance, call another binary with the message as argument
        std::string cmd = "./my_cpp_app " + msg;
        int rc = std::system(cmd.c_str());
        std::cout << "External app exited with code " << rc << "\n";

        // or parse `msg` and invoke internal functions instead
    }

    close(client_fd);
    close(server_fd);
    return 0;
}


// g++ -o server server.cpp
// ./server

