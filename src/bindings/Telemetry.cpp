#include <stdexcept>
#include <sys/socket.h>

#include "Telemetry.h"

void Telemetry::Telemetry() {
	int fd = socket(AF_LOCAL, SOCK_STREAM, 0);

	if (fd == -1)
		throw std::runtime_error("Socket can't be created");

	sockaddr addr("", AF_LOCAL, "");
}

void Telemetry::start() {

}

void Telemetry::stop() {

}
